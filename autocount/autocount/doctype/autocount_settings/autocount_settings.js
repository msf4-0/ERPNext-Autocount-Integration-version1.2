// Copyright (c) 2022, Timothy Wong and contributors
// For license information, please see license.txt

const defaultIPAddress = "host.docker.internal";
const defaultPort = "8888";

frappe.ui.form.on('Autocount Settings', {
	btn_test_connection: function(frm) {
		if (!frm.doc.ip_address) {
			frm.set_value("ip_address", defaultIPAddress);
		}

		if (!frm.doc.port) {
			frm.set_value("port", defaultPort);
		}

		frm.call({
			method: "autocount.autocount.doctype.autocount_settings.autocount_settings.test_connection",
			args:{
			    doc: frm.doc
			},
			freeze: true,
			callback:function(r){
				console.log(r.message);
				frappe.msgprint(r.message);
			},
		});
	},

	before_save: function(frm) {
		if (!frm.doc.ip_address) {
			frm.set_value("ip_address", defaultIPAddress);
		}

		if (!frm.doc.port) {
			frm.set_value("port", defaultPort);
		}
	}

});
