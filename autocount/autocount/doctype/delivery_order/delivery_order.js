// Copyright (c) 2022, Timothy Wong and contributors
// For license information, please see license.txt

const addMethod = "autocount.autocount.doctype.delivery_order.delivery_order.add";
const editMethod = "autocount.autocount.doctype.delivery_order.delivery_order.edit";

function isUndefinedOrEmpty(x) {
	return x === undefined || x === "";
}

function updateSubtotal(cdt, cdn) {
	var item = locals[cdt][cdn]; 
	if (!isUndefinedOrEmpty(item.quantity) && !isUndefinedOrEmpty(item.unit_price) 
		&& !isUndefinedOrEmpty(item.discount)) {
		var subtotal = (item.quantity * item.unit_price) - item.discount;
		frappe.model.set_value(cdt, cdn, "subtotal", subtotal);
	}
}

function updateGrandTotal(frm) {
	var total = 0;
	for (var i = 0; i < frm.doc.item_table.length; i++) {
		total += frm.doc.item_table[i].subtotal;
	}
	total = parseFloat(total).toFixed(2);
	frm.set_value("total", total);
}

frappe.ui.form.on('Delivery Order', {
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


frappe.ui.form.on('Sales Child Table', {
	item_table_add: function(frm, cdt, cdn) {
		updateSubtotal(cdt, cdn);
	},

	item_table_remove: function(frm, cdt, cdn) {
		updateGrandTotal(frm);
	},

	item_code: function(frm, cdt, cdn) {
		// Trigger when item_code in child table has changed
		var item = locals[cdt][cdn]; 
		var item_code = item.item_code;

		if (item_code) {
			frappe.call({
				method: "frappe.client.get",
				args:{
				    doctype: "Stock Item",
					name: item_code
				},
				callback:function(r){
					var uom = r.message.uom;
					var unitPrice = r.message.unit_cost;

					frappe.model.set_value(cdt, cdn, "uom", uom);
					frappe.model.set_value(cdt, cdn, "quantity", 1);
					frappe.model.set_value(cdt, cdn, "unit_price", unitPrice);
					frappe.model.set_value(cdt, cdn, "discount", 0);

					updateSubtotal(cdt, cdn);
				},
			});
		} else {
			frappe.model.set_value(cdt, cdn, "uom", undefined);
			frappe.model.set_value(cdt, cdn, "quantity", 1);
			frappe.model.set_value(cdt, cdn, "unit_price", 0);
			frappe.model.set_value(cdt, cdn, "discount", 0);
			updateSubtotal(cdt, cdn);
		}


	},

	unit_price: function(frm, cdt, cdn) {
		var item = locals[cdt][cdn];

		if (isUndefinedOrEmpty(item.unit_price)) {
			frappe.model.set_value(cdt, cdn, "unit_price", 0);
		}

		if (item.unit_price < 0) {
			frappe.msgprint("Unit price cannot be negative value.");
			frappe.model.set_value(cdt, cdn, "unit_price", 0);
		}

		updateSubtotal(cdt, cdn);
		
	},

	quantity: function(frm, cdt, cdn) {
		var item = locals[cdt][cdn]; 
		//console.log(item.quantity);
		
		if (isUndefinedOrEmpty(item.quantity)) {
			frappe.msgprint("Quantity cannot be zero or empty. Remove the row if not used.");
			frappe.model.set_value(cdt, cdn, "quantity", 1);
		}

		if (item.quantity < 0) {
			frappe.msgprint("Quantity cannot be negative value.");
			frappe.model.set_value(cdt, cdn, "quantity", 1);
		}

		updateSubtotal(cdt, cdn);
	},

	discount: function(frm, cdt, cdn) {
		var item = locals[cdt][cdn]; 

		if (isUndefinedOrEmpty(item.discount)) {
			frappe.model.set_value(cdt, cdn, "discount", 0);
		}

		if (item.discount < 0) {
			frappe.msgprint("Discount cannot be negative value.");
			frappe.model.set_value(cdt, cdn, "discount", 0);
		}

		updateSubtotal(cdt, cdn);
	},

	subtotal: function(frm, cdt, cdn) {
		var item = locals[cdt][cdn]; 

		if (item.subtotal < 0) {
			frappe.msgprint("Subtotal cannot be negative value. \
				Please adjust the discount."); 	// Means discount is too large
			frappe.model.set_value(cdt, cdn, "discount", 0);		// Reset discount to 0
		}

		updateGrandTotal(frm);
	},
	
});