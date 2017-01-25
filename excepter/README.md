# excepter.py
Java exceptions are kind of tedious to write. This does it for you.

## Usage
Run `excepter.py` with any number of command-line arguments.
Anything after a `-r` or a `--runtime-exception` switch will extend
`RuntimeException`, and anything after a `-e` or a `--exception` switch
(or by default) will extend `Exception`. For example:

```
python excepter.py An -r Another -e YetAnother
```

will make the following:

```
AnException.java            extends Exception
AnotherException.java       extends RuntimeException
YetAnotherException.java    extends Exception
```
