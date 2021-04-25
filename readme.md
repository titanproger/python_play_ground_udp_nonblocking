The third task is to write a Python script using coroutines that non-blockingly sends random integers as text via UDP to a local socket 11234, and prints strings received via the UDP socket 11235.
Usage of any blocking constructs is not permitted.
Hint: use Netcat for testing, e.g., nc -p 11234 -u localhost 11235
Hint: the solution can be implemented in approximately 20 lines of code.



# Prerequire
   Docker comatible linux distro. (Ubuntu 20.04 - ok )


## Using docker

 - install docker from  offical site https://docs.docker.com/engine/install/debian/
 - install docker-compuse tool https://docs.docker.com/compose/install/
 - add your user to docker group (to avoid sudo ): sudo usermod -aG docker $USER

 - choose option - 1)pull ready image or 2)build on your own:

### Option 1) Pull ready image from dockerhub
  run `./docker_pull.sh`

### Option 2) Build image form scratch
  run `./docker_build.sh`

### Start sandbox
  1) run `./docker_start.sh`

  in sandbox run `run_listener.sh`

  2) open new terminal
     run `./docker_start.sh`
     in sandbox run `run_task.sh`

     check first console - there should be random numbers

  3) open new terminal
     run `./docker_start.sh`
     in sandbox run `run_sender.sh`

     type any message + Enter
      check this message appear in console 2 (where task is running)





