# coding=utf-8
from __future__ import absolute_import, unicode_literals, division

import logging

import octoprint.plugin

BROKEN_VERSION = "1.4.0"
FIXED_VERSION = "1.4.1"

class RemoveTtySPortsPlugin(octoprint.plugin.OctoPrintPlugin):

	def __init__(self):
		self._monkey_patch_serial_ports()

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			remove_ttys_ports=dict(
				displayName=self._plugin_name,
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="OctoPrint",
				repo="OctoPrint-Remove-ttyS-Ports",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/OctoPrint/OctoPrint-Remove-ttyS-Ports/archive/{target_version}.zip"
			)
		)

	##~~ monkey patcher

	def _monkey_patch_serial_ports(self):
		import octoprint.util.comm

		original_serial_list = octoprint.util.comm.serialList

		def patched_serial_list():
			result = original_serial_list()
			return list(filter(lambda x: not x.startswith("/dev/ttyS"),
			                   result))

		octoprint.util.comm.serialList = patched_serial_list
		logging.getLogger(__name__).info("Patched octoprint.util.comm.serialList to filter out /dev/ttyS* ports")


__plugin_name__ = "Remove /dev/ttyS* ports"
__plugin_pythoncompat__ = ">=2.7,<4" # python 2 and 3

def __plugin_check__():
	from octoprint.util.version import is_octoprint_compatible
	compatible = is_octoprint_compatible(">={},<{}".format(BROKEN_VERSION, FIXED_VERSION))
	if not compatible:
		logging.getLogger(__name__).info("Plugin is not needed in OctoPrint versions < 1.4.0 or >= 1.4.1")
	return compatible

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = RemoveTtySPortsPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

