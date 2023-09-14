#Requires AutoHotkey v2.0
#SingleInstance
;spudpiggy's Wobbledogs Helper (Disc 2)
;This contains binds that are too situational to go into the main script.

Numpad7::{      ;Numpad 7 | Spawn 10 Dogs
    Send "{Shift down} {\ down}"  ;Shift is my dev console 1 bind
    Sleep 100
    Send "{Shift up} {\ up}"        ;Release console keys
    Sleep 200
    SendText "SpawnDog 10"          ;Type the command
    Send "{Enter}"                  ;Run the command
    Sleep 7500
    Send "{Escape}"                 ;Close dev console
}

Numpad8::{                      ;Numpad 8 | Release Dog
    Click 584, 551  ;Release
    Sleep 50
    Click 735, 360  ;Release
}