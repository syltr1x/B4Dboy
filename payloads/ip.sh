ip=$("curl -s https://api.ipify.org")
data=$("curl -s ipinfo.io/$ip?token=a70e36470018f5")
echo $data >> "data.json"