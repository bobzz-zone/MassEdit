# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Mass Edit",
			"color": "grey",
			"icon": "octicon .octicon-pencil",
			"type": "module",
			"label": _("Mass Edit")
		}
	]
