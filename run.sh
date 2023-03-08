#!/bin/bash


PID=$!
echo "run" && source "/root/saltpepperketchup/bin/activate" && python-dotenv -f /root/saltpepperketchup/.f/.env run python3 /root/saltpepperketchup/spkm.py & sleep 1 &
wait $!
echo "Process 1 ended at time $(date +%T) with exit status $?"
wait


