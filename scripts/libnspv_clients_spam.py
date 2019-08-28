import time
import subprocess
import requests

"""
   Libnspv has no analog to komodod's -connect= parameter
   You are supposed to run this script after modifying coins file
   and add a 0 && to the if statement on line 389 in netspv.c.
   Obviously, recompile nspv executable with this changes.
"""

# init params
nspv_clients_to_start = 100
ac_name = 'ILN'
node = '192.168.0.106'
userpass = 'uerpass'


# getinfo method execution
def nspv_getpeerinfo(node_ip, user_pass):
    params = {'userpass': user_pass,
              'method': 'getpeerinfo'}
    r = requests.post(node_ip, json=params)
    return r.content


def main():
    # start numnodes libnspv daemons, changing port
    for i in range(nspv_clients_to_start):
        subprocess.call(['./nspv', ac_name, '-p', str(7000 + i)])

    time.sleep(2)

    while True:
        for i in range(nspv_clients_to_start):
            nodeip = node + str(7000 + i)
            try:
                nspv_getinfo_output = nspv_getpeerinfo(nodeip, userpass)
                print(nspv_getinfo_output)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
