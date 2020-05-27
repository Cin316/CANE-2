cd ~
pulseaudio --start

DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo "info C8:84:47:16:62:3F" | "bluetoothctl"
echo "connect C8:84:47:16:62:3F" | "bluetoothctl"

sleep 15s
play -n synth 5 sine 880
py ~/CANE-2/CANE-client.py > '~/CANE-2/logs/$DATE' 
py ~/CANE-2/CANE-server.py > '~/CANE-2/logs/$DATE'
