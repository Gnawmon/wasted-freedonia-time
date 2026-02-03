import requests
import math


def doesPlayerExist(username):
    firstSeen = requests.get("https://minecraftonline.com/cgi-bin/getfirstseen_unix?"+username).text
    if firstSeen == "INVALID" or firstSeen == "NOTFOUND\n":
        return False
    return True

def getPlaytime(username):
    return int(requests.get("https://minecraftonline.com/cgi-bin/gettimeonline?" + username).text)

def formatTime(playtime):
    return str(math.trunc(playtime)) 
    pass

# amazing code i know
def shame(rawPlaytime):
 
     
    
    
    
    

    shameText = ""
    if rawPlaytime > 1620:
        shameText += "baked " + formatTime(rawPlaytime/1620) + " cookies.\n"
        if rawPlaytime > 5400:
            shameText += "watched Shrek " + formatTime(rawPlaytime/5400) + " times.\n"
            if rawPlaytime > 51180:
                shameText += "read Moby Dick " + formatTime(rawPlaytime/51180) + " times.\n"
                if rawPlaytime > 698400:
                    shameText += "fully completed Red Dead Redemption 2 " + formatTime(rawPlaytime/698400) + " times.\n"
                    if rawPlaytime > 2160000:
                         shameText += "learned spanish.\n"
    shameText += "also this time equals to\n"
    shameText += str(rawPlaytime * 0.0000001) + " meters of beard seconds.\n" #probably wrong but who cares
    shameText += formatTime(rawPlaytime * 0.0000005) + " CPU cycles of Intel 8080\n"
    shameText += format("% s years \n% s months \n% s days \n% s hours \n% s minutes \n% s seconds\n" % (rawPlaytime/31536000 ,rawPlaytime/2592000,rawPlaytime/86400,rawPlaytime/3600,rawPlaytime/60,rawPlaytime))


    return shameText

