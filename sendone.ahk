#Requires AutoHotkey v2.0
#SingleInstance
Esc::ExitApp
SetTimer CheckFileContent, 1000
Enter::
{
    Send '{Enter}'
    SetTimer CheckFileContent, 1000
}
CheckFileContent(){
	FC := FileRead('.\input.txt')
	If FC = 'InputAwaited'
	{
	Sleep "100"
	Send "1"
	SetTimer CheckFileContent, 0
	}
}



