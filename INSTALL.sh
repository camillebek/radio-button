#!/bin/sh
# Install the files and launch the deamon with systemd
# Run this command with sudo


SYSTEMCTL=$(which systemctl)
bindir=/usr/local/bin
systemdsystemetcdir=/etc/systemd/system
systemdsystemlibdir=/lib/systemd/system

# Install radio-button program file
if test ! -e "${bindir}/radio-button"; then :
	cp radio-button.py ${bindir}/radio-button
	echo "radio-button created"
else
	echo "radio-button already exists"
fi


# Install systemd service file if applicable for this system
if test ! -e "${systemdsystemlibdir}/radio-button.service"; then :
	cp radio-button.service ${systemdsystemlibdir}
	systemctl daemon-reload
	echo "radio-button.service created"
else
	echo "radio-button.service already exists"
fi
if test -e "${systemdsystemlibdir}/radio-button.service" && test ! -e "${systemdsystemetcdir}/multi-user.target.wants/radio-button.service"; then :
	${SYSTEMCTL} enable radio-button.service
	echo "Service enabled"
else
	echo "Service already enabled"
fi

${SYSTEMCTL} restart radio-button.service