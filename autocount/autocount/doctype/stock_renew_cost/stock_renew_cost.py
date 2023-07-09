# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json
from autocount.autocount.doctype.form_controller import FormController
from autocount.autocount.doctype.utils import convert_date_string

DOCTYPE = "Stock Renew Cost"			# Doctype name cannot contains keyword 'Update'
DOCTYPE_URL_NAME = "StockUpdateCost"	# REST API URL name different from doctype

controller = FormController(DOCTYPE_URL_NAME)

class StockRenewCost(Document):
	def on_trash(self):
		doc_no = self.name
		controller.delete_on_autocount(doc_no)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)
	new_date = convert_date_string(data.get("date"))
	detail_list = []

	if data.get("cost_table") is not None:
		for item in data.get("cost_table"):
			detail = {
			"itemCode" : item.get("item_code"),
			"uom" : item.get("uom"),
			"newCost" : str(item.get("new_cost"))
			}
			detail_list.append(detail)

	submitted_data = {
	"docNo" : data.get("doc_no"), 
	"dateString" : new_date,
	"description" : data.get("description"),
	"detailList" : detail_list
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
