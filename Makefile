PREFIX=/usr
SYSCONFDIR=/etc

INITCTL:=$(shell which initctl)
SYSTEMCTL:=$(shell which systemctl)

install:
	# Install systemd service file if applicable for this system
	if test -x "$(SYSTEMCTL)" && test -d "$(SYSCONFDIR)/systemd/system"; then cp radio-button.systemd $(SYSCONFDIR)/systemd/system/radio-button.service && $(SYSTEMCTL) daemon-reload; fi
	if test -e "$(SYSCONFDIR)/systemd/system/radio-button.service" && test ! -e "$(SYSCONFDIR)/systemd/system/multi-user.target.wants/radio-button.service"; then $(SYSTEMCTL) enable radio-button.service; fi
