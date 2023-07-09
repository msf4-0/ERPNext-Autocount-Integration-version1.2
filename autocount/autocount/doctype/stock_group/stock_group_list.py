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

DOCTYPE = "Stock Group"
DOCTYPE_URL_NAME = "StockGroup"
ERP_PRIMARY_KEY = "item_group"
AUTOCOUNT_PRIMARY_KEY = "ItemGroup"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{DOCTYPE_URL_NAME}/getDetail"

def get_suffix(code):
	codes_dict = {
	"150-0000" : "RETAINED EARNING",
	"151-0000" : "RESERVES",
	"200-0000" : "FIXED ASSETS",
	"200-2005" : "ACCUM. DEPRN. - FURNITURES & FITTINGS",
	"200-3000" : "OFFICE EQUIPMENT",
	"200-3005" : "ACCUM. DEPRN. - OFFICE EQUIPMENT",
	"200-4000" : "MOTOR VEHICLES",
	"200-4005" : "ACCUM. DEPRN. - MOTOR VEHICLES",
	"210-0000" : "GOODWILL",
	"305-0000" : "OTHER DEBTORS",
	"340-0000" : "DEPOSIT & PREPAYMENT",
	"405-0000" : "OTHER CREDITORS",
	"410-0000" : "ACCRUALS",
	"420-0000" : "HIRE PURCHASE CREDITOR",
	"420-1000" : "HIRE PURCHASE INTEREST SUSPENSE",
	"430-0000" : "SALES TAX",
	"440-0000" : "DEPOSIT RECEIVED",
	"490-0000" : "TEMPORARY ACCOUNT FOR CONTRA",
	"500-0000" : "SALES",
	"500-1000" : "CASH SALES",
	"510-0000" : "RETURN INWARDS",
	"520-0000" : "DISCOUNT ALLOWED",
	"530-0000" : "GAIN ON FOREIGN EXCHANGE",
	"540-0000" : "DISCOUNT RECEIVED",
	"610-0000" : "PURCHASES",
	"612-0000" : "PURCHASES RETURN",
	"615-0000" : "CARRIAGE INWARDS",
	"901-0000" : "ADVERTISEMENT",
	"902-0000" : "BANK CHARGES",
	"903-0000" : "DEPRECIATION OF FIXED ASSETS",
	"904-0000" : "SALARIES",
	"905-0000" : "TRAVELLING EXPENSES",
	"906-0000" : "UPKEEP OF MOTOR VEHICLE",
	"907-0000" : "WATER & ELECTRICITY",
	"908-0000" : "LOSS ON FOREIGN EXCHANGE",
	"909-0000" : "TELEPHONE CHARGES",
	"910-0000" : "PRINTING & STATIONERY",
	"911-0000" : "INTEREST EXPENSE",
	"912-0000" : "POSTAGES & STAMPS",
	"913-0000" : "COMMISSION & ALLOWANCES",
	"914-0000" : "OFFICE RENTAL",
	"915-0000" : "GENERAL EXPENSES",
	"950-0000" : "TAXATION"
	}
	return codes_dict.get(code)

def add_suffix(x):
	return f"{x} {get_suffix(x)}"

def create_data_map(data):
	output_data = {
	"item_group" : data["ItemGroup"], 
	"description" : data["ItemGroupDescription"], 
	"sales_code" : add_suffix(data["SalesCode"]),
	"cash_sales_code" : add_suffix(data["CashSalesCode"]),
	"sales_return_code" : add_suffix(data["SalesReturnCode"]),
	"sales_discount_code" : add_suffix(data["SalesDiscountCode"]),
	"purchase_code" : add_suffix(data["PurchaseCode"]),
	"cash_purchase_code" : add_suffix(data["CashPurchaseCode"]),
	"purchase_return_code" : add_suffix(data["PurchaseReturnCode"]),
	"purchase_discount_code" : add_suffix(data["PurchaseDiscountCode"]),
	"balance_stock_code" : "330-0000 STOCK"		
	}
	return output_data

@frappe.whitelist()
def update():
	controller = ListController(DOCTYPE, URL_GET_ALL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, create_data_map)