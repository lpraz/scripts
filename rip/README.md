# rip.sh
Rips an album using cdparanoia and re-encodes it as FLAC.

## Usage
`./rip.sh <num_disks> <device>`, where `<num_disks>` is the number of disks
that form the album, and `<device>` is the device (usually an optical drive)
to rip from. Output is one-file-per-track (using cdparanoia's -B flag), to the
current working directory.

This script requires cdparanoia and flac to run.
