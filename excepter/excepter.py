# excepter.py
# Writes a Java exception manually with whatever name you want on it.

import sys

# Declarations
template = ["public class {0} extends {1} {{\n",
            "   public {0}() {{\n",
            "       super();\n",
            "   }}\n",
            "   \n",
            "   public {0}(String msg) {{\n",
            "       super(msg);\n",
            "   }}\n",
            "}}\n"]
extends = "Exception"

# Cycle through arguments
sys.argv.pop(0)
for arg in sys.argv:
    # Flags
    if arg[0] == '-':
        if arg == "-r" or arg == "--runtime-exception":
            extends = "RuntimeException"
        elif arg == "-e" or arg == "--exception":
            extends = "Exception"
    # Input
    else:
        out = open(arg + "Exception.java", "w")
        for line in template:
            out.write(line.format(arg + "Exception", extends))
