# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

## Update the entire database ##

import time
import frappe

import datetime
import pytz
import os

import requests
import json

# from autocount.autocount.doctype.autocount_settings import autocount_settings
from autocount.autocount.doctype import url_config

from autocount.autocount.doctype.stock_item import stock_item_list
from autocount.autocount.doctype.stock_group import stock_group_list
from autocount.autocount.doctype.stock_take import stock_take_list
from autocount.autocount.doctype.stock_adjustment import stock_adjustment_list
from autocount.autocount.doctype.stock_issue import stock_issue_list
from autocount.autocount.doctype.stock_receive import stock_receive_list
from autocount.autocount.doctype.stock_write_off import stock_write_off_list
from autocount.autocount.doctype.stock_renew_cost import stock_renew_cost_list

from autocount.autocount.doctype.debtor import debtor_list
from autocount.autocount.doctype.autocount_sales_order import autocount_sales_order_list
from autocount.autocount.doctype.autocount_quotation import autocount_quotation_list
from autocount.autocount.doctype.delivery_order import delivery_order_list
from autocount.autocount.doctype.autocount_sales_invoice import autocount_sales_invoice_list
from autocount.autocount.doctype.cash_sale import cash_sale_list
from autocount.autocount.doctype.credit_note import credit_note_list
from autocount.autocount.doctype.debit_note import debit_note_list
from autocount.autocount.doctype.cancel_so import cancel_so_list
from autocount.autocount.doctype.delivery_return import delivery_return_list

def filter_msg(results):
	# Only showing msg when there are changes (deleted, added, edited)
	# Calculate total time
	msg = ""
	time = 0
	for result in results:
		time += result["time"]
		if any([result["deleted"], result["added"], result["edited"]]):
			msg += f"\n{result}"
	if msg == "":
		msg += f"\nAll skipped"
	msg += f"\nTotal time: {time} seconds"
	return msg


@frappe.whitelist()
def update_all_tables():
	a = stock_group_list.update()
	b = stock_item_list.update()
	c = stock_take_list.update()
	d = stock_adjustment_list.update()
	e = stock_issue_list.update()
	f = stock_receive_list.update()
	g = stock_write_off_list.update()
	h = stock_renew_cost_list.update()

	i = debtor_list.update()
	j = autocount_sales_order_list.update()
	k = autocount_quotation_list.update()
	l = delivery_order_list.update()
	m = autocount_sales_invoice_list.update()
	n = cash_sale_list.update()
	o = credit_note_list.update()
	p = debit_note_list.update()
	q = cancel_so_list.update()
	r = delivery_return_list.update()

	return filter_msg([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r])
