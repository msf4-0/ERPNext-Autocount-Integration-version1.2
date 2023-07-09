// Copyright (c) 2022, Timothy Wong and contributors
// For license information, please see license.txt

const addMethod = "autocount.autocount.doctype.debtor.debtor.add";
const editMethod = "autocount.autocount.doctype.debtor.debtor.edit";

function isDebtorCodeValid(x) {
	// Format: XXX-XXXX
	return /^[a-zA-Z0-9]{3}\-[a-zA-Z0-9]{4}$/.test(x);
}

frappe.ui.form.on('Debtor', {
	btn_copy_address: function(frm) {
		frm.set_value("delivery_address_1", frm.doc.billing_address_1);
		frm.set_value("delivery_address_2", frm.doc.billing_address_2);
		frm.set_value("delivery_address_3", frm.doc.billing_address_3);
		frm.set_value("delivery_address_4", frm.doc.billing_address_4);
	},

	before_save: function(frm) {
		if (frm.is_new()) {
			console.log("new form");
			if (!isDebtorCodeValid(frm.doc.debtor_code)) {
				frappe.throw("Invalid debtor code format. It should be XXX-XXXX with only numbers or alphabets.");
				frappe.validated = false;
			}

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
});
