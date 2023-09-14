#Requires AutoHotkey v2.0
#SingleInstance
; spudpiggy's Wobbledogs Helper Script
; This maps certain tasks to keys to make repeating them easier.
; I originally made this to automate aging up dogs using the Wobbledogs Toolkit

filename := "storage.txt"
Import()
{
    Click 319, 629  ;Import Dog
    Sleep 100
    Click 741, 450  ;Paste
    Sleep 100
    Click 1193, 450 ;Import
    Sleep 500
    Click 977, 450  ;Okay
    Sleep 100
}
Export()
{
    Click 132, 634  ;Export Dog
    Sleep 100
    Click 972, 450  ;Copy
    Sleep 100
    Click           ;Okay
    Sleep 100
}

NumpadSub::Import()             ;Numpad - | Import Dog from Clipboard

NumpadAdd::{                    ;Numpad + | Export Dog to File
    Export
    FileAppend(A_Clipboard "`n", filename)
}

Numpad9::{                      ;Numpad 9 | Import Dog from File
    Loop read, filename
        {
                A_Clipboard := A_LoopReadLine   ;Copy line to clipboard
                Import
                Sleep 1000
        }
}

NumpadDiv::{                    ;Numpad Slash | Age Up Dog
    Export
    RunWait("python.exe Age.py") ;Age up
    Sleep 100
    Import
}