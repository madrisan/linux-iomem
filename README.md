# linux-iomem
Display I/O memory map in Linux 2.4+

This script parses `/proc/iomem` and display in a human readable format the current map of the system's memory for each physical device.

#### Example of output

```
0 bytes to 4095 bytes (0 M to 0 M) - reserved
4096 bytes to 360447 bytes (0 M to 0 M) - System RAM
360448 bytes to 364543 bytes (0 M to 0 M) - reserved
364544 bytes to 647167 bytes (0 M to 0 M) - System RAM
647168 bytes to 655359 bytes (0 M to 0 M) - reserved
655360 bytes to 786431 bytes (0 M to 0 M) - PCI Bus 0000:00
786432 bytes to 802815 bytes (0 M to 0 M) - PCI Bus 0000:00
802816 bytes to 819199 bytes (0 M to 0 M) - PCI Bus 0000:00
819200 bytes to 835583 bytes (0 M to 0 M) - PCI Bus 0000:00
835584 bytes to 851967 bytes (0 M to 0 M) - PCI Bus 0000:00
851968 bytes to 868351 bytes (0 M to 0 M) - PCI Bus 0000:00
868352 bytes to 884735 bytes (0 M to 0 M) - PCI Bus 0000:00
884736 bytes to 901119 bytes (0 M to 0 M) - PCI Bus 0000:00
901120 bytes to 917503 bytes (0 M to 0 M) - PCI Bus 0000:00
917504 bytes to 933887 bytes (0 M to 0 M) - PCI Bus 0000:00
933888 bytes to 950271 bytes (0 M to 0 M) - PCI Bus 0000:00
950272 bytes to 966655 bytes (0 M to 0 M) - PCI Bus 0000:00
966656 bytes to 983039 bytes (0 M to 0 M) - PCI Bus 0000:00
983040 bytes to 1048575 bytes (0 M to 0 M) - System ROM
1048576 bytes to 3112529919 bytes (1 M to 2968 M) - System RAM
16777216 bytes to 21926657 bytes (16 M to 20 M) - Kernel code
21926658 bytes to 26042367 bytes (20 M to 24 M) - Kernel data
27062272 bytes to 27844607 bytes (25 M to 26 M) - Kernel bss
3112529920 bytes to 3112558591 bytes (2968 M to 2968 M) - ACPI Non-volatile Storage
3112558592 bytes to 3121393663 bytes (2968 M to 2976 M) - System RAM
...
```
