# macspoof.sh
Changes your network interface's MAC address to a random one. Use this
one for good, not evil.

## Usage
`./macspoof.sh <interface>`, where `<interface>` is the name of your
network interface. This is usually `eth0` for a wired interface, or
`wlan0` for a wireless interface, but check with `ifconfig` first in
case it's different on your system.

Because this script uses `ifconfig` and `ip`, it may need `sudo` to
work correctly.
