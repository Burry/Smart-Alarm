import json
import sys
import getopt
from os import system

sys.path.insert(0, '/requests')
import requests


def getBridgeIP():
    r = requests.get('http://www.meethue.com/api/nupnp')
    bridges = r.json()

    if not bridges:
        bridge_ip = 0
    else:
        bridge_ip = bridges[0]['internalipaddress']

    return bridge_ip


def createUser(bridge_ip):
    r = requests.post(
        'http://{bridge_ip}/api'.format(bridge_ip=bridge_ip),
        data=json.dumps({'devicetype': 'Smart Alarm'}))

    resp = r.json()[0]

    if resp.get('error'):
        username = 'Setup Error: %s' % resp['error'].get('description')
    else:
        username = resp['success']['username']

        return username


def main(argv):
    try:
        bridge_ip = sys.argv[1]
        return_value = createUser(bridge_ip)
    except:
        return_value = "Error: Please provide an IP address"

    print return_value
    return return_value


if __name__ == "__main__":
    main(sys.argv[1:])
