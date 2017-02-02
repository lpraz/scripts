#/bin/sh

wait=3

while [ true ]; do
    battery_level=$(sudo cat /sys/class/power_supply/BAT1/status)
    if [ "$battery_level" = "Discharging" ]; then
        echo "[battbeep.sh] Running on battery power, check your AC connection!"
        while [ "$battery_level" = "Discharging" ]; do
            beep -f 1000 -l 400 -n -f 500 -l 400
        done
    fi
    sleep "$wait"
done
