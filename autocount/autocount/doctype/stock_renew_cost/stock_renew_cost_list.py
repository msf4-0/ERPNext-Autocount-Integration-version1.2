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
from autocount.autocount.doctype.stock_item import stock_item_list
from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "Stock Renew Cost"
DOCTYPE_URL_NAME = "StockUpdateCost"
ERP_PRIMARY_KEY = "doc_no"
AUTOCOUNT_PRIMARY_KEY = "DocNo"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{DOCTYPE_URL_NAME}/getDetail"

def create_data_map(data):
	child_items = data["ChildItems"]
	new_child_list = []
	if len(child_items) != 0:
		for child in child_items:
			x = {
			"item_code": child["ItemCode"],
			"uom": child["UOM"],
			"new_cost": child["NewCost"]
			}
			new_child_list.append(x)

	output_data = {
	"doc_no" : data["DocNo"],
	"date" : data["DocDate"],
	"description" : data["Description"],
	"cost_table" : new_child_list
	}
	return output_data

@frappe.whitelist()
def update():
	controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	return controller.update_frappe("doc_no", "DocNo", create_data_map)