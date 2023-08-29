## AAG Cloud Watcher daemon

`cloudwatcherd` wraps an AAG CloudWatcher attached via a USB-RS232 or Ethernet-RS232 adaptor and
makes the latest measurement available for other services via Pyro.

`cloudwatcher` is a commandline utility that reports the latest data from the daemon.

### Configuration

Configuration is read from json files that are installed by default to `/etc/cloudwatcherd`.
A configuration file is specified when launching the dome server, and the `cloudwatcher` frontend will search this location when launched.

```python
{
  "daemon": "observatory_cloudwatcher", # Run the server as this daemon. Daemon types are registered in `warwick.observatory.common.daemons`.
  "log_name": "cloudwatcherd", # The name to use when writing messages to the observatory log.
  "serial_port": "/dev/cloudwatcher", # Serial FIFO for communicating with the device
  "serial_baud": 9600, # Serial baud rate
  "serial_timeout": 5, # Serial comms timeout
}
```

The FIFO device names are defined in the .rules files installed through the `-cloudwatcher-data` rpm packages.
If the physical serial port or USB adaptors change these should be updated to match.

### Initial Installation

The automated packaging scripts will push 5 RPM packages to the observatory package repository:

| Package                          | Description                                                                |
|----------------------------------|----------------------------------------------------------------------------|
| rockit-cloudwatcher-server       | Contains the `cloudwatcherd` server and systemd service file.              |
| rockit-cloudwatcher-client       | Contains the `cloudwatcher` commandline utility.                           |
| python3-rockit-cloudwatcher      | Contains the python module with shared code.                               |
| rockit-cloudwatcher-data-lapalma | Contains the json configuration and udev rules for the La Palma unit.      |
| rockit-cloudwatcher-data-warwick | Contains the json configuration and udev rules for the Windmill Hill unit. |

Alternatively, perform a local installation using `sudo make install`.

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now cloudwatcherd@<config>
```

where `config` is the name of the json file for the appropriate station.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `warwick.observatory.common.daemons` for the daemon specified in the config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart cloudwatcherd@<config>
```

### Testing Locally

The server and client can be run directly from a git clone:
```
./cloudwatcherd config/halfmetre.json
CLOUDWATCHERD_CONFIG_PATH=./config/halfmetre.json ./cloudwatcher status
```
