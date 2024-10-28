#!/bin/bash

HOST='192.168.178.29'
USER='andrea'
PASSWD='H0m3F!sh'

cd ftp

filename=$(ls)

for FN in $filename
do
sleep 1
	
ftp -n $HOST <<END_SCRIPT
quote USER $USER
quote PASS $PASSWD
cd media
binary
put $FN
quit
END_SCRIPT
	
rm $FN
	
done

exit 0

