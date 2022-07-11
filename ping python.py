
import json
import requests


mainUrl = "https://api.meraki.com/api/v1"

orgId = "635570497412663072"
API_KEY = "f81ba343ed0a33c5f61b5153776412eb0114886e"

netIdUrl = mainUrl + "/organizations/{}/networks?perPage=100000".format(orgId)

payload = {}

headers = {
    'Content-Type': 'application/json',
    'X-Cisco-Meraki-API-Key': API_KEY

}


responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)
nomes = "MCD_ASH_REST"

tags = "Kiosk","ksk"


#import subprocess
#import os
#import time
#ips = ['200.189.220.241']
#servidor arcos dc 200.189.220.241
#while True:
    #with open(os.devnull, "wb") as limbo:
        #for ip in ips:

            #result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                    #stdout=limbo, stderr=limbo).wait()
            #if result:
                    #print(nomes, ", não está UP")
            #else:
                    #print(nomes, ", está Up")

    #time.sleep()
    #print(' -- recomeçar --')

from pythonping import ping

def ping_host(host):
    ping_result = ping(target=host, count=100, timeout=2)

    return {
        'nome': nomes,
        'host': host,
        'avg_latency': ping_result.rtt_avg_ms,
        'min_latency': ping_result.rtt_min_ms,
        'max_latency': ping_result.rtt_max_ms,
        'packet_loss': ping_result.packet_loss
    }

hosts = ["8.8.8.8"]
for host in hosts:
    print(ping_host(host))