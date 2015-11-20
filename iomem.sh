#!/bin/bash

while IFS='-: ' read b e used_by; do
     set -- $(printf "%d %d" 0x$b 0x$e)
     echo "$1 to $2 bytes ($(($1/1024/1024)) to $(($2/1024/1024)) Mb) - $used_by"
done < /proc/iomem
