// Copyright (c) 2022, Timothy Wong and contributors
// For license information, please see license.txt

const itemTable = "item_table";
const chosenTable = "chosen_table";
const addChosenButton = "btn_add_chosen";

const addMethod = "autocount.autocount.doctype.cancel_so.cancel_so.add";
const editMethod = "autocount.autocount.doctype.cancel_so.cancel_so.edit";

function isItemInChosenTable(frm, selectedData) {
	// Check if selected item is already in chosen table
	var arr = frm.doc[chosenTable];
	for (var i = 0; i < arr.length; i++) {
		if (arr[i].sales_order_no == selectedData.sales_order_no 
			&& arr[i].item_code == selectedData.item_code) {
			return true;
		}
	}
	return false;
}

function unCheckAll(frm) {
	// Uncheck all checkboxes in item table
	var selected = frm.get_field(itemTable).grid.get_selected_children().length;
	var all = frm.doc[itemTable].length;
	if (selected > 0) {
		if (selected != all) {
			frm.get_field(itemTable).check_all_rows();
			frm.get_field(itemTable).check_all_rows();
			return;
		}
		frm.get_field(itemTable).check_all_rows();
	}
}

function populateItemTable(frm, msg) {
	for (var i = 0; i < msg.length; i++) {
		var data = msg[i];
		var remainingQuantity = data.Qty - data.TransferedQty;

		if (remainingQuantity > 0) {
			var newRow = frm.add_child(itemTable);

			newRow.sales_order_no = data.SalesOrderNo;
			newRow.item_code = data.ItemCode;
			newRow.uom = data.UOM;
			newRow.quantity = remainingQuantity;
		}
		
	}

	frm.refresh_fields(itemTable);
}

function populateChosenTable(frm, selected) {
	for (var i = 0; i < selected.length; i++) {
		if (!isItemInChosenTable(frm, selected[i])) {
			var newRow = frm.add_child(chosenTable);

			newRow.sales_order_no = selected[i].sales_order_no;
			newRow.item_code = selected[i].item_code;
			newRow.uom = selected[i].uom;
			newRow.quantity = selected[i].quantity;
		}
	}

	frm.refresh_fields(chosenTable);
}

frappe.ui.form.on(cur_frm.doctype, {
	// Fetch data from Autocount and populate to item table when debtor code is changed
	debtor_code: function(frm) {
		var debtor_code = frm.doc.debtor_code;

		if (debtor_code) {
			frm.call({
				method: "autocount.autocount.doctype.cancel_so.cancel_so.get_items_by_debtor_autocount",
				args:{
				    debtor_code: frm.doc.debtor_code
				},
				callback:function(r){
					console.log(r.message);

					frm.clear_table(itemTable);
					frm.clear_table(chosenTable);

					populateItemTable(frm, r.message);
				},
			}) 
		} else {
			frm.clear_table(itemTable);
			frm.clear_table(chosenTable);

			frm.refresh_fields(itemTable);
			frm.refresh_fields(chosenTable);
		}

	},

	btn_add_chosen: function(frm) {
		// Add selected items from item table to chosen table
		var selected = frm.get_field(itemTable).grid.get_selected_children();
		if (selected.length > 0) {
			populateChosenTable(frm, selected);			
			unCheckAll(frm);
		}

	},

	btn_clear_all: function(frm) {
		frm.clear_table(chosenTable);
		frm.refresh_fields(chosenTable);
	},

	onload_post_render: function(frm) {
        frm.get_field(itemTable).grid.cannot_add_rows = true;
        frm.get_field(itemTable).grid.only_sortable();

        frm.refresh_fields(itemTable);

        frm.get_field(chosenTable).grid.cannot_add_rows = true;
        frm.refresh_fields(chosenTable);
    },

    refresh: function(frm) {
    	// Disable debtor code to be edited in EDIT mode
    	frm.set_df_property("debtor_code", "read_only", frm.is_new() ? 0 : 1);

    	// Update available items when refresh for EDIT mode
    	if (!frm.is_new()) {
			frm.call({
				method: "autocount.autocount.doctype.cancel_so.cancel_so.get_items_by_debtor_autocount",
				args:{
				    debtor_code: frm.doc.debtor_code
				},
				callback:function(r){
					console.log(r.message);
					frm.clear_table(itemTable);
					populateItemTable(frm, r.message);
				},
			});

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