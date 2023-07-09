// Copyright (c) 2022, Timothy Wong and contributors
// For license information, please see license.txt

const addMethod = "autocount.autocount.doctype.stock_group.stock_group.add";
const editMethod = "autocount.autocount.doctype.stock_group.stock_group.edit";

frappe.ui.form.on('Stock Group', {
	before_load: function(frm) {
		var df1 = frappe.meta.get_docfield("Stock Group", "sales_code", frm.doc.name);
		var df2 = frappe.meta.get_docfield("Stock Group", "cash_sales_code", frm.doc.name);
		var df3 = frappe.meta.get_docfield("Stock Group", "sales_return_code", frm.doc.name);
		var df4 = frappe.meta.get_docfield("Stock Group", "sales_discount_code", frm.doc.name);
		var df5 = frappe.meta.get_docfield("Stock Group", "purchase_code", frm.doc.name);
		var df6 = frappe.meta.get_docfield("Stock Group", "cash_purchase_code", frm.doc.name);
		var df7 = frappe.meta.get_docfield("Stock Group", "purchase_return_code", frm.doc.name);
		var df8 = frappe.meta.get_docfield("Stock Group", "purchase_discount_code", frm.doc.name);
		var df9 = frappe.meta.get_docfield("Stock Group", "balance_stock_code", frm.doc.name);

		var codes_list = [
			"150-0000 RETAINED EARNING",
			"151-0000 RESERVES",
			"200-0000 FIXED ASSETS",
			"200-2005 ACCUM. DEPRN. - FURNITURES & FITTINGS",
			"200-3000 OFFICE EQUIPMENT",
			"200-3005 ACCUM. DEPRN. - OFFICE EQUIPMENT",
			"200-4000 MOTOR VEHICLES",
			"200-4005 ACCUM. DEPRN. - MOTOR VEHICLES",
			"210-0000 GOODWILL",
			"305-0000 OTHER DEBTORS",
			"340-0000 DEPOSIT & PREPAYMENT",
			"405-0000 OTHER CREDITORS",
			"410-0000 ACCRUALS",
			"420-0000 HIRE PURCHASE CREDITOR",
			"420-1000 HIRE PURCHASE INTEREST SUSPENSE",
			"430-0000 SALES TAX",
			"440-0000 DEPOSIT RECEIVED",
			"490-0000 TEMPORARY ACCOUNT FOR CONTRA",
			"500-0000 SALES",
			"500-1000 CASH SALES",
			"510-0000 RETURN INWARDS",
			"520-0000 DISCOUNT ALLOWED",
			"530-0000 GAIN ON FOREIGN EXCHANGE",
			"540-0000 DISCOUNT RECEIVED",
			"610-0000 PURCHASES",
			"612-0000 PURCHASES RETURN",
			"615-0000 CARRIAGE INWARDS",
			"901-0000 ADVERTISEMENT",
			"902-0000 BANK CHARGES",
			"903-0000 DEPRECIATION OF FIXED ASSETS",
			"904-0000 SALARIES",
			"905-0000 TRAVELLING EXPENSES",
			"906-0000 UPKEEP OF MOTOR VEHICLE",
			"907-0000 WATER & ELECTRICITY",
			"908-0000 LOSS ON FOREIGN EXCHANGE",
			"909-0000 TELEPHONE CHARGES",
			"910-0000 PRINTING & STATIONERY",
			"911-0000 INTEREST EXPENSE",
			"912-0000 POSTAGES & STAMPS",
			"913-0000 COMMISSION & ALLOWANCES",
			"914-0000 OFFICE RENTAL",
			"915-0000 GENERAL EXPENSES",
			"950-0000 TAXATION"
		];

		df1.options = codes_list;
		df2.options = codes_list;
		df3.options = codes_list;
		df4.options = codes_list;
		df5.options = codes_list;
		df6.options = codes_list;
		df7.options = codes_list;
		df8.options = codes_list;
		df9.options = ["330-0000 STOCK"];

	},


	before_save: function(frm) {
		if (frm.is_new()) {
			console.log("new form");
		 	frm.call({
				method: addMethod,
				args:{
				    doc: frm.doc
				},
				freeze: true,
				callback: function(r) {
					if (!r.exc) {
						console.log("Added successfully");	
					} 
					console.log(r.message);
				},
				error: function(r) {
					console.log("Added failed");
					frappe.validated = false;
				}
			})
		} else {
			console.log("edit form");
			frm.call({
				method: editMethod,
				args:{
				    doc: frm.doc
				},
				freeze: true,
				callback: function(r) {
					if (!r.exc) {
						console.log("Edited successfully");
					} 
					console.log(r.message);
				},
				error: function(r) {
					console.log("Edited failed");
					frappe.validated = false;
				}
			}) 
			
		}
	},


	btn_load_default: function(frm) {
		frm.set_value("sales_code", "500-0000 SALES");
		frm.set_value("cash_sales_code", "500-1000 CASH SALES");
		frm.set_value("sales_return_code", "510-0000 RETURN INWARDS");
		frm.set_value("sales_discount_code", "520-0000 DISCOUNT ALLOWED");
		frm.set_value("purchase_code", "610-0000 PURCHASES");
		frm.set_value("cash_purchase_code", "610-0000 PURCHASES");
		frm.set_value("purchase_return_code", "612-0000 PURCHASES RETURN");
		frm.set_value("purchase_discount_code", "610-0000 PURCHASES");
		frm.set_value("balance_stock_code", "330-0000 STOCK");
	},


});
