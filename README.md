# georepsetup - Gluster Geo-replication Setup Tool

A tool to help the Gluster Geo-replication session creation. Very easy to install this tool.

    git clone https://github.com/aravindavk/georepsetup.git
    cd georepsetup
    sudo python setup.py install

Thats it!

## Usage

To use run this tool with Master Volume name, Slave host and Slave Volume information. Run `georepsetup -h` or `georepsetup --help` for Help information.

Output of `help` command

    usage: georepsetup [-h] [--force] [--no-color] MASTERVOL SLAVE SLAVEVOL
     
    CLI tool to setup Gluster Geo-replication Session between
    Master Gluster Volume to Slave Gluster Volume.
     
    positional arguments:
      MASTERVOL   Master Volume Name
      SLAVE       Slave, HOSTNAME or root@HOSTNAME or user@HOSTNAME
      SLAVEVOL    Slave Volume Name
     
    optional arguments:
      -h, --help  show this help message and exit
      --force     Force
      --no-color  No Terminal Colors


Example,

    sudo georepsetup gv1 fvm1 gv2

Where, gv1 is Master Volume, fvm1 is Slave Host and gv2 is Slave Volume.

## Screenshot

![georepsetup in Action](https://github.com/aravindavk/georepsetup/blob/master/georepsetup.png)


## Setting up Geo-replication with Root user in Slave

1. Create Master and Slave Gluster Volumes

2. Run `georepsetup` command and provide root password for the Slave host

        georepsetup gv1 fvm1 gv2

## Setting up Geo-replication with Non-privilaged user in Slave

For non root Geo-replication, still some manual work. Will plan to simplify some steps in future.

1. Create a new user group in all the Slave nodes. For example, geogroup.

2. Create a unprivileged account in all the Slave nodes. For example,  geoaccount. Add geoaccount as a member of geogroup group.

3. As a root, create a new directory with permissions `0711`. Ensure that the location where this directory is created is writeable only by root but geoaccount is able to access it. For example, create a mountbroker-root directory at `/var/mountbroker-root`.

4.  Run the following commands in any one of the Slave node:

        gluster system:: execute mountbroker opt mountbroker-root /var/mountbroker-root
        gluster system:: execute mountbroker user geoaccount slavevol
        gluster system:: execute mountbroker opt geo-replication-log-group geogroup
        gluster system:: execute mountbroker opt rpc-auth-allow-insecure on

5. Restart Glusterd on all Slave nodes

6. Run `georepsetup` command and provide root password for the Slave host

        georepsetup gv1 geoaccount@fvm1 gv2


## Blogs

1. http://aravindavk.in/blogs/introducing-georepsetup
