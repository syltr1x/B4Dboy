sudo python -m http.server 80 -d server > output.txt 2>&1 &
if [ $1 == "listen" ]; then
    while true; do
        if grep -qE "$2\.$3\.$4\.[0-9]+" output.txt && grep -qE "temp" output.txt; then
            kill $(pgrep -f "python -m http.server 80 -d server")
            rm output.txt
            break
        fi
        sleep 1
    done
fi