#!/bin/bash

echo "Listening on UDP port 11234"
#nc -p 11234 -u localhost
nc -ul localhost 11234