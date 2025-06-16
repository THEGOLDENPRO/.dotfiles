#!/bin/sh

# I FUCKING HATE KWIN FUCKING SETTING MY FUCKING SECOND MONITOR
# FUCKING INCORRECTLY EVERY FUCKING BOOT! FUCK OFF!

if kscreen-doctor -o 2>&1 | sed 's/\x1b\[[0-9;]*m//g' | grep "Scale: 1.05"; then
    echo "Detected 'Scale: 1.05' — disabling HDMI-A-1 (second monitor)"
    kscreen-doctor output.HDMI-A-1.disable
else
    echo "Scale is not 1.05 — did not disable second monitor."
fi