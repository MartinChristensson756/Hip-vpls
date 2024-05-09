# About

Virtual Private LAN Services are common place in modern networking. 
This repository contains implementation of VPLS based on Host Identity Protocol.

# Introduction
Host Identity Protocol, or HIP, is a layer 3.5 solution, which was initially designed to 
split the dual role of the IP address as both locator and identifier. By using the HIP protocol, 
one can address not only mobility issues but also establish an authenticated secure channel. 
This repository contains a simple implementation of HIP-VPLS. In this version, HMAC classes 
have been updated. The classes that have been updated is HMAC-SHA1, HMAC-SHA256 and HMAC-SHA384 and 
they are now using the cryptography library instead of pycryptodome. 


# Usage
At the moment the setup is simple. We have four routers, which form the HIP VPLS and five switches
connecting hosts and routers. There are also four hosts that are agnostic about the topology used.

First clone the repository:
```
$ cd ~
$ git clone https://github.com/MartinChristensson756/Hip-vpls.git
```

After this step is done you can deploy the topology:

```
$ cd hip-vpls
$ sudo bash deploy.sh
```
The script should install Mininet and start the topology if it does not
run  the following command to start the topology:

```
$ cd ~
$ cd hip-vpls
$ sudo python3 hipls-mn.py
```

The script can be executed from the Tools folder by running the following command to initiate 
the topology and perform the iperf3 test, which varies parameters like buffer length and window size.

$ cd ~
$ cd Tools
$ sudo python3 hipls.py
```

Base exchange should complete its execution in a few seconds. 

Once BEX is done, you should be able to ping h2 from h1 as follows (from the mininet):

```
mininet> h1 ping h2
```
