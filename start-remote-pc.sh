#!/bin/bash
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

JOYDEV=
#JOYDEV=/dev/null
for ((i=0; i <=5; i++)); do
#printf "testing /dev/input/js$i\n"
    if [ -e "/dev/input/js$i" ]; then
        printf "/dev/input/js$i exists.\n"
        JOYDEV=/dev/input/js$i
        break
    fi
done

#eh forget about this for now i dont want to spend time making it work
#if command -v udevadm &> /dev/null; then
#    printf "Dev is %s\n" `udevadm info --attribute-walk --name $JOYDEV|grep -Po '(?<=name}==")(.*)(?<=")'`
#    #'(?:.*ATTRS\{name\}==\")(.*)(?:\")'`
#fi
#printf
#ROSHOST=`ip -4 addr show enp5s0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'`
#if [[ -z "${JOYDEV}" ]]; then
#    DOCPARAMS=-e 

#else
#fi
if [[ -z "${JOYDEV}" ]]; then
    printf "${YELLOW}Warning: Controller not detected.  The joy node will be non-operational.${NC}\n"
else
    JOYPARAM="--device=$JOYDEV"
fi


DOCPARAMS="--network host -e ROS_MASTER_URI=http://localhost:11311 -e ROS_HOSTNAME=localhost -v $PWD:/ros -w /ros"

docker run $DOCPARAMS $JOYPARAM --rm -it $(docker build --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -q docker) /bin/bash