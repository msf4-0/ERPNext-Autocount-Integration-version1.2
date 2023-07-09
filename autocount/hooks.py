# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "autocount"
app_title = "Autocount"
app_publisher = "Timothy Wong"
app_description = "The accounting software"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "tw52@hw.ac.uk"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/autocount/css/autocount.css"
# app_include_js = "/assets/autocount/js/autocount.js"

# include js, css files in header of web template
# web_include_css = "/assets/autocount/css/autocount.css"
# web_include_js = "/assets/autocount/js/autocount.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

#stock_item_list_js = {"doctype" : "autocount/doctype/stock_item/stock_item_list.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "autocount.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "autocount.install.before_install"
# after_install = "autocount.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "autocount.notifications.get_notification_config"

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
	# "*": {
		# "on_update": "method",
		# "on_cancel": "autocount.autocount.doctype.update.cancel",
		# "on_trash": "method"
	# },
	
	# "Stock Item" :{
	# 	"on_trash": "autocount.autocount.doctype.stock_item.stock_item.delete"
	# },
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
	# "cron": {
	# 	"* * * * *": [
	# 		"autocount.autocount.doctype.update.update_entire_database",
	# 	]
	# },
	# "all": [
	# 	"autocount.autocount.doctype.update.update_entire_database"
	# ],
# 	"daily": [
# 		"autocount.tasks.daily"
# 	],
# 	"hourly": [
# 		"autocount.tasks.hourly"
# 	],
# 	"weekly": [
# 		"autocount.tasks.weekly"
# 	]
# 	"monthly": [
# 		"autocount.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "autocount.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "autocount.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "autocount.task.get_dashboard_data"
# }

