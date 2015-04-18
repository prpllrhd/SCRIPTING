#!/home/y/bin/python2.7
example:subprocess

import subprocess as sub
import os, sys

def get_subnet(ip):
    args = [ '/home/y/bin/get_network', ip ]
    response = sub.Popen(args, stdout=sub.PIPE)
    s_line = response.stdout.readlines()
    try:
        network_id = s_line[0].split()[1]
        mask = s_line[0].split()[2].strip("/")
        print mask
        print network_id
    except IndexError:
        network_id = 'none'
        mask = 'none'

    #return network_id + "/" + mask
if __name__ == '__main__':
    get_subnet('10.194.128.128/26')
