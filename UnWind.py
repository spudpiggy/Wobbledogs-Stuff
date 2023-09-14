# Fixed by BlenderRender#0001
# Pyperclip added by spudpiggy

import pyperclip
all_dog_ages = ["PUPPY", "CHILD", "TEEN", "YOUNGADULT", "ADULT", "ANCIENT"]


def Start():
    print("Your dog code will be grabbed from the clipboard.")
    print("Make sure you've exported it before running the script.")
    code = pyperclip.paste()
    Unwinder(code)


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

    pyperclip.copy(workingCode)
    print("Your dog code has been copied to the clipboard.")


Start()
