# Fixed by BlenderRender#0001
# Pyperclip/tkinter added by spudpiggy

import pyperclip
from tkinter import messagebox
from re import findall, sub, escape, subn

def Start():
    print("Your dog code will be grabbed from the clipboard.")
    print("Make sure you've exported it before running the script.")
    code = pyperclip.paste()
    Change_Age(code)


def Unwinder(DogCode):
    workingCode = DogCode[::-1]
    workingCodeList = []

    for char in workingCode:
        workingCodeList.append(char)

    # using workingCodeList:
    for i in range(len(workingCodeList)):
        indexToSwap = ord(
            workingCodeList[(i - 1) % len(workingCodeList)]
        )
        workingCodeList[i], \
            workingCodeList[(i - indexToSwap) % len(workingCode)] = \
            workingCodeList[(i - indexToSwap) % len(workingCode)], \
            workingCodeList[i]

    workingCode = ""

    for char in workingCodeList[::-1]:
        workingCode += char

    return workingCode


def Winder(DogCode):
    workingCode = DogCode
    workingCodeList = []

    for char in workingCode:

        workingCodeList.append(char)

    for i in range(len(workingCodeList)):

        indexToSwap = ord(
            workingCodeList[(i + 1) % len(workingCodeList)]
        )

        workingCodeList[i], \
            workingCodeList[(i + indexToSwap) % len(workingCode)] = \
            workingCodeList[(i + indexToSwap) % len(workingCode)], \
            workingCodeList[i]

    workingCode = ""

    for char in workingCodeList:
        workingCode += char

    return workingCode


def Change_Age(DogCode):
    thisCode = Unwinder(DogCode)

    if not findall(r'\^((?:[0-2]{7}))', thisCode):
        messagebox.showerror(title=None, message="Invalid dog code. Did you forget to export it?")
        exit()
    
    print('Your dog\'s personality code is:', findall(r'\^((?:[0-2]{7}))', thisCode))
    print("""\n
1 = 0 is social, 1 is none, 2 is aloof
2 = 0 is high energy, 1 is none, 2 is layabout
3 = 0 is glutton, 1 is none, 2 is averse
4 = 0 is polite, 1 is none, 2 is rude
5 = 0 is peaceful, 1 is none, 2 is antagonistic
6 = 0 is pettable, 1 is unpettable 
7 = 0 is none, 1 is loud, 2 is quiet
	\n""")

    sevenDigitTraits = input("Using the list above, enter in your traits (must be six digits long)\n")

    newCode = sub(r'((?:[0-2]{7}))', sevenDigitTraits, thisCode)
    pyperclip.copy(Winder(newCode))
    print("Dog personality changed!\n Your new dog code has been copied to the clipboard.")


Start()
