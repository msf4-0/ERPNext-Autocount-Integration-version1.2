# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json

from autocount.autocount.doctype.form_controller import FormController
from autocount.autocount.doctype.utils import convert_date_string

DOCTYPE = "Stock Item"
DOCTYPE_URL_NAME = "StockItem"

controller = FormController(DOCTYPE_URL_NAME)

class StockItem(Document):
	def on_trash(self):
		item_code = self.name
		controller.delete_on_autocount(item_code)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)
	submitted_data = {
		"itemCode" : data.get("item_code"), 
		"description" : data.get("description"),
		"uom" : data.get("uom"),
		"unitCost" : data.get("unit_cost"),
		"price" : data.get("price"),
		"costingMethod" : data.get("costing_method")[0],	# Only get the first char (costing code)
		"itemGroup" : data.get("item_group"),
		"leadTime" : data.get("lead_time"),
		"dutyRate" : data.get("duty_rate"),
		"taxType" : data.get("tax_type"),
		"purchaseTaxType" : data.get("purchase_tax_type"),
		}
	return submitted_data

@frappe.whitelist()
def add(doc):
	submitted_data = parse_doc(doc)
	return controller.add_to_autocount(submitted_data)

@frappe.whitelist()
def edit(doc):
	submitted_data = parse_doc(doc)
	return controller.edit_on_autocount(submitted_data)