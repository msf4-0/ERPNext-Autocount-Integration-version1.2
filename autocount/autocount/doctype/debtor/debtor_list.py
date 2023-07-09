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

DOCTYPE = "Debtor"
DOCTYPE_URL_NAME = "Debtor"
ERP_PRIMARY_KEY = "debtor_code"
AUTOCOUNT_PRIMARY_KEY = "DebtorCode"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"


def transform_statement_type(api_json_value):
	maps = {
	"O" : "Open Item",
	"B" : "Balance Forward",
	"N" : "No Statement"
	}
	return maps[api_json_value]


def transform_aging_on(api_json_value):
	maps = {
	"I" : "Invoice Date",
	"D" : "Due Date"
	}
	return maps[api_json_value]


def match_erp_with_api_json(data):
	output_data = {
	"debtor_code" : data.get("DebtorCode"),
	"company_name" : data.get("DebtorCompanyName"),
	"billing_address_1" : data.get("DebtorAddress1"),
	"billing_address_2" : data.get("DebtorAddress2"),
	"billing_address_3" : data.get("DebtorAddress3"),
	"billing_address_4" : data.get("DebtorAddress4"),
	"delivery_address_1" : data.get("DebtorDeliverAddress1"),
	"delivery_address_2" : data.get("DebtorDeliverAddress2"),
	"delivery_address_3" : data.get("DebtorDeliverAddress3"),
	"delivery_address_4" : data.get("DebtorDeliverAddress4"),
	"phone" : data.get("DebtorPhone1"),
	"mobile" : data.get("DebtorMobile"),
	"fax" : data.get("DebtorFax1"),
	"email_address" : data.get("DebtorEmailAddress"),
	"attention" : data.get("DebtorAttention"),
	"business_nature" : data.get("DebtorNatureOfBusiness"),
	"credit_term" : data.get("DebtorDisplayTerm"),
	"statement_type" : transform_statement_type(data.get("DebtorStatementType")),
	"aging_on" : transform_aging_on(data.get("DebtorAgingOn")),
	"credit_limit" : data.get("DebtorCreditLimit"),
	"overdue_limit" : data.get("DebtorOverdueLimit")
	}
	return output_data

@frappe.whitelist()
def update():
	controller = ListController(DOCTYPE, URL_GET_ALL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)