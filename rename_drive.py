# Rename this file to boot.py and copy to the Circuit Python drive
import storage

storage.remount("/", readonly=False)

m = storage.getmount("/")
# LABEL MUST BE <= 11 CHARS
m.label = "PING_CLOCK"

storage.remount("/", readonly=True)

storage.enable_usb_drive()

