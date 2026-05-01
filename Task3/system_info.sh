#!/bin/bash
{
echo "Generated: $(date)"
echo ""
echo "--- HOSTNAME ---"
hostname
echo ""

echo "---KERNEL VERSION ---"
uname -r
echo ""

echo "--- CPU INFO ---"
lscpu
echo ""

echo "--- MEMORY ---"
free -h
echo ""

echo "--- DISK SPACE ---"
df -h
echo ""

echo "--- IP ADDRESS ---"
ip a
echo ""

echo "--- UPTIME ---"
uptime
echo ""

echo "--- LOGGED IN USERS ---"
users

} > system_info.txt
