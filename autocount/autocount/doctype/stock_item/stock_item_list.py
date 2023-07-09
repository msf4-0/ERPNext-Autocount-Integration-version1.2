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

DOCTYPE = "Stock Item"
DOCTYPE_URL_NAME = "StockItem"
ERP_PRIMARY_KEY = "item_code"
AUTOCOUNT_PRIMARY_KEY = "ItemCode"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"

def add_costing_method_suffix(code):
	desc_dict = { "0": "Fixed Cost", "1": "Weighted Average", "2": "FIFO", "3":"LIFO" }
	return f"{code} - {desc_dict.get(str(code))}"

def str_or_none(x):
	if x is None:
		return None
	return str("{:.2f}".format(x))

def create_data_map(data):
	output_data = {
	"item_code" : data.get("ItemCode"), 
	"description" : data.get("Description"), 
	"uom" : data.get("BaseUOM"),
	"unit_cost" : str_or_none(data.get("Cost")),	## Bcoz some values are null, unit_cost and price in ERPNext 
	"price" : str_or_none(data.get("Price")),		## are stored as str instead of float.
	"costing_method" : add_costing_method_suffix(data.get("CostingMethod")),
	"item_group" : data.get("ItemGroup"),
	"lead_time" : data.get("LeadTime"),
	"duty_rate" : data.get("DutyRate"),
	"tax_type" : data.get("Taxtype"),
	"purchase_tax_type" : data.get("PurchaseTaxType"),
	}
	return output_data

@frappe.whitelist()
def update():
	# controller = ListController(DOCTYPE, URL_GET_ALL)
	# return controller.update_frappe("item_code", "ItemCode", create_data_map)
	controller = ListController(DOCTYPE, URL_GET_ALL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, create_data_map)