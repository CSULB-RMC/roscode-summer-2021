# CSULB's ROS code repository for Nasa Lunabotics

This repo contains all of the needed files in order to start and run the rover.  The rover uses an ARM based processor on board to process autonomy and run the teleop code.

The rover is programmed with a system called ROS (Robot Operating System).  If you wish to learn more about what ROS is, I suggest you checkout their website [here](https://www.ros.org/).

We have two main ROS packages, `rmc_teleop` and `rmc_autonomy` (located in the `catkin_ws/src` folder) which contain the code needed in order to run the rover in teleop and autonomous mode respectively.

Because ROS can be a bit of a pain to setup, we utilize [Docker](https://www.docker.com/) to automate creating an environment where we can run our code.

## What is Docker?

Docker is a system used for managing "containers", that is, environments completely isolated from your main operating system that can run it's own operating system.  Although it's a bit more complex, you can think of a docker container like a tiny Virtual Machine, where the only way you can communicate it is through terminal.  If you want a more in depth explanation of exactly how Docker works behind the scenes, I recommend you check out [here](https://docs.docker.com/get-started/overview/).

## How do we use Docker?

We use docker in this project to setup ROS automatically for us.  The [`docker/Dockerfile`](docker/Dockerfile) file contains the configuration we use for setting up our docker container.

While most of the configuration is done by [ROS's official docker images](https://hub.docker.com/_/ros/), which is what we use as a base, we do make a few modifications to it.  Namely, we configure the user to have the same UID and GID as the host's user, that way any files created within the container can be edited like normal through external text editors or whatever you have on your system.  In addition, we also automatically install some packages which are needed for our code to run.

A script to automatically create a docker container from the Dockerfile is located at the root of this repo as [`start-remote-pc.sh`](start-remote-pc.sh).

## How do I use this repo?

In order to use this repo to create a ROS development environment or to run our ROS code, you must meet the following requirements:

### System Requirements
- Must be running a Linux based operating system (Ubuntu, Debian, Pop!_OS, Manjaro, Arch, etc...)
- Git (Instructions on how to install [here](https://www.linuxfordevices.com/tutorials/ubuntu/install-git-on-ubuntu).  Just go up to step 3.)
- Latest stable version of Docker installed.  Recommended instructions on how to do that for Ubuntu are [here](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script).
- (Recommended) Add your user to the docker group so you can run docker without sudo/root.  Recommended instructions [here](https://www.configserverfirewall.com/ubuntu-linux/add-user-to-docker-group-ubuntu/).
- (Optional) Some kind of gamepad/controller/joystick to be able to run/debug the teleop code.

Note: In the future, I hope to make a way for Windows users to easily use this code too, but for the time being, it's Linux only.

### Downloading the Repo

Open up the "Terminal" program, and type the following command to download the repository.

```
git clone https://github.com/CSULB-RMC/roscode-summer-2021.git
```
Then move into that directory with this command:

```
cd roscode-summer-2021
```

### Starting the Container

Now lets test running the container.  Run the following command and it should give us a terminal in the newly created container.

```
./start-remote-pc.sh
```

Note: depending on the speed of your internet/computer, this command could take a few minutes to complete.

Once the command is completed, you should have the following prompt (ending with `/ros$`) if everything was successful, as shown in the image below.  Note: you may have a lot more that was put into the terminal as output if this was your first time running that command.

![Docker has been setup.](docs/containersetup.png)

## Running commands within the Container

Now that you have a ROS environment, you can follow along with any of the [ROS tutorials](http://wiki.ros.org/ROS/Tutorials), or you can continue reading to try running the ROS packages we have already created.

The following section is WIP and a bit sparce.  Please contact me if you need help following along, but I will continue to update it as we go along.

### Building the Catkin Packages

Run the following:
```
cd catkin_ws
caktin_make
source devel/setup.bash
```

Then you can run any of our nodes like so:

Teleop:
```
rosrun rmc_teleop teleop.py
```

Autonomy:
```
rosrun rmc_autonomy autonomy.py
```

As mentioned earlier, this section will be updated and improved in the future.