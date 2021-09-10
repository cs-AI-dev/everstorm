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

window = Tk() # Initialize master window
inFullscreen = False

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
        this.white = "ffffff"
        this.lightGray = "bfbfbf"
        this.gray = "808080"
        this.darkGray = "404040"
        this.black = "000000"

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
        this.top = Frame(window, bg=color.red.red, height=200, width=1000) # Top padding frame
        this.top.grid(row=1, column=2, columnspan=7) # Columns 1 and 9 reserved for L/R paddings.

        this.left = Frame(window, bg=color.blue.blue, height=650, width=200) # Left padding frame
        this.left.grid(row=1, rowspan=9, column=1)

        this.right = Frame(window, bg=color.blue.blue, height=650, width=200) # Right padding frame
        this.right.grid(row=1, rowspan=9, column=9)

        this.chara1Left = Frame(window, bg=color.green.green, height=60, width=90)
        this.chara1Left.grid(row=3, column=2)

class dialogueBoxClass:
    def __init__(this):
        this.parentFrame = Frame(window, bg=color.white, padx=5, pady=5, height=125, width=990)
        this.parentFrame.grid(row=2, column=2, columnspan=7)
        this.parentFrame.grid_propagate(False)

        this.textBox = Label(
        this.parentFrame, bg=color.black, fg=color.white, width=51, height=3,
        text="* ExampleText Example Text example, ExampleText.\n* Exampletext?\n* Exampletext exampletext.", font=("OCR A Extended", 24),
        justify=LEFT
        )
        this.textBox.grid(row=1, column=1)

class objectsClass:
    def __init__(this):
        this.padding = paddingClass()
        this.dialogueBox = dialogueBoxClass()

if __name__ == "__main__":
    print("[everstorm] compiling ...")

    color = colorPalette()
    object = objectsClass()

    window.resizable(width=False, height=False)
    window.title("EVERSTORM")
    window.configure(bg=color.black)
    #toggleFullscreen()




    print("[everstorm] compilation complete.")
    window.mainloop() # Run the game
