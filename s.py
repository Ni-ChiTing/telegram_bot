import subprocess
import requests
import json
import time

if __name__ == '__main__':
    p=subprocess.Popen(r'ngrok.exe http -bind-tls=true 5000')
    time.sleep(3) # to allow the ngrok to fetch the url from the server
    localhost_url = "http://localhost:4044/api/tunnels" #Url with tunnel details
    tunnel_url = requests.get(localhost_url).text #Get the tunnel information
    j = json.loads(tunnel_url)
    print(j['tunnels'][0]['public_url'])
