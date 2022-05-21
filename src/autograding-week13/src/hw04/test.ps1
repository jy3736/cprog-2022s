g++ -o main ./main.cpp
$n = Get-Random -Minimum 5 -Maximum 15
$dat = 1..100 | Get-Random -Count "$n"
Write-Output "Test Data : $dat"
Write-Output ""
$dat | .\main.exe