# Remove `/dev/ttyS*` Ports (port auto detection fix)

This plugin patches the internal method inside OctoPrint that creates a list of the serial ports in your system to
filter out `/dev/ttyS*` entries, which were added to the default port pattern in OctoPrint 1.4.0.

Install this plugin if you are running into issues with port auto detection no longer working on your instance which
worked flawlessly on earlier versions, especially if you have a Raspberry Pi camera or a touch screen installed (which
appear to add a `/dev/ttyS` port to the system at least in some cases).

This is a work around for OctoPrint 1.4.0 until a generally better port auto detection solution can be released with
1.4.1, and thus currently only works with OctoPrint 1.4.0.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/OctoPrint/OctoPrint-Remove-ttyS-Ports/archive/master.zip
