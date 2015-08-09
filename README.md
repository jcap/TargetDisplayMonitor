# Target Display Monitor

Target Display Monitor monitors /var/log/system.log for patterns that indicate
the initiation or termination of Target Display Mode and then disables local
bluetooth or enables local bluetooh respectively.

In this manner you can pair your bluetooth keyboard and mouse with both your
iMac and Apple laptop, and pretty transparently have them move between both
devices. It's partly assumed that your laptop is closed / has bluetooth disabled
when it doesn't need to be paired with your bluetooth peripherals.

Typcially I use Target Display Mode when home with my work laptop and when I'm
not using TDM, I've closed my laptop and packed it up.

## Requirements

### blueutil

blueutil lets us control your bluetooth controller.

Either install from src here: http://www.frederikseiffert.de/blueutil/ or
install with brew:
```Bash
% brew install blueutil
```

## Run

```Bash
% ./targetdisplaymode.py
```

### Enter Target Display Mode

Cmd-F2 to enter Target Display Mode

TargetDisplayMonitor should detect this and turn off your bluetooth controller.

### Unplug your thunderbolt cable

TargetDispalyMonitor should detect this and reenabled your bluetooth controller.

## Run on boot

```Bash
% ./install.sh
```
## Acknowledgements

Stumbled across this blog post which got me thinking:
http://billhiggins.us/blog/2014/09/13/use-target-display-mode-with-an-imac/
