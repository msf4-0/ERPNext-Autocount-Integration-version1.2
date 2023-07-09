// Copyright (c) 2022, Timothy Wong and contributors
// For license information, please see license.txt

const addMethod = "autocount.autocount.doctype.stock_take.stock_take.add";
const editMethod = "autocount.autocount.doctype.stock_take.stock_take.edit";

frappe.ui.form.on('Stock Take', {
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

});


frappe.ui.form.on('Item Child Table', {
	item_code: function(frm, cdt, cdn) {
		// Trigger when item_code in child table has changed
		var item = locals[cdt][cdn]; 
		var item_code = item.item_code;

		// MUST use frappe.call instead of frm.call, 
		// otherwise 'description' field will be populated unexpectedly
		if (item_code) {
			console.log(`item code: ${item_code}`);
			frappe.call({
				method: "frappe.client.get",
				args:{
				    doctype: "Stock Item",
					name: item_code
				},
				callback:function(r){
					var uom = r.message.uom;
					frappe.model.set_value(cdt, cdn, "uom", uom);
				},
			});
		} else {
			frappe.model.set_value(cdt, cdn, "uom", undefined);
		}
	},
	
});
