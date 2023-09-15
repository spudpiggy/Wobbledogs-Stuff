#Requires AutoHotkey v2.0
#SingleInstance
; spudpiggy's Wobbledogs Helper Script
; This maps certain tasks to keys to make repeating them easier.
; I originally made this to automate aging up dogs using the Wobbledogs Toolkit

filename := "storage.txt"
delay := 150    ;
Rename(mode)
{
    Click 69, 58    ;Rename
    Sleep delay
    Click 952, 393  ;Click on name
    Sleep delay
    If (mode == 1) {
        SendInput "{Ctrl Down}c{Ctrl Up}"
        Sleep 200
        Send "{Esc}"    ;Exit out so we don't remove name
    }
    else {
        SendInput "{Ctrl Down}v{Ctrl Up}"
        Sleep 200
        Click 950, 633
    }
}
Import()
{
    Click 319, 629  ;Import Dog
    Sleep delay
    Click 741, 450  ;Paste
    Sleep delay
    Click 1193, 450 ;Import
    Sleep 500
    Click 977, 450  ;Okay
    Sleep delay
}
Export()
{
    Click 132, 634  ;Export Dog
    Sleep delay
    Click 972, 450  ;Copy
    Sleep delay
    Click           ;Okay
    Sleep delay
}

NumpadSub::Import()             ;Numpad - | Import Dog from Clipboard

NumpadAdd::{                    ;Numpad + | Export Dog to File
    Export
    FileAppend(A_Clipboard "`n", filename)
    Sleep 500
    Rename(1)
    FileAppend(A_Clipboard "`n", filename)
}

Numpad9::{                      ;Numpad 9 | Import Dog from File
    Loop read, filename
        {
            A_Clipboard := A_LoopReadLine   ;Copy line to clipboard
            If Mod(A_Index, 2) == 0 {       ;Setup for name support
                Rename(0)
            }Else {
                Import
            }
            Sleep 1000
        }
}

NumpadDiv::{                    ;Numpad Slash | Age Up Dog
    Export
    RunWait("python.exe Age.py") ;Age up
    Sleep delay
    Import
}