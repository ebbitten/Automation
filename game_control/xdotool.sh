xdotool getmouselocation 2>&1 |
    sed -rn '${s/x:([0-9]+) y:([0-9]+) .*/\1 \2/p}'