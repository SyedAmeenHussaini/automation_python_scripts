# Auth Log Monitor

## Overview
This Python script continuously monitors the specified authentication log file for new invalid login attempts and retrieves the location information of the attacker's IP address using the `geoiplookup` command. It then prints the attacker's country along with the IP address.

## Prerequisites
- This script requires Python 3.x to be installed on your system.
- The `geoiplookup` command (from the `geoip-bin` package) is required for retrieving location information. You can install it using the following command:
  ```bash
  sudo apt install geoip-bin

