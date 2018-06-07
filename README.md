# radio-button

_**Connect a button on your raspberry pi to play radio**_

![Radio button](/button.png)

## Installation

### Configuration
Change the radio url associated to the variable radioUrl in `radio-button.py`.

### Requirements
Connect a button between GPIO 13 and GND to control the radio.

### Test
```
sudo ./radio-button.py
```

### Deamonize with systemd
Run the install script :
```
sudo ./INSTALL.sh
```

