FROM ros:noetic-ros-base

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user


RUN apt-get update
RUN apt-get install -y xboxdrv ros-noetic-joy ros-noetic-joystick-drivers
USER user