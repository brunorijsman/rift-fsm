# Routing In Fat Trees (RIFT)

This repository contains an implementation of the Routing In Fat Trees (RIFT) protocol specificied in Internet Draft (ID)
[draft-draft-rift-02](https://tools.ietf.org/html/draft-ietf-rift-rift-02)

The code is currently still a work in progress. Only the Link Information Element (LIE) Finite State Machine (FSM) is complete.

It will be used for interoperability testing in the hackathon at the Internet Engineering Task Force (IETF) meeting number 102 in Montreal (July 2018).

# Installation Instructions

## Linux (Ubuntu Server 16.04 LTS)

I am using an Amazon Web Services (AWS) Elastic Compute Cloud (EC2) t2.micro instance with Amazon Machine Image (AMI) "Ubuntu Server 16.04 LTS (HVM), SSD Volume Type" (ami-ba602bc2), which is free-tier eligible.

### Login to Ubuntu

If you are using an Ubuntu instance on AWS, use user name ubuntu and your private key file to login (the following command assumes you are logging in from Linux or Mac OS X)

<pre>
$ <b>ssh ubuntu@<i>ec2-instance-ip-address</i> -i ~/.ssh/<i>your-private-key-file</i>.pem</b> 
</pre>

### Update apt-get

Install the latest security patches on your EC2 instance by doing an update:

<pre>
$ <b>sudo apt-get update</b>
</pre>

### Install Python3

The code is written in Python 3 and tested using version 3.5.1. It will not run using Python 2.

Python 3 comes pre-installed on the AWS Ubuntu AMI:

<pre>
$ <b>python3 --version</b>
Python 3.5.2
</pre>

However, if you need to install Python 3 yourself you can do so as follows:

<pre>
$ <b>sudo apt-get install -y python3</b>
</pre>

### Install virtualenv

A Python virtual environment is a mechanism to keep all project dependencies together and isolated from the dependencies of other projects you may be working on to avoid conflicts.

Install virtualenv so that you can create a virtual environment for your project later on in the installation process:

<pre>
$ <b>sudo apt-get install -y virtualenv</b>
</pre>

Verify that virtualenv has been properly installed by asking for the version (the exact version number may be different when you run the command, which is okay):

<pre>
$ <b>virtualenv --version</b>
15.0.1
</pre>

### Install git

You git to clone clone this repository onto the EC2 instance.

Git comes pre-installed on the AWS Ubuntu AMI:

<pre>
$ <b>git --version</b>
git version 2.7.4
</pre>

However, if you need to install git yourself you can do so as follows:

<pre>
$ <b>sudo apt-get install -y git</b>
</pre>

### Clone the repository

Clone this rift-fsm repository from github onto the EC2 instance:

<pre>
$ <b>$ git clone https://github.com/brunorijsman/rift-fsm.git</b>
Cloning into 'rift-fsm'...
remote: Counting objects: 276, done.
remote: Compressing objects: 100% (194/194), done.
remote: Total 276 (delta 172), reused 180 (delta 78), pack-reused 0
Receiving objects: 100% (276/276), 87.53 KiB | 0 bytes/s, done.
Resolving deltas: 100% (172/172), done.
Checking connectivity... done.
</pre>

This will create a directory rift-fsm with the source code:

<pre>
$ <b>find rift-fsm</b>
rift-fsm
rift-fsm/config.py
rift-fsm/encoding.thrift
rift-fsm/utils.py
rift-fsm/cli_listen_handler.py
rift-fsm/.gitignore
rift-fsm/constants.py
...
</pre>

### Create Python virtual environment

Go into the newly create rift-fsm directory and create a new virtual environment named env:

<pre>
$ <b>cd rift-fsm</b>
$ <b>virtualenv env --python=python3</b>
Already using interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in /home/ubuntu/rift-fsm/env/bin/python3
Also creating executable in /home/ubuntu/rift-fsm/env/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
</pre>

### Activate the Python virtual environment

While still in the rift-fsm directory, activate the newly created Python environment:

<pre>
$ <b>source env/bin/activat</b>
(env) $ 
</pre>

### Use pip to install dependecies

Use pip to install the external following modules. It is important that you have activated
the virtual environment as described in the previous step before you install these dependencies.

Install the trift module which is used to encode and decode Thrift messages:

<pre>
(env) $ <b>pip install thrift</b>
</pre>

Install the sortedcontainers module which is used to created Python containers (e.g. dictionaries) that are sorted by key value:

<pre>
(env) $ <b>pip install sortedcontainers</b>
</pre>

Install the netifaces module which provides cross-platform portable code for retrieving information about interfaces and their addresses:

<pre>
(env) $ <b>pip install netifaces</b>
</pre>

Install the pyyaml module which is used to parse YAML files:

<pre>
(env) $ <b>pip install pyyaml</b>
</pre>

Install the cerberus module which is used to validate whether the data stored in a YAML file conforms to a data model (schema):

<pre>
(env) $ <b>pip install cerberus</b>
</pre>

## macOS (High Sierra 10.13)

TODO

## Windows

TODO

Note: also need a Telnet client.

# Running Instructions

## Starting RIFT

Go into the rift-fsm directory that was created when you cloned the git repository:

<pre>
$ <b>cd rift-fsm</b>
</pre>

Make sure the Python environment that you created during the installation is activated. This is needed to make sure you run the right version of Python 3 and that the right versions of all depencency modules can be found:

<pre>
$ <b>source env/bin/activate</b>
(env) $ 
</pre>

Start the RIFT protocol engine by running the python main script. 

<pre>
(env) $ <b>python main.py</b>
Command Line Interface (CLI) for Brunos-MacBook1 available on port 55018
</pre>

Note that you can simply type python instead of python3 because activing the environment automatically selected the right version of Python:

<pre>
(env) $ <b>which python</b>
/Users/brunorijsman/rift-fsm/env/bin/python
(env) $ <b>python --version</b>
Python 3.5.1
</pre>

After you start RIFT, there should be a single line of output reporting that the Command Line Interface (CLI) is available on a particular TCP port (in this example port 55018):

<pre>
Command Line Interface (CLI) for Brunos-MacBook1 available on port 55018
</pre>

The next section explains how to connect to the CLI and how to use to CLI.

## Command Line Interface (CLI)

### Connect to the CLI

You can connect to the Command Line Interface (CLI) using a Telnet client. Assuming you are connecting from the same device as where the RIFT engine is running, the hostname is localhost. The port should be the port number that RIFT reported when it was started:

<pre>
$ <b>telnet localhost 55018</b>
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Brunos-MacBook1> 
</pre>

You should get a prompt containing the name of the RIFT node. In this example the name of the RIFT node is "Brunos-MacBook1".

By default (i.e. if no configuration file is specified) a single instance of the RIFT protocol engine (a single so-called RIFT node) is started. And by default, the name of that single RIFT node is equal to the hostname of the computer on which the RIFT node is running.

### Entering CLI Commands

You can enter CLI commands at the CLI prompt. For example, try entering the <b>help</b> command:

<pre>
Brunos-MacBook1> <b>help</b>
show node 
show interfaces 
show interface &lt;interface-name&gt;
Brunos-MacBook1> 
</pre>

(You may see more commands in the help output if you are running a more recent version of the code.)

Unfortunately, the CLI does not yet support using cursor-up or cursor-down or ctrl-p or ctrl-n to go the the previous or next command in the command history. It does also not support tab command completion; all commands must be entered in full manually. And you can also not yet use ? for context-sensitive help. These features will be added in a future version.

### The <b>show node</b> command

The "<b>show node</b>" command reports the details for the RIFT node:

<pre>
Brunos-MacBook1> <b>show node</b>
+-------------------------------------+------------------+
| Name                                | Brunos-MacBook1  |
| Passive                             | False            |
| Running                             | True             |
| System ID                           | 667f3a2b1a721f01 |
| Configured Level                    | 0                |
| Multicast Loop                      | True             |
| Receive LIE IPv4 Multicast Address  | 224.0.0.120      |
| Transmit LIE IPv4 Multicast Address | 224.0.0.120      |
| Receive LIE IPv6 Multicast Address  | FF02::0078       |
| Transmit LIE IPv6 Multicast Address | FF02::0078       |
| Receive LIE Port                    | 10000            |
| Transmit LIE Port                   | 10000            |
| LIE Send Interval                   | 1.0 secs         |
| Receive TIE Port                    | 10001            |
+-------------------------------------+------------------+
</pre>


### The <b>show interfaces</b> command

The "<b>show interfaces</b>" command reports a summary of all interfaces configured on the RIFT node. Note that "interfaces" is plural with an s. It only reports the interfaces on which RIFT is running; your device may have additional interfaces on which RIFT is not running.

<pre>
Brunos-MacBook1> <b>show interfaces</b>
+-----------+----------+-----------+----------+
| Interface | Neighbor | Neighbor  | Neighbor |
| Name      | Name     | System ID | State    |
+-----------+----------+-----------+----------+
| en0       |          |           | ONE_WAY  |
+-----------+----------+-----------+----------+
</pre>

In the above example, RIFT is running on interface en0 but there is no RIFT neighbor on that interface. The example below does have a RIFT neighbor and the adjacency to that neighbor is in state THREE_WAY:

<pre>
Brunos-MacBook1> <b>show interfaces</b>
+-----------+---------------------+------------------+-----------+
| Interface | Neighbor            | Neighbor         | Neighbor  |
| Name      | Name                | System ID        | State     |
+-----------+---------------------+------------------+-----------+
| en0       | Brunos-MacBook1-en0 | 667f3a2b1a737c01 | THREE_WAY |
+-----------+---------------------+------------------+-----------+
</pre>

### The <b>show interface</b><i>interface-name</i> command

The "<b>show interface</b><i>interface-name</i>" command reports more detailed information about a single interface. Note that "interface" is singular without an s.

Here is an example of the output when there is no neighbor (note that the state of the interface is ONE_WAY):

<pre>
Brunos-MacBook1> <b>show interface en0</b>
Interface:
+-------------------------------------+---------------------+
| Interface Name                      | en0                 |
| Advertised Name                     | Brunos-MacBook1-en0 |
| Interface IPv4 Address              | 192.168.2.163       |
| Metric                              | 100                 |
| Receive LIE IPv4 Multicast Address  | 224.0.0.120         |
| Transmit LIE IPv4 Multicast Address | 224.0.0.120         |
| Receive LIE IPv6 Multicast Address  | FF02::0078          |
| Transmit LIE IPv6 Multicast Address | FF02::0078          |
| Receive LIE Port                    | 10000               |
| Transmit LIE Port                   | 10000               |
| Receive TIE Port                    | 10001               |
| System ID                           | 667f3a2b1a721f01    |
| Local ID                            | 1                   |
| MTU                                 | 1500                |
| POD                                 | 0                   |
| State                               | ONE_WAY             |
| Neighbor                            | No                  |
+-------------------------------------+---------------------+
</pre>

Here is an example of the output when there is a neighbor (note that the state of the interface is THREE_WAY):

<pre>
Brunos-MacBook1> <b>show interface en0</b>
Interface:
+-------------------------------------+---------------------+
| Interface Name                      | en0                 |
| Advertised Name                     | Brunos-MacBook1-en0 |
| Interface IPv4 Address              | 192.168.2.163       |
| Metric                              | 100                 |
| Receive LIE IPv4 Multicast Address  | 224.0.0.120         |
| Transmit LIE IPv4 Multicast Address | 224.0.0.120         |
| Receive LIE IPv6 Multicast Address  | FF02::0078          |
| Transmit LIE IPv6 Multicast Address | FF02::0078          |
| Receive LIE Port                    | 10000               |
| Transmit LIE Port                   | 10000               |
| Receive TIE Port                    | 10001               |
| System ID                           | 667f3a2b1a721f01    |
| Local ID                            | 1                   |
| MTU                                 | 1500                |
| POD                                 | 0                   |
| State                               | THREE_WAY           |
| Neighbor                            | Yes                 |
+-------------------------------------+---------------------+

Neighbor:
+----------------------------------+---------------------+
| Name                             | Brunos-MacBook1-en0 |
| System ID                        | 667f3a2b1a73cb01    |
| IPv4 Address                     | 192.168.2.163       |
| LIE UDP Source Port              | 55048               |
| Link ID                          | 1                   |
| Level                            | 0                   |
| Flood UDP Port                   | 10001               |
| MTU                              | 1500                |
| POD                              | 0                   |
| Hold Time                        | 3                   |
| Not a ZTP Offer                  | False               |
| You Are Not a ZTP Flood Repeater | False               |
| Your System ID                   | 667f3a2b1a721f01    |
| Your Local ID                    | 1                   |
+----------------------------------+---------------------+
</pre>

## Logging

The RIFT protocol engine write very detailed logging information to the file rift.log in the same directory as where the RIFT engine was started.

You can monitor the log file by running "tail -f":

<pre>
$ <b>tail -f rift.log</b>
2018-07-15 07:47:07,064:INFO:node.if.tx:[667f3a2b1a73cb01-en0] Send LIE ProtocolPacket(header=PacketHeader(level=0, major_version=11, sender=7385685870712703745, minor_version=0), content=PacketContent(tie=None, lie=LIEPacket(holdtime=3, neighbor=Neighbor(remote_id=1, originator=7385685870712594177), not_a_ztp_offer=False, flood_port=10001, name='Brunos-MacBook1-en0', you_are_not_flood_repeater=False, link_mtu_size=1500, local_id=1, pod=0, nonce=6638665728137929476, label=None, capabilities=NodeCapabilities(flood_reduction=True, leaf_indications=1)), tide=None, tire=None))
2018-07-15 07:47:07,065:INFO:node.if.rx:[667f3a2b1a721f01-en0] Receive ProtocolPacket(header=PacketHeader(minor_version=0, major_version=11, level=0, sender=7385685870712703745), content=PacketContent(tide=None, tire=None, tie=None, lie=LIEPacket(local_id=1, name='Brunos-MacBook1-en0', you_are_not_flood_repeater=False, pod=0, capabilities=NodeCapabilities(flood_reduction=True, leaf_indications=1), label=None, flood_port=10001, nonce=6638665728137929476, link_mtu_size=1500, not_a_ztp_offer=False, holdtime=3, neighbor=Neighbor(originator=7385685870712594177, remote_id=1))))
2018-07-15 07:47:07,065:INFO:node.if.rx:[667f3a2b1a73cb01-en0] Receive ProtocolPacket(header=PacketHeader(level=0, major_version=11, sender=7385685870712703745, minor_version=0), content=PacketContent(tie=None, lie=LIEPacket(holdtime=3, neighbor=Neighbor(remote_id=1, originator=7385685870712594177), not_a_ztp_offer=False, flood_port=10001, name='Brunos-MacBook1-en0', you_are_not_flood_repeater=False, link_mtu_size=1500, local_id=1, pod=0, nonce=6638665728137929476, label=None, capabilities=NodeCapabilities(flood_reduction=True, leaf_indications=1)), tide=None, tire=None))
2018-07-15 07:47:07,065:INFO:node.if.fsm:[667f3a2b1a721f01-en0] FSM push event, event=LIE_RECEIVED
2018-07-15 07:47:07,065:INFO:node.if:[667f3a2b1a73cb01-en0] Ignore looped back LIE packet
2018-07-15 07:47:07,065:INFO:node.if.fsm:[667f3a2b1a721f01-en0] FSM process event, state=THREE_WAY event=LIE_RECEIVED event_data=(ProtocolPacket(header=PacketHeader(minor_version=0, major_version=11, level=0, sender=7385685870712703745), content=PacketContent(tide=None, tire=None, tie=None, lie=LIEPacket(local_id=1, name='Brunos-MacBook1-en0', you_are_not_flood_repeater=False, pod=0, capabilities=NodeCapabilities(flood_reduction=True, leaf_indications=1), label=None, flood_port=10001, nonce=6638665728137929476, link_mtu_size=1500, not_a_ztp_offer=False, holdtime=3, neighbor=Neighbor(originator=7385685870712594177, remote_id=1)))), ('192.168.2.163', 55048))
2018-07-15 07:47:07,065:INFO:node.if.fsm:[667f3a2b1a721f01-en0] FSM invoke state-transition action, action=process_lie
2018-07-15 07:47:07,065:INFO:node.if.fsm:[667f3a2b1a721f01-en0] FSM push event, event=UPDATE_ZTP_OFFER
2018-07-15 07:47:07,065:INFO:node.if.fsm:[667f3a2b1a721f01-en0] FSM process event, state=THREE_WAY event=UPDATE_ZTP_OFFER
...
</pre>

The format of the log messages is designed to make it easy to "grep" for particular subsets of information that you might be interested in.

TODO: Provide grep patterns

## Configuration Script

TODO

## Command-Line Options

TODO
