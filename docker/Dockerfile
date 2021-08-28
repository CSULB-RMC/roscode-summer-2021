FROM ros:noetic-ros-base

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user

RUN usermod -aG sudo user
RUN echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN apt-get update
RUN apt-get install -y xboxdrv ros-noetic-joy
#we used to install ros-noetic-joystick-drivers, but something broke with it.
#ros-noetic-joy should have the drivers we need though...

USER user
