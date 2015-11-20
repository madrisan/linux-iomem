# linux-iomem
Display I/O memory map in Linux 2.4+

This script parses `/proc/iomem` and display in a human readable format the current map of the system's memory for each physical device.

#### Example of output

```
0 to 4095 bytes (0 to 0 Mb) - reserved
4096 to 360447 bytes (0 to 0 Mb) - System RAM
360448 to 364543 bytes (0 to 0 Mb) - reserved
364544 to 647167 bytes (0 to 0 Mb) - System RAM
647168 to 655359 bytes (0 to 0 Mb) - reserved
655360 to 786431 bytes (0 to 0 Mb) - PCI Bus 0000:00
786432 to 802815 bytes (0 to 0 Mb) - PCI Bus 0000:00
802816 to 819199 bytes (0 to 0 Mb) - PCI Bus 0000:00
819200 to 835583 bytes (0 to 0 Mb) - PCI Bus 0000:00
835584 to 851967 bytes (0 to 0 Mb) - PCI Bus 0000:00
851968 to 868351 bytes (0 to 0 Mb) - PCI Bus 0000:00
868352 to 884735 bytes (0 to 0 Mb) - PCI Bus 0000:00
884736 to 901119 bytes (0 to 0 Mb) - PCI Bus 0000:00
901120 to 917503 bytes (0 to 0 Mb) - PCI Bus 0000:00
917504 to 933887 bytes (0 to 0 Mb) - PCI Bus 0000:00
933888 to 950271 bytes (0 to 0 Mb) - PCI Bus 0000:00
950272 to 966655 bytes (0 to 0 Mb) - PCI Bus 0000:00
966656 to 983039 bytes (0 to 0 Mb) - PCI Bus 0000:00
983040 to 1048575 bytes (0 to 0 Mb) - System ROM
1048576 to 3112529919 bytes (1 to 2968 Mb) - System RAM
16777216 to 21926657 bytes (16 to 20 Mb) - Kernel code
21926658 to 26042367 bytes (20 to 24 Mb) - Kernel data
27062272 to 27844607 bytes (25 to 26 Mb) - Kernel bss
3112529920 to 3112558591 bytes (2968 to 2968 Mb) - ACPI Non-volatile Storage
3112558592 to 3121393663 bytes (2968 to 2976 Mb) - System RAM
...
```
