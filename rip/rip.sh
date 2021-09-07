#!/bin/bash

# $1: Number of discs to rip as part of the same album.
# $2: Path to device to rip from.

for i in $(seq 1 $1)
do
    eject $2
    echo -ne "\aInsert disc $i and press ENTER to continue..."
    read
    eject -t $2
    sleep 15 # TODO: check for CD present (mounted?) in drive
    
    echo "Ripping disc $i"
    cdparanoia -qB -d $2
    
    for file in track*.cdda.wav
    do
        mv "$file" "disc${i}_${file}"
    done
    
    echo "Done with disc $i"
done

eject $2
echo "Encoding files to FLAC"
for file in *.wav
do
    flac -s $file
    rm $file
done

echo "Finished"
