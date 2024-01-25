#!/bin/bash

# Author: Ankit Raut 

# Description: This script can be used to check weather specific Ip address and port is rechable or not.

check_reachability() {
    ip=$1
    port=$2

    if [ -z "$ip" ] || [ -z "$port" ]; then
        echo "IP or Port Not Provided"
        exit 1
    fi
    nc -zv -w 5 $ip $port

}
read -p "Enter IP Address::" ip
read -p "Enter Port Number::" port

check_reachability $ip $port


