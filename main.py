from requests import get, post
from time import sleep
from time import time
from datetime import datetime

class Stuff:
    cookie = '' # _|WARNING-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someon......
    groupid = '' # https://www.roblox.com/groups/126633211/Group-Name/about -> 126633211
    webhook = '' # https://hookdeck.com/webhooks/platforms/how-to-get-started-with-discord-webhooks
    timeout = 10 # Default 120
    wait = 5 # Default 10
    pastids = [] # KEEP THIS HERE, DO NOT CHANGE IT

def profilePicture(id):
    r2 = get(f'https://www.roblox.com/users/{id}/profile').text
    return r2.split('<meta property="og:image" content="')[1].split('"')[0]

def log(text):
    print(f"[{datetime.utcfromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')}] → {text}")

r = get(f'https://economy.roblox.com/v1/groups/{Stuff.groupid}/revenue/summary/day', cookies={'.ROBLOSECURITY': Stuff.cookie})
pastpending = r.json()['pendingRobux']

response = get(f'https://economy.roblox.com/v2/groups/{Stuff.groupid}/transactions?cursor=&limit=10&transactionType=Sale', cookies={'.ROBLOSECURITY': Stuff.cookie})
for purchase in response.json()['data']:
    Stuff.pastids.append(purchase['idHash'])

log(f"Loaded with {len(Stuff.pastids)} past hashes.")

try:
    post(Stuff.webhook,json={"content":None,"embeds":[{"description":"🔄 **The [Group Sale Notifier](https://github.com/DankoOfficial/Roblox-Group-Sale-Notifier) has loaded and is now ready to track sales. Enjoy!!!!!!!**","color":0,"author":{"name":"🚀 Program Loaded","icon_url":"https://avatars.githubusercontent.com/u/99405955?v=4"},"footer":{"text":"Status: ONLINE","icon_url":"https://icones.pro/wp-content/uploads/2022/06/icone-du-bouton-en-ligne-vert.png"},"thumbnail":{"url":"https://cdn-icons-png.flaticon.com/512/5537/5537993.png"}}],"attachments":[]})
except:
    log('Failed to send notification')

while True:
    try:
        r = get(f'https://economy.roblox.com/v1/groups/{Stuff.groupid}/revenue/summary/day', cookies={'.ROBLOSECURITY': Stuff.cookie})
        nowpending = r.json()['pendingRobux']
        if nowpending>pastpending:
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
                    thetype = purchase['details']['type']
                    if thetype == 'GamePass':
                        display = 'a Game Pass'
                        moreinformation = f"**Sold [{purchase['details']['name']}](https://www.roblox.com/game-pass/{purchase['details']['id']}) in [{purchase['details']['place']['name']}](https://www.roblox.com/games/{purchase['details']['place']['placeId']})**"
                    elif thetype == 'PrivateServer':
                        display = 'a Private Server'
                        moreinformation = f"**Sold Private Server in [{purchase['details']['place']['name']}](https://www.roblox.com/games/{purchase['details']['place']['placeId']})**"
                    elif thetype == 'DeveloperProduct':
                        display = 'a Developer Product'
                        moreinformation = f"**Sold {purchase['details']['name']} in [{purchase['details']['place']['name']}](https://www.roblox.com/games/{purchase['details']['place']['placeId']})**"
                    elif thetype == 'Asset':
                        display = 'an Asset'
                        moreinformation = f"**Sold {purchase['details']['name']}**"
                    else:
                        display = 'Unknown'
                        moreinformation = 'This seems to be an unknown purchase type, please report it to https://discord.gg/zzcYQnXJaN'
                    post(Stuff.webhook,json={"content": None,"embeds": [{"title": ":shopping_cart:  Purchase Confirmation","description": f"[{purchase['agent']['name']}](https://www.roblox.com/users/{purchase['agent']['id']}/profile) spent **{purchase['currency']['amount']} ⏣ **  on `{display}`\n\n{moreinformation}",  "color": 0,  "author": {"name": "💸 New Sale","icon_url": "https://avatars.githubusercontent.com/u/99405955?v=4"  },  "thumbnail": {"url": pfp  },  "footer": {"text": "Download the Group Sale Notifier: https://github.com/DankoOfficial/Roblox-Group-Sale-Notifier","icon_url": "https://avatars.githubusercontent.com/u/99405955?v=4"  }}],"attachments": []})
        sleep(int(Stuff.wait))
    except Exception as e:
        log(f'[ERROR] {e}')
        sleep(Stuff.timeout)
