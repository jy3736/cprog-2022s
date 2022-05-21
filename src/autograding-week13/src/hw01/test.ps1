g++ -o main ./main.cpp
$dat = 3..8 | Get-Random -Count 1
Write-Output "Test Data : $dat"
Write-Output ""
$dat | .\main.exe