
import string
import subprocess
path:string = "./steamcmd.exe"




def startSubprocess(gameID, modID, gameName):
    steamcmd_params = (
        path,
        '+force_install_dir {}'.format(gameName),
        '+login {} {}'.format("anonymous", None),
        '+workshop_download_item {} {}'.format(gameID, modID),
        '{}'.format(None),
        '+quit',
    )
    subprocess.check_call(steamcmd_params)
    print("\n\n")


def process_link(gameID,gameName):
    print("quit->quit\nchange game ->change\n")
    while True:
        linkWorkShop = input("Link of the mod:\n")
        if linkWorkShop.upper()=="QUIT":
           return
        if linkWorkShop.upper() == "CHANGE":
            break;
        modID = linkWorkShop[linkWorkShop.find("?id=")+4:]
        startSubprocess(gameID, modID, gameName)
    initialize()
    return;



def initialize():
    gameList = {}
    with open("gamesID.txt") as ID:
        for line in ID:
            (name, id) = line.split()
            gameList[name.upper()] = id

    try:
        gameName = input("GAME NAME:\n").upper();
        process_link(gameList[gameName], gameName)
    except KeyError:
        print("\n\nThe game isn't present in the gamesID file.\n\n");
        userDecision = input("\nDo you want to add the game? yes/no\n");
        if userDecision.upper() == "YES":
            gameName = input("The name of the game or an alias\n").upper();
            gameID = input(
                "Game ID. You can find the game on the home workshop of the game. Eg: https://steamcommunity.com/app/GAME_ID/workshop/\n")
            with open("gamesID.txt", 'a') as ID:
                ID.write('\n' + gameName + " " + gameID)
            process_link(gameID, gameName)

def main():
    initialize()

if __name__ == '__main__':
   main()

