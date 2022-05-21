g++ -o main ./main.cpp
$n = Get-Random -Minimum 10 -Maximum 20
$dat = 1..100 | Get-Random -Count "$n"
Write-Output ("=" * 60)
Write-Output "Test Data : $dat"
Write-Output ("=" * 60)
$dat | .\main.exe