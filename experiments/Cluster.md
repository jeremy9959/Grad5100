## To start jupyter on the cluster



1. **On your local machine:** Login to the login node:

```bash
$ ssh netID@hpc2.storrs.hpc.uconn.edu
```

You need to install anaconda on your account on the cluster. To do this you 
can use wget to download the installer and then run it and follow
the installation prompts as usual. You only need to do this part once!

```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
$ sh Anaconda3-2023.03-1-Linux-x86_64.sh
```
Now check if python and jupyter lab work.

If jupyter lab won't run
because of a libc++.so.6.o error, you can  run

```bash
$ conda install -c anaconda libstdcxx-ng
```

2. **On the cluster:** Start an interactive process

```bash
$ srun --nodes=1 --mem=32G --pty=bash
```
Make a note of the node where your interactive process is running.  This is in the prompt. 

3. **On the cluster:** Start jupyter on the interactive node

```bash
$ jupyter lab --no-browser --ip='*'
```

Make a note of the token provided by the jupyter lab process and the port
where the server is running. 

4. **On your local machine:** Create an ssh tunnel to the jupyter server.

```bash
$ ssh -NL localhost:8888:node:port netID@hpc2.storrs.hpc.uconn.edu
```

5. **On your local machine:** Open a web browser and point it at localhost:8888.

With luck, you're running jupyter on a node in the cluster!
