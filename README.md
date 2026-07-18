# Python Network Information Collector

## Overview

This beginner-friendly Python script uses **Netmiko** to connect to a Cisco IOS network device through SSH, run operational commands, and save the results to a text file.

## What the Script Does

The script:

* Connects to a Cisco router or switch using SSH
* Prompts the user for a username and password
* Runs several `show` commands
* Saves the command output to `network_report.txt`
* Disconnects from the device

## Commands

The script runs:

* `show ip interface brief`
* `show ip route`
* `show version`

## Requirements

* Python 3
* Netmiko
* Cisco IOS router or switch
* SSH connectivity to the network device

Install Netmiko:

```bash
pip install netmiko
```

## Usage

Update the device IP address in the Python script:

```python
"host": "192.168.1.1"
```

Run the script:

```bash
python network_automation.py
```

Enter your username and password when prompted.

## Skills Demonstrated

* Python
* Network Automation
* Netmiko
* SSH
* Cisco IOS
* Network Information Collection
* File Handling

## Purpose

This project demonstrates how Python can automate the process of connecting to a network device, collecting operational information, and saving the results for troubleshooting or documentation.

This script is intended for learning and lab environments.
