# This is my automation code for downloading internet games from lichess.org and chess.com using
# the website openingtree.com
# First import the needed modules
# os is for working with files, selenium for automation things and time for pausing the process when needed
# (and for testing)
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Make a list of the players from Lichess.org you want to download their games from. i is set to 0,
# because we're going to iterate through that list
# Lichess will be in Dutch, Chess.com will be in English
# These are players I found  on Lichess for the next match

# List of players at Lichess that BSG will face next:
spelers = ["tjarkvos", "IlSalvatore", "Woodtree", "senior73", "GijsBon"]
i = 0

# The same is done for the account names at Chess.com. Here I use k to loop through the elements
# These are the players I found on Chess.com for the next match

# List of players from chess.com that we will face next time
players = ["DudeDoel", "tjarkvos", "kingloek"]
k = 0



# Start automation, first load the Chrome Webdriver
# Then get the website openingtree.com
# And then, very important, a couple of seconds of sleep. This prevents the program from crashing if the page
# doesn't load quick enough.
web = webdriver.Chrome()
web.get('https://www.openingtree.com/')
time.sleep(3)

# Then it's time to loop through the list. As long as i is smaller than the number of elements in the list, it executes
# the code.
# it begins with selecting Lichess by finding the web element
# then it clicks on that. It can also be done in 1 line of code.
while i < len(spelers):
    # These are the things necessary for making it work. First copy your standard download folder here.
    # Notice that if you use Windows, you should change '\' in '/' to make it work.
    # Because it downloads files, I want to see if they exist, so I must make a file name that consists of 2 parts
    # 1) is the account name, which is dynamic, it takes the element 'i' from the lichess list.
    # 2) then it adds +white.pgn or +black.pgn
    # And then it combines both the path and the file name, separated by a '/' using string formatting.
    # Example, if a player's lichess account is 'unBEARableBEAR, the files will become
    # unBEARableBEAR-white.pgn and unBEARableBEAR-black.pgn within the download path.
    # First I had these next 5 lines of codes before the while loop, but then after the first element was done,
    # the program failed. Now it works with this inside the while loop.
    LichessPath = "C:/Users/ewoud/Downloads/"
    BestandWit = (spelers[i] + '-white.pgn')
    BestandZwart = (spelers[i] + '-black.pgn')
    PathWit = f'{LichessPath}/{BestandWit}'
    PathZwart = f'{LichessPath}/{BestandZwart}'


    Lichess = web.find_element(By.CLASS_NAME, 'sourceName')
    Lichess.click()
    time.sleep(2)

    # then you need to fill in a name
    # first it finds the right element
    # then it takes element [i] from the list 'spelers'.
    # In python, if i = 0, it returns the first element of a list
    # After done that, 2 seconds rest
    Naam = web.find_element(By.XPATH, '//*[@id="playerNameTextBox"]')
    Naam.send_keys(spelers[i])
    time.sleep(2)

    #After that, it must find the continue button and click it
    ContinueKnop = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div[2]/button/span[1]')
    ContinueKnop.click()
    time.sleep(2)

    # And after that, it must declare that it begins with the white games and click it
    SpeeltMetWit = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[1]/fieldset/div/label[1]/span[2]')
    SpeeltMetWit.click()
    time.sleep(2)

    # After that the advanced settings must be clicked, because I want to change something.
    Filters = web.find_element(By.XPATH,  '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[2]/span')
    Filters.click()
    time.sleep(2)

    # I want to exclude some playing rates, so the program needs to find it and click it
    Speeltempo = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/span/span')
    Speeltempo.click()
    time.sleep(2)

    # Exclude bullet by clicking on it
    Bullet = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/label/span[2]')
    Bullet.click()
    time.sleep(2)

    # Same goes for retarded UltraBullet. Find it and click it
    UltraBullet = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/label/span[2]')
    UltraBullet.click()
    time.sleep(2)

    # Another Continue button that must be found and clicked
    ContinueKnop2 = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[2]/button/span[1]')
    ContinueKnop2.click()
    time.sleep(2)

    # Then it must find Analyze Games and click it.
    AnalyseerPartijen = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/button/span[1]')
    AnalyseerPartijen.click()
    time.sleep(60)

    # Then it needs to be exported as PGN file, so that element must be found and clicked
    # I found out that you do not have to wait until all games are load in the previous step,
    # so that's why there's not a long wait between them
    ExporteerAlsPGN = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div[2]/button/span[1]')
    ExporteerAlsPGN.click()
    time.sleep(60)

    # This is an important step.In the Selenium module there's no build-in that waits until a file has been downloaded
    # so had to make something work.
    # The thing is that some files are small but some can be really large and because I want it to download
    # multiple files makes it hard to wait for it by building in a very long wait after every player.
    # I chose for a way that checks whether the downloaded file exists.
    # if not, it waits a seconds and checks it again. If the file has been downloaded, it breaks out.
    # And gives a print statement that someone's games have been downloaded. Note the formatting is now in {}.

    while not os.path.isfile(PathWit):
        time.sleep(2)
        continue
    else:
        print(f"De witpartijen van {spelers[i]} van Lichess.org zijn gedownload!")
        time.sleep(5)

    # After that, the program goes for the Black games. It doesn't have to go through everything again, it stays on
    # where it was and find the element on the website that can change the color and clicks on that
    Kleurverandering = web.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[1]/div[1]/span/img')
    Kleurverandering.click()
    time.sleep(2)

    # After finding that, it must find and click on 'Black'.
    KiesZwart = web.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[1]/fieldset/div/label[2]/span[2]')
    KiesZwart.click()
    time.sleep(2)

    # And find and press another Continue button...
    ContinueKnop3 = web.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[2]/button/span[1]')
    ContinueKnop3.click()
    time.sleep(2)

    # And this is exact the same and before
    AnalyseerPartijen = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/button/span[1]')
    AnalyseerPartijen.click()
    time.sleep(5)

    # Same goes for this, not that now the program is looking for Black games, the path is should look for is now PathZwart
    # instead of PathWit
    ExporteerAlsPGN = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div[2]/button/span[1]')
    ExporteerAlsPGN.click()
    time.sleep(30)

    while not os.path.isfile(PathZwart):
        time.sleep(2)
        continue
    else:
        print(f"De zwartpartijen van {spelers[i]} van Lichess.org zijn gedownload!")
        time.sleep(30)

    # And then the page gets a refresh
    web.refresh()
    # It went through everything, now it's time to go to the next element in the list, so i gets +1
    i = i + 1

# Now that the games from Lichess are downloaded, the same is done from Chess.com
# First the Paths and files are dynamically created
# Note: now the naming of the things are in English
# Because this is more or less exactly the same as before, I'll limit the number of comments.
while k < len(players):
    # Same as in the Lichess section, I put these inside the while loop to make it work
    ChesscomPath = "C:/Users/ewoud/Downloads/"
    FileWhite = (players[k] + '-white.pgn')
    FileBlack = (players[k] + '-black.pgn')
    PathWhite = (f'{ChesscomPath}/{FileWhite}')
    PathBlack = (f'{ChesscomPath}/{FileBlack}')

    Chesscom = web.find_element(By.XPATH, '//*[@id="panel1c-content"]/div/div/label[2]/span[2]/span/img')
    Chesscom.click()
    time.sleep(5)

    Name = web.find_element(By.XPATH, '//*[@id="playerNameTextBox"]')
    Name.send_keys(players[k])
    time.sleep(2)

    ContinueButton = web.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div[2]/button/span[1]')
    ContinueButton.click()
    time.sleep(2)

    PlayerIsWhite = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[1]/fieldset/div/label[1]/span[1]/span[1]/input')
    PlayerIsWhite.click()
    time.sleep(2)

    AdvancedFilters = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[2]/span')
    AdvancedFilters.click()
    time.sleep(2)

    TimeControl = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/span/span')
    TimeControl.click()
    time.sleep(2)

    RemoveBullet = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/label/span[2]')
    RemoveBullet.click()
    time.sleep(2)

    ContinueButton2 = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[2]/button/span[1]')
    ContinueButton2.click()
    time.sleep(2)

    AnalyzeGames = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/button/span[1]')
    AnalyzeGames.click()
    time.sleep(60)

    ExportAsPGN = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div[2]/button/span[1]')
    ExportAsPGN.click()
    time.sleep(60)
    while not os.path.isfile(PathWhite):
        time.sleep(2)
        continue
    else:
        print(f"De witpartijen van {players[k]} van Chess.com zijn gedownload!")
        time.sleep(30)

    # Switch to Black
    ColorChange = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[1]/div[1]/span/img')
    ColorChange.click()
    time.sleep(2)

    PickBlack = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[1]/fieldset/div/label[2]/span[1]/span[1]/input')
    PickBlack.click()
    time.sleep(2)

    ContinueButton3 = web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/div/div[2]/button/span[1]')
    ContinueButton3.click()
    time.sleep(2)

    AnalyzeGames = web.find_element(By.XPATH,  '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/button/span[1]')
    AnalyzeGames.click()
    time.sleep(60)

    ExportAsPGN = web.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div[2]/button/span[1]')
    ExportAsPGN.click()
    time.sleep(60)
    while not os.path.isfile(PathBlack):
        time.sleep(2)
        continue
    else:
        print(f"De zwartpartijen van {players[k]} van Chess.com zijn gedownload!")
    time.sleep(30)
    web.refresh()
    k = k + 1

# After everything is done, it closes itself.
web.close()
