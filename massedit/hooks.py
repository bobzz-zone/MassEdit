# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "massedit"
app_title = "Mass Edit"
app_publisher = "bobzz"
app_description = "Mass Edit is a Bulk Edit"
app_icon = ".octicon-pencil"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/massedit/css/massedit.css"
# app_include_js = "/assets/massedit/js/massedit.js"

# include js, css files in header of web template
# web_include_css = "/assets/massedit/css/massedit.css"
# web_include_js = "/assets/massedit/js/massedit.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "massedit.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "massedit.install.before_install"
# after_install = "massedit.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "massedit.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"massedit.tasks.all"
# 	],
# 	"daily": [
# 		"massedit.tasks.daily"
# 	],
# 	"hourly": [
# 		"massedit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"massedit.tasks.weekly"
# 	]
# 	"monthly": [
# 		"massedit.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "massedit.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "massedit.event.get_events"
# }

