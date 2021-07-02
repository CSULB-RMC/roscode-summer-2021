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

#omega long command to get list of local IP addresses.  lots of regex
HOSTIP=`ip addr show|grep -Po 'inet.*(?<!lo|docker\d)$'|grep -Po '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?=/)'`
printf "Host ip: %s\n", ${HOSTIP[0]}

if [[ -z "${JOYDEV}" ]]; then
    printf "${YELLOW}Warning: Controller not detected.  The joy node will be non-operational.${NC}\n"
else
    JOYPARAM="--device=$JOYDEV"
fi


DOCPARAMS="--network host -e ROS_MASTER_URI=http://${HOSTIP[0]}:11311 -e ROS_HOSTNAME=${HOSTIP[0]} -v $PWD:/ros -w /ros"

docker build --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) docker -t rmc:ros
docker run $DOCPARAMS $JOYPARAM --rm -it rmc:ros /bin/bash