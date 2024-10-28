#!/bin/bash
url=$1

cd work
yt-dlp $url

python3 ../rinomina_file.py

filename=$(ls)

echo $filename
output=${filename%.*}.mkv
echo $output

HandBrakeCLI -i $filename -o $output -Z "Chromecast 1080p60 Surround"

sleep 1

rm $filename

mv $output ../ftp

cd ../ftp

sleep 1

HOST='192.168.178.29'
USER='andrea'
PASSWD='H0m3F!sh'

ftp -n $HOST <<END_SCRIPT
quote USER $USER
quote PASS $PASSWD
cd media
binary
put $output
quit
END_SCRIPT

rm $output

exit 0
