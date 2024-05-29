---
title: Jupyter on UConn's HPC cluster
author: Jeremy Teitelbaum
subtitle: Fundamentals of Data Science
---



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
$ srun  --partition=class --account=classroom --qos=classroom --pty bash 
```
Make a note of the node where your interactive process is running.  This is in the prompt. It will be something like `cn560`.

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

## Moving a file to the cluster

If you can login to the cluster successfully using `ssh` then you can transfer a file
to the cluster from your laptop using `rsync`.  From a shell on your **local machine:**

```bash
rsync filename <netID>@hpc2.storrs.hpc.uconn.edu
```


## Getting a file from the cluster

To transfer a file from the cluster to your local machine, run the following command from a shell
*on your local machine.*

```bash
rsync <netID>@hpc2.storrs.hpc.uconn.edu:filename .
```