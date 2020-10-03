# powerpanel-ups-api-docker
CyberPower PowerPanel simple API


## Run it

It is required to pass the usb device that is connected to your UPS to the docker container.  This example is running in vCenter with Host USB Passthru enabled.  The USB Device connected is `/dev/bus/usb/002/004`.  You can find your USB device by typing `lsusb`.  You can see an example `lsusb` output here:

```
lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 005: ID 0658:0200 Sigma Designs, Inc. 
Bus 002 Device 004: ID 0764:0501 Cyber Power System, Inc. CP1500 AVR UPS
Bus 002 Device 003: ID 0e0f:0002 VMware, Inc. Virtual USB Hub
Bus 002 Device 002: ID 0e0f:0003 VMware, Inc. Virtual Mouse
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
```

*Docker Command* `docker run --name ups-api --privileged -d --device=/dev/bus/usb/002/004 -p 5002:5002 tvories/powerpanel-ups-api`