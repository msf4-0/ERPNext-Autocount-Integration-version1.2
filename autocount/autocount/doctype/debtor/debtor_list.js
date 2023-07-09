// Copyright (c) 2022, Timothy Wong and contributors
// For license information, please see license.txt

const doctype = "Debtor";
const updateInterval = 10000;
var updateInProgress = false;
var interval;

function isInsideListView() {
    return (cur_page.page.id === `page-List/${doctype}/List`);
}

frappe.listview_settings[doctype] = {

	before_render: function(listview) {
		clearInterval(interval);
		//console.log("before render");
		interval = setInterval(function() {
			if (isInsideListView()) {
				if (updateInProgress == false) {
					if (cur_list.get_checked_items().length == 0) {
						//console.log("Refresh");
						cur_list.refresh();	
						return;
					}
					console.log(`${new Date().toLocaleString()} : [-] Paused sync when item is checked.`);
					return;
				}
				console.log(`${new Date().toLocaleString()} : [-] Paused sync when update in progress.`);
				return;
			} else {
				clearInterval(interval);
				console.log(`${new Date().toLocaleString()} : [!] Stopped sync on ${doctype}.`);
			}		
		}, updateInterval);
	},

	refresh: function (listview) {
		updateInProgress = true;
		frappe.call({
            method:"autocount.autocount.doctype.update.update_all_tables",
            callback:function(r){
                localStorage.clear();
                sessionStorage.clear();
                console.log(`${new Date().toLocaleString()} : ${r.message}`);
                updateInProgress = false;
            },
        });
	},

    onload: function(listview) {
    	console.log("Onload");
  
    	listview.page.set_secondary_action('Sync', function() {
            console.log("Sync is pressed");
            frappe.msgprint("Sync now...");
            frappe.call({
                method:"autocount.autocount.doctype.debtor.debtor_list.update",
                callback:function(r){
                	localStorage.clear();
                	sessionStorage.clear();
                    console.log(r.message);
                    // listview.refresh();
                    location.reload();
                },
            })
        }, 'octicon octicon-sync');
    },

    
    
}