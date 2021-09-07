# transcode.py
Transfers a music collection (in root folder and all subfolders) from a source
folder to a destination folder and re-encodes all FLAC files as Opus. Useful
for keeping any lossless copies of music you have while conserving space on
something where you won't need the full quality of the lossless files on
(eg: a smartphone with limited storage, or a MicroSD card).

This script will attempt to keep the destination in sync with the source by
comparing file names between the source and destination, copying/transcoding
any files that aren't in the destination, and deleting any files from the
destination that aren't in the source.

## Usage
`./transcode.py <source> <destination>`, where `<source>` and `<destination>`
are paths to the source of a music collection, and the desired destination to
copy/sync it to.

Python 3 and ffmpeg (and the FLAC/Opus codecs) are required.