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

from tkinter import *
from random import randint as random
from time import sleep as timeout
import simpleaudio as audio

window = Tk() # Initialize master window
inFullscreen = False

def font(size):
    return ("OCR A Extended", int(size))

def getAudio(wavFile):
    return audio.WaveObject.from_wave_file(wavFile)

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
        this.textBox.grid(row=1, column=1)

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
        this.textIncrement = 0
        this.textToDisplay = text

        printedText = ""
        if speechbite == None:
            for x in len(list(text)):
                this.updateText()
                timeout(0.05)

        else:
            for letter in list(text):
                this.updateText()
                speechSound = getAudio(speechbite).play()
                speechSound.wait_done()

class playerStatsClass:
    def __init__(this):
        pass

class playerClass:
    def __init__(this):
        this.sprite = Frame(window, bg=color.green.green, width=60, height=60)
        this.sprite.grid(row=6, column=5)
        
class statBarHealthClass:
    def __init__(this):
        this.parentFrame = Frame(window)
        this.parentFrame.grid(row=11, column=1, columnspan=9)
        
        this.healthPositiveBar = Frame(this.parentFrame, width=1398, bg=color.green.green)
        this.healthPositiveBar.grid(row=1, column=1)
        
        this.healthNegativeBar = Frame(this.parentFrame, width=1, bg=color.red.red)
        this.healthNegativeBar.grid(row=1, column=2)
        
    def setHealthBar(healthValue):
        if int(healthValue*14) >= 1398:
            this.healthPositiveBar.config(width=1398)
        else:
            this.healthPositiveBar.config(width=(int(healthValue)*14))
        this.healthNegativeBar.config(width=(1398-(int(healthValue)*14)))
        
class statBarManaClass:
    def __init__(this):
        this.parentFrame = Frame(window)
        this.parentFrame.grid(row=11, column=1, columnspan=9)
        
        this.manaPositiveBar = Frame(this.parentFrame, width=1398, bg=color.green.green)
        this.manaPositiveBar.grid(row=1, column=1)
        
        this.manaNegativeBar = Frame(this.parentFrame, width=1, bg=color.red.red)
        this.manaNegativeBar.grid(row=1, column=2)
        
    def setManaBar(manaValue):
        if int(manaValue*14) >= 1398:
            this.manaPositiveBar.config(width=1398)
        else:
            this.manaPositiveBar.config(width=(int(manaValue)*14))
        this.manaNegativeBar.config(width=(1398-(int(manaValue)*14)))

class statBarClass:
    def __init__(this):
        this.label = Label(window, bg=color.grayscale.black, fg=color.grayscale.white, text="PLAYER_NAME", font=font(20))
        this.label.grid(row=10, column=1)
        
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

class playerModifierClass:
    def __init__(modifier):
        modifier.armor = playerModifierArmorClass()
        modifier.health = playerModifierHealthClass()
        modifier.mana = playerModifierManaClass()

class playerStatsClass:
    def __init__(player):
        player.health = 100
        player.mana = 50
        player.modifier = playerModifierClass()

if __name__ == "__main__":
    print("[everstorm] compiling ...")

    color = colorPalette()
    object = objectsClass()

    window.resizable(width=False, height=False)
    window.title("EVERSTORM")
    window.configure(bg=color.black)
    #toggleFullscreen()

    object.dialogueBox.setNextText("* ExampleText Example Text example, ExampleText.\n* Exampletext?\n* Exampletext exampletext...")

    window.bind("<Return>", object.dialogueBox.updateText)

    print("[everstorm] compilation complete.")
    window.mainloop() # Run the game
