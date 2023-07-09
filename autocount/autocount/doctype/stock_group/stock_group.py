# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json

from autocount.autocount.doctype.form_controller import FormController
from autocount.autocount.doctype.utils import convert_date_string

DOCTYPE = "Stock Group"
DOCTYPE_URL_NAME = "StockGroup"

controller = FormController(DOCTYPE_URL_NAME)

class StockGroup(Document):
	def on_trash(self):
		item_group = self.name
		controller.delete_on_autocount(item_group)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)
	submitted_data = {
	"itemGroup" : data.get("item_group"), 
	"description" : data.get("description"),
	"stockCodes" : 
		{
		"SalesCode" : data.get("sales_code").split(" ")[0],
		"CashSalesCode" : data.get("cash_sales_code").split(" ")[0],
		"SalesReturnCode" : data.get("sales_return_code").split(" ")[0],
		"SalesDiscountCode" : data.get("sales_discount_code").split(" ")[0],
		"PurchaseCode" : data.get("purchase_code").split(" ")[0],
		"CashPurchaseCode" : data.get("cash_purchase_code").split(" ")[0],
		"PurchaseReturnCode" : data.get("purchase_return_code").split(" ")[0],
		"PurchaseDiscountCode" : data.get("purchase_discount_code").split(" ")[0],
		"BalanceStockCode" : data.get("balance_stock_code").split(" ")[0]
		}
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
