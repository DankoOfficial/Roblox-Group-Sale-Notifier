from requests import get, post
from time import sleep
from time import time
from datetime import datetime

class Stuff:
    cookie = 'YOUR ROBLOX COOKIE HERE' # _|WARNING-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someon......
    groupid = 'YOUR GROUP ID HERE' # https://www.roblox.com/groups/126633211/Group-Name/about -> 126633211
    webhook = 'YOUR DISCORD WEBHOOK HERE' # https://hookdeck.com/webhooks/platforms/how-to-get-started-with-discord-webhooks
    timeout = 'TIMEOUT TIME HERE, WHEN ERRORS HAPPEN, IT WILL TIMEOUT WITH X SECONDS, HAS TO BE A NUMBER, NOT DECIMAL' # Default 120
    wait = 'TIME TO WAIT TO CHECK FOR NEW PURCHASES' # Default 10
    pastids = [] # KEEP THIS HERE, DO NOT CHANGE IT

def profilePicture(id):
    r2 = get(f'https://www.roblox.com/users/{id}/profile').text
    return r2.split('<meta property="og:image" content="')[1].split('"')[0]

def log(text):
    print(f"[{datetime.utcfromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')}] → {text}")

r = get(f'https://economy.roblox.com/v1/groups/{Stuff.groupid}/revenue/summary/day', cookies={'.ROBLOSECURITY': Stuff.cookie})
pastpending = r.json()['pendingRobux']

response = get('https://economy.roblox.com/v2/groups/{Stuff.groupid}/transactions?cursor=&limit=10&transactionType=Sale', cookies={'.ROBLOSECURITY': Stuff.cookie})
for purchase in response.json()['data']:
    Stuff.pastids.append(purchase['idHash'])

log(f"Loaded with {len(Stuff.pastids)} past hashes.")

while True:
    try:
        r = get(f'https://economy.roblox.com/v1/groups/{Stuff.groupid}/revenue/summary/day', cookies={'.ROBLOSECURITY': Stuff.cookie})
        nowpending = r.json()['pendingRobux']
        if pastpending<nowpending:
            response = get(f'https://economy.roblox.com/v2/groups/{Stuff.groupid}/transactions?cursor=&limit=10&transactionType=Sale', cookies={'.ROBLOSECURITY': Stuff.cookie})
            for purchase in response.json()['data']:
                if purchase['idHash'] not in Stuff.pastids:
                    pastpending = nowpending
                    log(f"[+] New Purchase - Username: {purchase['agent']['name']} - Their ID: {purchase['agent']['id']} - Robux Earned: {purchase['currency']['amount']} - Product Name: {purchase['details']['name']} - Product ID: {purchase['details']['id']}")
                    Stuff.pastids.append(purchase['idHash'])
                    try:
                        pfp = profilePicture(purchase['agent']['id'])
                    except:
                        pfp = 'https://tr.rbxcdn.com/af0be829bc4349c0b116ae36843a0a91/150/150/AvatarHeadshot/Png'
                    post(Stuff.webhook,json={"content":None,"embeds":[{"title":"💸 New Sale","description":f"💎 **Buyer information:**\n\nㅤ▫️ㅤ:detective: **Buyer:** `{purchase['agent']['name']}`\nㅤ▫️ㅤ:bulb: **ID:** `{purchase['agent']['id']}`\nㅤ▫️ㅤ:moneybag: **Robux Made:** `{purchase['currency']['amount']}`\n\n👜 **Clothing Information:**\n\nㅤ▫️ㅤ:crossed_swords: **Name:** `{str(purchase['details']['name']).rstrip()}`\nㅤ▫️ㅤ🫧 **ID:** `{purchase['details']['id']}`\nㅤ▫️ㅤ:link: **Link:** https://www.roblox.com/catalog/{purchase['details']['id']}\n\n:office: **Group Stats:**ㅤ▫️ㅤ⏣ **Pending:** `{nowpending}`","color":000000,"thumbnail":{"url":pfp}}],"username":purchase['agent']['name'],"avatar_url":pfp,"attachments":[]})
        sleep(int(Stuff.wait))
    except:
        log("Program bugged. Sleeping for 2m")
        sleep(int(Stuff.timeout))