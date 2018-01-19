#!/bin/bash

# $1: Determines whether an even byte should be generated. This is
#     required for the first byte of a MAC address to be valid, but can
#     be left false otherwise.
function random_hex_byte {
    digits='0123456789abcdef'
    
    if [[ $1 = even ]]
    then
        byte=$(( ($RANDOM % 128) * 2 ))
    else
        byte=$(( $RANDOM % 256 ))
    fi
    
    byte_as_hex=${digits:$(( $byte / 16 )):1}
    byte_as_hex="$byte_as_hex${digits:$(( $byte % 16 )):1}"
    
    echo $byte_as_hex
}

function random_mac_address {
    # One iteration for each byte
    for i in even any any any any any
    do
        # Add separator (:) if necessary
        if [[ "$mac_address" != '' ]]
        then
            mac_address="$mac_address:"
        fi
        
        mac_address="$mac_address$(random_hex_byte $i)"
    done
    
    echo "$mac_address"
}

# (main)
# $1: Name of network interface to spoof.
mac_address=$(random_mac_address)

ifconfig $1 down
ip link set dev $1 address $mac_address
ifconfig $1 up

echo "$1 successfully set to $mac_address"
