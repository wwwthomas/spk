#!/bin/bash


PID=$!
echo "derun" && source "/root/saltpepperketchup/bin/activate" && python-dotenv -f /root/saltpepperketchup/.f/.env run python3 /root/saltpepperketchup/decrypt.py & sleep 1 &
wait $!
echo "Process 2 ended at time $(date +%T) with exit status $?"
wait

