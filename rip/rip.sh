#!/bin/bash

# $1: Number of discs to rip as part of the same album.
# $2: Path to device to rip from.

for i in $(seq 1 $1)
do
    echo -ne "\aInsert disc $i and press ENTER to continue..."
    read
    
    echo "Ripping disc $i"
    cdparanoia -qB -d $2
    
    for file in track*.cdda.wav
    do
        mv "$file" "disc${i}_${file}"
    done
    
    echo "Done with disc $i"
done

echo "Encoding files to FLAC"
for file in *.wav
do
    flac -s $file
    rm $file
done

echo "Finished"
