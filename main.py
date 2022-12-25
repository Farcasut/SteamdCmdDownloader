
import string
import subprocess
import re
import requests
path:string = "./steamcmd.exe"
removeExcess= r'\d'
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
    modID=0;
    match = re.search(removeExcess, link[::-1])
    if match:
        modID=link[link.find('?id=')+4:len(link)-match.start()]
    else:
        modID=link[link.find('?id=')+4:]

    return [linkHomePage[linkHomePage.find("/app/")+5:], re.search(regexGameName, htmlSteam.text)[0][37:-6], modID]

def process_link():
    print("quit->quit\nchange game ->change\n")
    while True:
        linkWorkShop = input("Link of the mod:\n")
        if linkWorkShop.upper()=="QUIT":
            return;

        [gameID,gameName,modID]= getGameData(linkWorkShop)
        startSubprocess(gameID, modID,gameName)
    return;
def process_file(fileName):
    with open(fileName, 'r') as file:
        for i in file.readlines():
           [gameID, gameName,modID] = getGameData(i)
           print(gameID,gameName,modID)
           startSubprocess(gameID,modID, gameName)
def main():
    mode =  input("Do you want do download from a file or from a link?\nFile/Link\n").upper();
    if mode=="LINK":
        process_link()
    if mode=="FILE":
        fileName =  input("File name:\n")
        process_file(fileName)


if __name__ == '__main__':
   main()