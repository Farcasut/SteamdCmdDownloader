
import string
import subprocess
import re
import requests
path:string = "./steamcmd.exe"

def startSubprocess(gameID, modID, gameName):
    steamcmd_params = (
        path,
        '+force_install_dir {}'.format("./Downloads/"+gameName),
        '+login {} {}'.format("anonymous", None),
        '+workshop_download_item {} {}'.format(gameID, modID),
        '{}'.format(None),
        '+quit',
    )
    subprocess.check_call(steamcmd_params)
    print("\n\n")


def getGameData(link):
    htmlSteam =  requests.get(link)
    regexGameID = "(https:\/\/steamcommunity\.com\/app\/[0-9]+) ?"
    regexGameName="<div class=\"apphub_AppName ellipsis\">.*<.div>"

    linkHomePage = re.search(regexGameID, htmlSteam.text)[0]
    return [linkHomePage[linkHomePage.find("/app/")+5:], re.search(regexGameName, htmlSteam.text)[0][37:-6]]

def process_link():
    print("quit->quit\nchange game ->change\n")
    while True:
        linkWorkShop = input("Link of the mod:\n")
        if linkWorkShop.upper()=="QUIT":
            return;

        [gameID,gameName]= getGameData(linkWorkShop)
        modID = linkWorkShop[linkWorkShop.find("?id=")+4:]
        startSubprocess(gameID, modID,gameName)
    return;

def main():
    process_link()


if __name__ == '__main__':
   main()

