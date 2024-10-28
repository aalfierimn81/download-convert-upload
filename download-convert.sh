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
