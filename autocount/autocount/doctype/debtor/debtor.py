# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json

from autocount.autocount.doctype.form_controller import FormController
from autocount.autocount.doctype.utils import convert_date_string

DOCTYPE = "Debtor"
DOCTYPE_URL_NAME = "Debtor"

controller = FormController(DOCTYPE_URL_NAME)

class Debtor(Document):
	def on_trash(self):
		debtor_code = self.name
		controller.delete_on_autocount(debtor_code)


@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)
	# Matches API key with ERPNext form key
	submitted_data = {
		"debtorCode" : data.get("debtor_code"), 
		"companyName" : data.get("company_name"),
		"billingAddress1" : data.get("billing_address_1"),
		"billingAddress2" : data.get("billing_address_2"),
		"billingAddress3" : data.get("billing_address_3"),
		"billingAddress4" : data.get("billing_address_4"),
		"deliveryAddress1" : data.get("delivery_address_1"),
		"deliveryAddress2" : data.get("delivery_address_2"),
		"deliveryAddress3" : data.get("delivery_address_3"),
		"deliveryAddress4" : data.get("delivery_address_4"),
		"phone" : data.get("phone"),
		"mobile" : data.get("mobile"),
		"fax" : data.get("fax"),
		"emailAddress" : data.get("email_address"),
		"attention" : data.get("attention"),
		"businessNature" : data.get("business_nature"),
		"creditTerm" : data.get("credit_term"),
		"statementType" : data.get("statement_type")[0],
		"agingOn" : data.get("aging_on")[0],
		"creditLimit" : data.get("credit_limit"),
		"overdueLimit" : data.get("overdue_limit"),
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
