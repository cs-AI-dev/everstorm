# Copyright 2021 [name of copyright owner]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pprint import pprint             # PPrint      # Tool for DBing objects
from PIL import Image                 # Pillow      # image processing library
from tkinter import *                 # Tkinter     # GUI assembly API
from random import randint as random  # random      # Random number generator
from time import sleep as timeout     # time        # Sleeper
import simpleaudio as audio           # simpleaudio # Audio playing library

import playsound


window = Tk() # Initialize master window
inFullscreen = False

def font(size):
    return ("OCR A Extended", int(size))

def getAudio(wavFile):
    playsound.playsound(wavFile)
    #return audio.WaveObject.from_wave_file(wavFile)

def getPillowAsset(assetName):
    return "everstorm/assets/" + assetName

assetsIndicator = 1
usedAssets = {}

def getAsset(assetName):
    print("setting globals ...", end="")
    global assetsIndicator
    global usedAssets
    print("done.\nincrementing assetsIndicator ...", end="")
    assetsIndicator += 1
    print("done.\nadding asset to usedAssets ...", end="")
    usedAssets[assetsIndicator] = PhotoImage(file="E:\\computer_science\\everstorm\\assets\\" + assetName + ".pgm")
    pprint(vars(usedAssets[assetsIndicator]))
    print("done.\nreturning value " + str(assetsIndicator) + ", equal to " + str(usedAssets[assetsIndicator]) + " ...")
    return assetsIndicator

CHARA1 = "chara1"
c1_stored = None
CHARA2 = "chara2"
c2_stored = None
CHARA3 = "chara3"
c3_stored = None
PLAYER = "player"
pl_stored = None

canvasStorage = {
    CHARA1: None,
    CHARA2: None,
    CHARA3: None,
    PLAYER: None,
}

class redClass:
    def __init__(this):
        this.veryLight = "#FF9999"
        this.light = "#FF6666"
        this.slightlyLight = "#FF3333"
        this.red = "#FF0000"
        this.slightlyDark = "#CC0000"
        this.dark = "#990000"
        this.veryDark = "#660000"

class goldClass:
    def __init__(this):
        this.veryLight = "#FFE699"
        this.light = "#FFD966"
        this.slightlyLight = "#FFCC33"
        this.gold = "#FFBF00"
        this.slightlyDark = "#CC9900"
        this.dark = "#997300"
        this.veryDark = "#332600"

class greenClass:
    def __init__(this):
        this.veryLight = "#99FF99"
        this.light = "#66FF66"
        this.slightlyLight = "#33FF33"
        this.green = "#00FF00"
        this.slightlyDark = "#00CC00"
        this.dark = "#009900"
        this.veryDark = "#006600"

class blueClass:
    def __init__(this):
        this.veryLight = "#99C2FF"
        this.light = "#66A3FF"
        this.slightlyLight = "#3385FF"
        this.blue = "#0066FF"
        this.slightlyDark = "#0052CC"
        this.dark = "#003D99"
        this.veryDark = "#002966"

class grayscaleClass:
    def __init__(this):
        this.white = "#ffffff"
        this.lightGray = "#bfbfbf"
        this.gray = "#808080"
        this.darkGray = "#404040"
        this.black = "#000000"

class colorPalette:
    def __init__(this):
        global goldClass, blueClass, greenClass, redClass, grayscaleClass
        this.gold = goldClass()
        this.blue = blueClass()
        this.green = greenClass()
        this.red = redClass()
        this.grayscale = grayscaleClass()
        this.black = "#000000"
        this.white = "#FFFFFF"
        del goldClass, blueClass, greenClass, redClass, grayscaleClass

def toggleFullscreen():
    global inFullscreen
    if inFullscreen == True:
        window.attributes("-fullscreen", False)
        inFullscreen = False
    else:
        window.attributes("-fullscreen", True)
        inFullscreen = True

class paddingClass:
    # 9 columns exist - left padding, C-1 left padding, character one spot, C1-2 padding, character 2 spot, C2-3 padding, character 3 spot, C-3 right padding, and right padding
    # 9 rows exist - top row (padding), top dialogue box, characters 2 and 3, character 1, character-player padding, player, player-stats padding, stats/actions, and bottom padding.
    def __init__(this):
        this.top = Frame(window, bg=color.grayscale.black, height=50, width=1000) # Top padding frame
        this.top.grid(row=1, column=2, columnspan=7) # Columns 1 and 9 reserved for L/R paddings.

        this.left = Frame(window, bg=color.grayscale.black, height=500, width=200) # Left padding frame
        this.left.grid(row=1, rowspan=9, column=1)

        this.right = Frame(window, bg=color.grayscale.black, height=500, width=200) # Right padding frame
        this.right.grid(row=1, rowspan=9, column=9)

        this.chara3_2DialogueBox = Frame(window, bg=color.grayscale.black, height=90, width=200)
        this.chara3_2DialogueBox.grid(row=2, column=5)

        this.chara1Left = Frame(window, bg=color.grayscale.black, height=60, width=90)
        this.chara1Left.grid(row=3, column=2, columnspan=2)

        this.chara1chara3 = Frame(window, bg=color.grayscale.black, height=60, width=120)
        this.chara1chara3.grid(row=3, column=5)

        this.chara3Right = Frame(window, bg=color.grayscale.black, height=60, width=90)
        this.chara3Right.grid(row=3, column=7)

        this.chara2Left = Frame(window, bg=color.grayscale.black, height=60, width=180)
        this.chara2Left.grid(row=4, column=2, columnspan=3)

        this.chara2Right = Frame(window, bg=color.grayscale.black, height=60, width=180)
        this.chara2Right.grid(row=4, column=6, columnspan=3)

        this.chara2Player = Frame(window, bg=color.grayscale.black, height=125, width=300)
        this.chara2Player.grid(row=5, column=2, columnspan=7)

        this.playerStatsBox = Frame(window, bg=color.grayscale.black, height=100, width=200)
        this.playerStatsBox.grid(row=7, column=5)

        this.statsBoxBar = Frame(window, bg=color.grayscale.white, height=5, width=1400)
        this.statsBoxBar.grid(row=8, column=1, columnspan=9)

        this.statsBoxBarStatsLabel = Frame(window, bg=color.grayscale.black, height=20, width=1399)
        this.statsBoxBarStatsLabel.grid(row=9, column=1, columnspan=9)

        this.statbarLabelStats = Frame(window, bg=color.grayscale.black, height=20, width=1399)
        this.statbarLabelStats.grid(row=11, column=1, columnspan=9)

class dialogueBoxClass:
    def __init__(this):
        this.parentFrame = Frame(window, bg=color.white, padx=5, pady=5, height=125, width=990)
        this.parentFrame.grid(row=1, column=2, columnspan=7)
        this.parentFrame.grid_propagate(False)

        this.textToDisplay = "* ExampleText Example Text example, ExampleText.\n* Exampletext?\n* Exampletext exampletext..."
        this.textIncrement = 0

        this.currentDisplay = StringVar()
        this.currentDisplay.set("")

        this.textBox = Label(
        this.parentFrame, bg=color.black, fg=color.white, width=51, height=3,
        textvariable=this.currentDisplay, font=font(24),
        justify=LEFT
        )
        this.textBox.grid(row=1, column=1, columnspan=4)

    def updateText(this, null=None):
        this.textIncrement += 1
        out = ""
        for char in list(this.textToDisplay)[0:int(this.textIncrement)]:
            out = out + char
        this.setText(out)
        lchar = list(char)[-1]
        if lchar == ",":
            timeout(0.2)
        if lchar == "." or lchar == "?" or lchar == "!":
            timeout(0.5)
        return True

    def setText(this, text):
        this.currentDisplay.set(text)

    def setNextText(this, text):
        this.textIncrement = 0
        this.textToDisplay = text + "          "

    def say(this, text="DIALOGUE_BOX_ERROR:NO_TEXT_PROVIDED", speechbite=None):
        doSB = True
        this.textIncrement = 0
        this.textToDisplay = text

        printedText = ""
        if speechbite == None:
            for x in range(len(list(text))):
                this.updateText()
                this.textBox.update()
                timeout(0.05)

        else:
            doSB = True
            for letter in list(text):
                this.updateText()
                if letter == "[":
                    doSB = False
                if doSB == True:
                    getAudio(speechbite)
                this.textBox.update()
                if letter == ",":
                    timeout(0.2)
                if letter == ".":
                    timeout(0.5)

class playerStatsClass:
    def __init__(this):
        pass

class playerClass:
    def __init__(this):
        this.sprite = Frame(window, bg=color.green.green, width=60, height=60)
        this.sprite.grid(row=6, column=5)

class statBarHealthClass:
    def __init__(this):
        this.label = Label(window, bg=color.grayscale.black, fg=color.grayscale.white, text="Health                                                                    ", font=font(14))
        this.label.grid(row=13, column=1, columnspan=9)

        this.parentFrame = Frame(window)
        this.parentFrame.grid(row=14, column=1, columnspan=9)

        this.healthPositiveBar = Frame(this.parentFrame, width=1398, bg=color.green.green, height=20)
        this.healthPositiveBar.grid(row=1, column=1)

        this.healthNegativeBar = Frame(this.parentFrame, width=1, bg=color.red.red, height=20)
        this.healthNegativeBar.grid(row=1, column=2)

    def setHealthBar(this, healthValue):
        if int(healthValue*14) >= 1398:
            this.healthPositiveBar.config(width=1398)
        else:
            this.healthPositiveBar.config(width=(int(healthValue)*14))
        this.healthNegativeBar.config(width=(1398-(int(healthValue)*14)))

class statBarManaClass:
    def __init__(this):
        this.label = Label(window, bg=color.grayscale.black, fg=color.grayscale.white, text="Mana                                                                      ", font=font(14))
        this.label.grid(row=15, column=1, columnspan=9)

        this.parentFrame = Frame(window)
        this.parentFrame.grid(row=16, column=1, columnspan=9)

        this.manaPositiveBar = Frame(this.parentFrame, width=1398, bg=color.blue.blue, height=20)
        this.manaPositiveBar.grid(row=1, column=1)

        this.manaNegativeBar = Frame(this.parentFrame, width=1, bg=color.red.red, height=20)
        this.manaNegativeBar.grid(row=1, column=2)

    def setManaBar(this, manaValue):
        if int(manaValue*14) >= 1398:
            this.manaPositiveBar.config(width=1398)
        else:
            this.manaPositiveBar.config(width=(int(manaValue)*14))
        this.manaNegativeBar.config(width=(1398-(int(manaValue)*14)))

class healthBarClass:
    def __init__(this):
        this.parentFrame = Frame(window, bg=color.grayscale.black)
        this.parentFrame.grid(row=12, column=1, columnspan=9)

        this.label = Label(this.parentFrame, bg=color.grayscale.black, fg=color.grayscale.white, text="HEALTH")
        this.label.grid(row=1, column=1)

class statBarClass:
    def __init__(this):
        this.label = Label(window, bg=color.grayscale.black, fg=color.grayscale.white, text="PLAYER_NAME", font=font(20))
        this.label.grid(row=10, column=1, columnspan=9)

        this.healthBar = statBarHealthClass()
        this.manaBar = statBarManaClass()


class objectsClass:
    def __init__(this):
        this.padding = paddingClass()
        this.dialogueBox = dialogueBoxClass()

        this.chara1 = Frame(window, bg=color.gold.gold, width=60, height=60)
        this.chara1.grid(row=3, column=4)

        this.chara2 = Frame(window, bg=color.gold.gold, width=60, height=60)
        this.chara2.grid(row=4, column=5)

        this.chara3 = Frame(window, bg=color.gold.gold, width=60, height=60)
        this.chara3.grid(row=3, column=6)

        this.player = playerClass()

        this.statbar = statBarClass()

class playerModifierArmorClass:
    def __init__(armor):
        armor.superficialDamageThreshold = 0 # An amount of damage equal to or less than this is reduced to 0.
        armor.criticalDamageThreshold = 0    # Damage is doubled if a random number between 1 and 100 is greater than or equal to this.
        armor.damageReduction = 0            # Incoming damage is reduced by this percent.

class playerModifierHealthClass:
    def __init__(health):
        health.regenChance = 0   # Every turn you have a chance to regain health equal to this number in 100.
        health.regenAmount = 0   # If you do regain health by chance, you regain this much health.
        health.regenAddition = 0 # If you do regain health in any way, it's increased by this percent.

class playerModifierManaClass:
    def __init__(mana):
        mana.regenChance = 0   # Every turn you have a change to regain mana equal to this number in 100.
        mana.regenAmount = 0   # If you do regain mana by cnahce, you regain this much mana.
        mana.regenAddition = 0 # If you do regain mana in any way, it's increased by this percent.
        mana.costReduction = 0 # Amount by which the cost of casting spells is reduced in mana.

class playerModifierAttackClass:
    def __init__(attack):
        attackDamage = 5    # Minimum amount of damage to deal.
        attackModifier = 10 # Adds between 0 and this to any attack.
        criticalHitRate = 5 # Chance in 100 for damage to be doubled.

class playerModifierClass:
    def __init__(modifier):
        modifier.armor = playerModifierArmorClass()
        modifier.health = playerModifierHealthClass()
        modifier.mana = playerModifierManaClass()
        modifier.attack = playerModifierAttackClass()

class playerStatsClass:
    def __init__(player):
        player.health = 100
        player.mana = 50
        player.modifier = playerModifierClass()

# Main loop. API fully constructed at this point. GUI assembled by `window.mainloop()`, last line of code.
if __name__ == "__main__":
    print("[everstorm] compiling ...")

    color = colorPalette()
    object = objectsClass()

    window.resizable(width=False, height=False)
    window.title("EVERSTORM")
    window.configure(bg=color.black)
    #toggleFullscreen()

    object.dialogueBox.setNextText("* ExampleText Example Text example, ExampleText.\n* Exampletext?\n* Exampletext exampletext...")

    object.statbar.healthBar.setHealthBar(90)

    print(" | loading levels ...")
    object.chara1.config(bg=color.grayscale.black)
    object.chara2.config(bg=color.grayscale.black)
    object.chara3.config(bg=color.grayscale.black)
    object.chara1.config(bg=color.grayscale.black)
    blackouts = []

    ssb = "E:/computer_science/everstorm/mSound.wav"

    testmode = False

    def secret(x):
        object.dialogueBox.say("(What? I didn't say 'X' was an option.)")
        timeout(0.5)
        object.dialogueBox.say("(How did... what?)\n(Whatever. They said this might happen.)\n(CMD:py -c __main__.this.window.destroy())")
        window.destroy()
        print("ERROR AT 0x457A656C6F747A -> Jeez. Can't these simulos just take a hint?")
        print("ERROR AT 0x53796D6E69 -> It's not their fault. Don't blame your weird spell wording on them.")
        exit()

    def l1_keep_going(x):
        object.dialogueBox.say("* You continue on, and your headache fades. Good job.")

    def l1_find_village(x):
        pass

    def l1_spell(x):
        object.dialogueBox.say("* Looks like there are a couple neat\nsunlit spots nearby.", ssb)
        timeout(0.5)
        object.dialogueBox.say("* You can see a glade, a spot you might\nbe able to reach on a mountain,\nor just right here.", ssb)
        timeout(1)
        object.dialogueBox.say("[A -> FOREST GLADE]\n[W -> MOUNTAIN SPT]\n[D ->  RIGHT HERE ]")
        window.bind("d", l2_right_here)
        window.bind("w", l2_mountain_spot)
        window.bind("a", l2_glade)

    def l2_right_here(x):
        object.dialogueBox.say("...")
        timeout(0.5)
        object.statbar.healthBar.setHealthBar(5)
        object.statbar.manaBar.setManaBar(50)
        object.dialogueBox.say("* OWWWWW.\n* You feel a lot closer to death now. ...", ssb)
        l0(None)

    def l2_mountain_spot(x):
        object.dialogueBox.say("* You go and cast the spell, and ...", ssb)
        timeout(1)
        if random(1, 10) >= 3:
            object.statbar.healthBar.setHealthBar(100)
            object.dialogueBox.say("* you feel all better!\n* Looks like you'll be making it to that tavern.", ssb)
            timeout(2)
            window.destroy()
            exit()
        else:
            object.dialogueBox.say("* ... you feel a strange disturbance.\nYou, unfortunately, aren't healed.", ssb)
            timeout(1)
            l0(None)

    def l2_glade(x):
        object.dialogueBox.say("* You step into the verdure-laden glade.\n* You know two spells that you could\n* use to heal yourself here.", ssb)
        timeout(1)
        object.dialogueBox.say("* One that you learned in the schools of magic,\n and one from your mother, who\nis a mage.", ssb)
        timeout(1)
        object.dialogueBox.say("[A -> SCHOOL'S SPELL]\n[D -> MOTHER'S SPELL]")
        window.bind("a", l2_right_here)
        window.bind("d", l2_mountain_spot)

    firstTime = True

    def l0(x):
        global firstTime
        if firstTime == True:
            firstTime = False
        else:
            object.dialogueBox.say("* Back where you started.")
            timeout(1)
        object.dialogueBox.say("[W -> KEEP GOING]\n[A -> CAST SPELL]\n[D -> FIND VILL.]")
        window.bind("x", secret)
        window.bind("a", l1_spell)
        window.bind("w", l1_keep_going)
        window.bind("d", l1_find_village)

    def runLevels(x):
        print("[everstorm] entering levels.")

        if testmode == False:
            object.dialogueBox.say("* All of a sudden, you don't feel too well.\n* Your head is hurting. Kinda bad.", ssb)
            timeout(1)
            object.dialogueBox.say("* You could always try and cast a spell to\nmake yourself feel better.\n[PRESS A]", ssb)
            timeout(1)
            object.dialogueBox.say("* Or just keep going. Not really a huge\nproblem... probably...\n[PRESS W]", ssb)
            timeout(1)
            object.dialogueBox.say("* Or maybe you could find a village nearby\nthat'd be willing to treat you?\n[PRESS D]", ssb)
            timeout(1)
            object.dialogueBox.say("* Actually you remember there aren't any\nvillages nearby ... aww ...")
        timeout(1)
        l0(None)

    window.bind("<Return>", runLevels)

    print("[everstorm] compilation complete.")
    window.mainloop() # Run the game
