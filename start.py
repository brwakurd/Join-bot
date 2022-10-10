from xs import FakeXSRF

import requests
import json
import psutil
import time
import subprocess
xst = FakeXSRF()
token = xst
auth = ''
mulePID = "Nothing"

def join():
    global mulePID
    global token
    global auth
    try:
        #roblox = subprocess.Popen([r"C:\Users\admin\AppData\Local\Roblox\Versions\version-aa66315930d14906\RobloxPlayerLauncher", "roblox-player:1+launchmode:play+gameinfo:{}+launchtime:1586893015226+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D46154891730%26placeId%3D735030788%26isPlayTogetherGame%3Dfalse+browsertrackerid:46154891730+robloxLocale:en_us+gameLocale:en_us".format(auth)])
        roblox = subprocess.Popen([r"C:\Users\Belen\AppData\Local\Roblox\Versions\version-0beb053becad47aa\RobloxPlayerLauncher.exe", "roblox-player:1+launchmode:play+gameinfo:{}+launchtime:1602865431847+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestPrivateGame%26browserTrackerId%3D65167079117%26placeId%3D920587237%26accessCode%3Dc97b9d79-4c2a-429b-a2ec-248cd0f47891%26linkCode%3D2d88T9V1W33pyNYaf7fbFy05R59H_yWJ+browsertrackerid:65167079117+robloxLocale:en_us+gameLocale:en_us+channel:".format(auth)])
        print('Joined Game')
        time.sleep(25)
        for process in psutil.process_iter():
            try:
                processName = process.name()
            #print(processName)
                if processName == 'RobloxPlayerBeta.exe':
                    if mulePID == "Noothing":
                        #process.kill()

                        #mulePID = 321
                        # f = input()
                        #print("New mulePID {}".format(mulePID))
                        return
                    elif process.pid!=mulePID:
                        process.kill()
                        print("Killed")
                        
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                print("Hmm")
        
    except Exception as e:
        print(e)
        return


def getauth(cookie):
    global token
    global auth
    try:
        r = requests.post('https://auth.roblox.com/v1/authentication-ticket/',headers={
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; MXQ-Pro-NEXBOX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 YaBrowser/19.4.4.317.01 Safari/537.36',
            'X-CSRF-TOKEN':token,
            'Cookie': '.ROBLOSECURITY={}'.format(cookie),
            'Referer':'https://www.roblox.com/games/920587237/Adopt-Me'
        })
        
        print(r.status_code)
        print(r.text)
        if 'Token' in r.text:
            token = r.headers['X-CSRF-TOKEN']
            getauth(cookie)
        if '{}' in r.text:
            autht = r.headers['rbx-authentication-ticket']
            auth = autht
            join()
        
    except Exception as e:
        return
        
acc = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_BB29DB6CA512FA5CB28226D844D5211785697670ACB071C1F3DA4881B3335C8FF1876AAB25D3A44E8A4D1F2A078954AC5A5BEE1517B50FA7CBF78C40168DA235CD39A30E754D9156DAFDB0AA5303F338FEB0875EA4374ABEE5D1F8C18CF60450699D57676E207390CA86D7D1DB4FA1399E88CEE5A27D421B7A37E87A887C986920EBA53003CB78C94A1E6B7EE5238C05765EB8FADD01071951684CAA47622AF20410D42272074CBDF594F300BBBBEE2A1719F4E5B5A3B83C72B78A2F990D3B824CACA07B9CE641F0BDF21EE292742F6EC113477278D5C4383B93593BB2A8F2DB46BF31A0D5A7F9281981CAE3F56199F1DF3F97CEF8C2E31DF761092D31A958A97CECC0C9B0EC215F23DF7BCA66F582837884BD2AB98145F9A88F41E80D8F88F7C0181F9D"
for i in range(30):
    print(f"Starting line {str(i)}")
    getauth(acc)
    time.sleep(5)