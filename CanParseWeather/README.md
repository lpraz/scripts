# CanParseWeather.py
Generates a fancy climate data table in MediaWiki markup from an Environment
Canada .csv of climate data, for inserting into Wikipedia articles.

## Usage
Run canparseweather.py with two arguments: the first for the input .csv file,
and the second for the name of the output markup file you want to generate.
For example:
```
python canparseweather.py brandon.csv brandon.txt
```
will read from a file called `brandon.csv` and output to a file called
`brandon.txt`.
