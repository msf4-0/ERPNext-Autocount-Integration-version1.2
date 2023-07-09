from __future__ import unicode_literals
from frappe import _
def get_data():
    config = [
        {
            "label": _("Stock"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Stock Item",
                    "label": "Stock Item",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Stock Group",
                    "label": "Stock Group",
                    "onboard": 2,
                },
                {
                    "type": "doctype",
                    "name": "Stock Take",
                    "label": "Stock Take",
                    "onboard": 3,
                },
                {
                    "type": "doctype",
                    "name": "Stock Adjustment",
                    "label": "Stock Adjustment",
                    "onboard": 4,
                },
                {
                    "type": "doctype",
                    "name": "Stock Issue",
                    "label": "Stock Issue",
                    "onboard": 5,
                },
                {
                    "type": "doctype",
                    "name": "Stock Receive",
                    "label": "Stock Receive",
                    "onboard": 6,
                },
                {
                    "type": "doctype",
                    "name": "Stock Write Off",
                    "label": "Stock Write Off",
                    "onboard": 7,
                },
                {
                    "type": "doctype",
                    "name": "Stock Renew Cost",
                    "label": "Stock Renew Cost",
                    "onboard": 8,
                },
            ]
        },
        {
            "label": _("Sales"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Debtor",
                    "label": "Debtor",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Autocount Sales Order",
                    "label": "Sales Order",
                    "onboard": 2,
                },
                {
                    "type": "doctype",
                    "name": "Autocount Quotation",
                    "label": "Quotation",
                    "onboard": 3,
                },
                {
                    "type": "doctype",
                    "name": "Delivery Order",
                    "label": "Delivery Order",
                    "onboard": 4,
                },
                {
                    "type": "doctype",
                    "name": "Autocount Sales Invoice",
                    "label": "Sales Invoice",
                    "onboard": 5,
                },
                {
                    "type": "doctype",
                    "name": "Cancel SO",
                    "label": "Cancel SO",
                    "onboard": 6,
                },
                {
                    "type": "doctype",
                    "name": "Delivery Return",
                    "label": "Delivery Return",
                    "onboard": 7
                },
                {
                    "type": "doctype",
                    "name": "Cash Sale",
                    "label": "Cash Sale",
                    "onboard": 8
                },
                {
                    "type": "doctype",
                    "name": "Credit Note",
                    "label": "Credit Note",
                    "onboard": 9
                },
                {
                    "type": "doctype",
                    "name": "Debit Note",
                    "label": "Debit Note",
                    "onboard": 10
                },
            ]

        },
        {
            "label": _("Settings"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Autocount Settings",
                    "label": "Autocount Settings",
                    "onboard": 1,
                },
            ]

        }

    ]
    return config

