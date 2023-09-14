# Fixed by BlenderRender#0001
# Pyperclip/tkinter added by spudpiggy
import pyperclip
from tkinter import messagebox

all_dog_ages = ["PUPPY", "CHILD", "TEEN", "YOUNG_ADULT", "ADULT", "ANCIENT"]


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
    print("Changing dog age to Adult!")

    thisCode = Unwinder(DogCode)

    foundAge = ""

    for val in all_dog_ages:
        if val in thisCode:
            foundAge = val
            break

    if not foundAge:
        messagebox.showerror(title=None, message="Invalid dog code. Did you forget to export it?")
        exit()

    print(f"Dog Age = {foundAge}")
	# Ages: PUPPY, CHILD, TEEN, YOUNG_ADULT, ADULT or ANCIENT
    
    newCode = thisCode.replace(foundAge, "ADULT")
    print("Changed to Adult successfully!\nYour new code has been copied to the clipboard.")
    pyperclip.copy(Winder(newCode))
Start()