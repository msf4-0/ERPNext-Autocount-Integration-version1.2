# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

DEFAULT_IP_ADDRESS = "host.docker.internal"
DEFAULT_PORT = "8888"

@frappe.whitelist()
def get_socket_address():
	data = frappe.db.get("Autocount Settings")

	if not data:
		return f"http://{DEFAULT_IP_ADDRESS}:{DEFAULT_PORT}"

	ip_address = data.get("ip_address")
	port = data.get("port")

	if not ip_address:
		ip_address = DEFAULT_IP_ADDRESS
		frappe.db.set_value("Autocount Settings", "Autocount Settings", "ip_address", DEFAULT_IP_ADDRESS)
		frappe.db.commit()
		
	if not port:
		port = DEFAULT_PORT
		frappe.db.set_value("Autocount Settings", "Autocount Settings", "port", DEFAULT_PORT)
		frappe.db.commit()

	return f"http://{ip_address}:{port}"


	
