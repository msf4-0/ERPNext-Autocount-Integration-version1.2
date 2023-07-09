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

DOCTYPE = "Delivery Return"
DOCTYPE_URL_NAME = "DeliveryReturn"
ERP_PRIMARY_KEY = "doc_no"
AUTOCOUNT_PRIMARY_KEY = "DocNo"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{DOCTYPE_URL_NAME}/getDetail"


def match_erp_with_api_json(data):
	child_items = data["ChildItems"]
	new_child_list = []
	if len(child_items) != 0:
		for child in child_items:
			x = {
			"delivery_order_no": child["FromDocNo"],
			"item_code": child["ItemCode"],
			"uom": child["UOM"],
			"quantity": child["Qty"],
			}
			new_child_list.append(x)

	output_data = {
	"doc_no" : data.get("DocNo"),
	"debtor_code" : data.get("DebtorCode"),
	"date" : data.get("DocDate"),
	"chosen_table" : new_child_list
	}
	return output_data

@frappe.whitelist()
def update():
	controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)