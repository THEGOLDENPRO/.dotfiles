#!/bin/sh

# I FUCKING HATE KWIN FUCKING SETTING MY FUCKING SECOND MONITOR
# FUCKING INCORRECTLY EVERY FUCKING BOOT! FUCK OFF!

count = 0

attempt_monitor_disable () {
    if kscreen-doctor -o 2>&1 | sed 's/\x1b\[[0-9;]*m//g' | grep "Scale: 1.05"; then
        echo "Detected 'Scale: 1.05' — disabling HDMI-A-1 (second monitor)"
        kscreen-doctor output.HDMI-A-1.disable
        return 0
    else
        echo "Scale is not 1.05 — did not disable second monitor."
        return 1
    fi
}

while true; do
    count=$((count + 1))

    echo "Attempt ${count}..."

    attempt_monitor_disable
    response=$?

    if [ "$response" -eq 1 ]; then
        if [ "$count" -ge 3 ]; then
            break
        fi

        sleep 0.5
    else
        break
    fi
done