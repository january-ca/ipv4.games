import httpx, threading, random, sys, colr, os

class count:
    claimed = 0

def title():
    while True:
        os.system(f'title Claimed: {count.claimed}')

def claim(proxy):
    while True:
        try:
            client = httpx.Client(proxies=proxy)
            client.proxies = proxy
            req = client.get('https://ipv4.games/claim?name=discord.gg/arkoselabs', headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
            
            if '<a href=/>Back to homepage</a>' in req.text:
                ip = req.text.split('The land at ')[1].split(' was')[0]
                sys.stdout.write(colr.color(f'[+] Claimed land for IP: {ip} \n'))
                sys.stdout.flush()
                count.claimed+=1
        except Exception as e:
            pass

threading.Thread(target=title).start()
proxy = input('Proxy: ')
for _ in range(250):
    threading.Thread(target=claim, args=[proxy]).start()
