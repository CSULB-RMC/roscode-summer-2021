#!/bin/bash
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

JOYDEV=/dev/null
for ((i=0; i <=5; i++)); do
#printf "testing /dev/input/js$i\n"
    if [ -e "/dev/input/js$i" ]; then
        printf "/dev/input/js$i exists.\n"
        JOYDEV=/dev/input/js$i
        break
    fi
done
if command -v udevadm &> /dev/null; then
    printf "Dev is %s\n" `udevadm info --attribute-walk --name $JOYDEV|grep -Po '(?<=name}==")(.*)(?<=")'`
    #'(?:.*ATTRS\{name\}==\")(.*)(?:\")'`
fi
#printf

printf "${YELLOW}Warning: Controller not detected.  The joy node will be non-operational.${NC}\n"

#docker run --rm -it $(docker build -q docker)