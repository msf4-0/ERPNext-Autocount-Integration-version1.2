// Copyright (c) 2022, Timothy Wong and contributors
// For license information, please see license.txt

const addMethod = "autocount.autocount.doctype.stock_item.stock_item.add";
const editMethod = "autocount.autocount.doctype.stock_item.stock_item.edit";

function isValidNumber(x) {
	return /^\d+(\.\d{1,2})?$/.test(x);
}

function isValidNumberOrEmpty(x) {
	return isValidNumber(x) || !x;
}

function isPriceGreaterThanCost(price, unitCost) {
	if (!price || !unitCost) {
		return true;
	}
	return parseFloat(price) >= parseFloat(unitCost);
}

function toTwoDecimalPlaces(x) {
	if (!x) {
		return x;
	}
	return parseFloat(x).toFixed(2);	
}

frappe.ui.form.on('Stock Item', {
	validate: function(frm) {
		if (frm.is_new()) {
			if (!isValidNumberOrEmpty(frm.doc.unit_cost) || !isValidNumberOrEmpty(frm.doc.price)) {
				frappe.validated = false;
				console.log("Unit cost or price must contain 1 / 2 d.p. numbers or empty");
				frappe.throw("Unit cost or price must contain 1 / 2 d.p. numbers or empty");
			}

			frm.set_value('unit_cost', toTwoDecimalPlaces(frm.doc.unit_cost));
			frm.set_value('price', toTwoDecimalPlaces(frm.doc.price));

			if (!isPriceGreaterThanCost(frm.doc.price, frm.doc.unit_cost)) {
				frappe.validated = false;
			}
			
		} else {
			if (!frm.doc.unit_cost) {
				frm.set_value('unit_cost', '0.00');
			}

			if (!frm.doc.price) {
				frm.set_value('price', '0.00');
			}

			if (!isValidNumber(frm.doc.unit_cost) || !isValidNumber(frm.doc.price)) {
				frappe.validated = false;
				console.log("Unit cost or price must contain 1 / 2 d.p. numbers");
				frappe.throw("Unit cost or price must contain 1 / 2 d.p. numbers");
			}

			frm.set_value('unit_cost', toTwoDecimalPlaces(frm.doc.unit_cost));
			frm.set_value('price', toTwoDecimalPlaces(frm.doc.price));

			if (!isPriceGreaterThanCost(frm.doc.price, frm.doc.unit_cost)) {
				frappe.validated = false;
			}

		}
		
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

});
