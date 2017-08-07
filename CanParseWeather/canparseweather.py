import csv
import datetime
import sys

def get_row(row, data_name, special = None):
    """
    Inputs a list (row) of data which will have 13 temperature values
    within it, a string (template_name) that will be used to refer to
    each piece of data within the Wikicode template, and another string
    (comment) used to add a comment to the Wikicode template as a
    header. Outputs a block of Wikicode - first, a comment with proper
    formatting (from comment param), then the temperature data, put in
    the format of Template:Weather box, using template_name for each
    cell of data.
    """
    # Declarations
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "year")
    special_tags = ("|" + data_name.split(' ', 1)[0] + " colour=green\n",
                    "|unit " + data_name + "=0.2 mm\n")
    output = ""
    
    # Add colour tag/unit tag, if present
    try:
        output += special_tags[special]
    except:
        pass
    
    # Add monthly/yearly data
    for element in range(1, 14):
        output += ("|" + months[element - 1] + " " +
                   data_name + "=" + row[element] + "\n")
    return output

def upper_to_title(input):
    """
    Converts a string in all-uppercase to title-case, most of the time.
    Can't guess capitals in the middle of words, all-caps acronyms, or
    words that should be all-lowercase to be gramatically correct.
    """
    end_chars = (" ", "-")
    make_upper = False
    output = ""
    
    if input[0 : 1].isalpha():
        output += input[0 : 1]
    else:
        make_upper = True
    
    for char in range(1, len(input)):
        if make_upper:
            output += input[char : char + 1]
            make_upper = False
        else:
            output += input[char : char + 1].lower()
        # Is the current character something that ends a word?
        for end_char in end_chars:
            if input[char : char + 1] == end_char:
                make_upper = True
    
    return output  

def parse_csv(reader):
    """
    Scans the CSV file, and fills in an output list with all of the
    parts of the Weather box template that can be found in the CSV,
    including some information for the Cite web template.
    """
    tags = {"Daily Average (°C)": ("mean C", None),
            "Daily Maximum (°C)": ("high C", None),
            "Daily Minimum (°C)": ("low C", None),
            "Extreme Maximum (°C)": ("record high C", None),
            "Extreme Minimum (°C)": ("record low C", None),
            "Precipitation (mm)" : ("precipitation mm", 0),
            "Rainfall (mm)": ("rain mm", 0),
            "Snowfall (cm)": ("snow cm", 0),
            0: ("precipitation days", 1),
            1: ("rain days", 1),
            2: ("snow days", 1),
            "Total Hours": ("sun", None),
            "% of possible daylight hours": ("percentsun", None)}
    flags = ("Days with Precipitation",
             "Days with Rainfall",
             "Days With Snowfall",
             "STATION_NAME")
    output = ""
    flag = 4
    place_name = ""
    
    for row in reader:
        if len(row) > 0: # Make sure a blank line isn't being read
            # Flag actions
            if flag != None:
                # Location
                if flag == 3:
                    place_name = (upper_to_title(row[0]), row[1])
                    output += "|location = " + place_name[0] + " (" + header + ")\n"
                # CSV title ("Climate Normals 19x0-xxx0 Station Data")
                elif flag == 4:
                    header = row[0]
                # Days with precipitation (all, rain, snow)
                else:
                    output += get_row(row, *tags[flag])
                flag = None
            
            # Temperature, precipitation amt. values
            try:
                output += get_row(row, *tags[row[0]])
            except:
                pass
            
            # Set flag (watch out for...on next line)
            try:
                flag = flags.index(row[0])
            except:
                pass
    
    output += ("|source 1=\n" +
               "<ref>\n" + 
               "{{Cite web\n" +
               "|title=" + place_name[0] + ", " + place_name[1] + "\n" +
               "|work=" + header + "\n" +
               "|url=<!--Add me!-->" + "\n")
    
    return output

def main():
    """
    Main method. Handles file operations and output of program
    activities to the user.
    """
    # Validate input: Right amount of args?
    if len(sys.argv) != 3:
        print("Invalid number of arguments!",
              "Should have an input and an output.")
    else:
        # Take input from args
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        
        # Populate output
        print("Loading %s..." % input_path);
        with open(input_path, encoding='iso-8859-1') as input_csv:
            reader = csv.reader(input_csv, delimiter=",", quotechar="\"")
            output = ("<!--This template was auto-generated. " +
                      "Please check for any errors or fields left " +
                      "incomplete.-->\n" + 
                      "{{Weather box\n" +
                      "|collapsed=yes\n" +
                      "|metric first=yes\n" + 
                      "|single line=yes\n" +
                      parse_csv(reader) +
                      "|publisher=Environment Canada\n" +
                      "|accessdate=" + datetime.date.today().isoformat() + "\n" 
                      "}}\n" +
                      "</ref>\n" +
                      "}}")
        
        # Output
        print("Writing to %s..." % output_path)
        with open(output_path, mode = "w") as output_txt:
            output_txt.write(output)
        print("File successfully written to " + output_path + ".")
        print("Insert your citation URL before saving to an article.")

if __name__ == "__main__":
    main();
