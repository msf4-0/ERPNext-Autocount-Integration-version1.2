# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time
from autocount.autocount.doctype.list_controller import ListController
# from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "Autocount Quotation"
DOCTYPE_URL_NAME = "Quotation"
ERP_PRIMARY_KEY = "doc_no"
AUTOCOUNT_PRIMARY_KEY = "DocNo"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{DOCTYPE_URL_NAME}/getDetail"

def transform_discount(api_json_discount):
	if not api_json_discount:
		return 0
	return float(api_json_discount)

def transform_total(api_json_discount):
	# ERPNext total is str, but Autocount is float
	# Transform float to str to match ERPNext
	if api_json_discount is None:
		return None
	return str(api_json_discount)


def match_erp_with_api_json(data):
	child_items = data["ChildItems"]
	new_child_list = []
	if len(child_items) != 0:
		for child in child_items:
			x = {
			"item_code": child["ItemCode"],
			"uom": child["UOM"],
			"quantity": child["Qty"],
			"unit_price": child["UnitPrice"],
			"discount": transform_discount(child["Discount"])
			}
			new_child_list.append(x)

	output_data = {
	"doc_no" : data.get("DocNo"),
	"debtor_code" : data.get("DebtorCode"),
	"date" : data.get("DocDate"),
	"ship_info" : data.get("ShipInfo"),
	"credit_term" : data.get("DisplayTerm"),
	"delivery_term" : data.get("DeliveryTerm"),
	"payment_term" : data.get("PaymentTerm"),
	"validity" : data.get("Validity"),
	"your_ref" : data.get("YourRef"),
	"cc" : data.get("CC"),
	"total" : transform_total(data.get("Total")),
	"item_table" : new_child_list
	}
	return output_data

@frappe.whitelist()
def update():
	controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)