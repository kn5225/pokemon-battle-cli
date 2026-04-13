#Requires AutoHotkey v2.0
#SingleInstance
Esc::ExitApp

!a::
{
    MaxVal := Integer(FileRead(".\movnumwrite.txt"))
    
    ; Read current tracker value (default 1 if file missing)
    TrackerPath := ".\tracker.txt"
    Try
        Current := Integer(FileRead(TrackerPath))
    Catch
        Current := 0

    ; Increment and loop
    Next := Mod(Current, MaxVal) + 1

    ; Save tracker
    FileOpen(TrackerPath, "w").Write(Next)

    ; Clear current line and type the new number
    Send "{BS 5}" 
    Sleep 100
    Send String(Next)
}