# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json
from autocount.autocount.doctype.form_controller import FormController
from autocount.autocount.doctype.utils import convert_date_string

DOCTYPE = "Stock Receive"
DOCTYPE_URL_NAME = "StockReceive"

controller = FormController(DOCTYPE_URL_NAME)

class StockReceive(Document):
	def on_trash(self):
		doc_no = self.name
		controller.delete_on_autocount(doc_no)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)
	new_date = convert_date_string(data.get("date"))
	detail_list = []

	if data.get("item_table") is not None:
		for item in data.get("item_table"):
			detail = {
			"itemCode" : item.get("item_code"),
			"uom" : item.get("uom"),
			"quantity" : str(item.get("quantity")),
			"unitCost" : str(item.get("unit_cost"))
			}
			detail_list.append(detail)

	submitted_data = {
	"docNo" : data.get("doc_no"), 
	"dateString" : new_date,
	"description" : data.get("description"),
	"refDocNo" : data.get("ref_doc_no"),
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
