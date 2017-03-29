// Copyright (c) 2016, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bulk Edit', {
	refresh: function(frm) {
		frm.page.set_primary_action(__('Update'), function() {
			if(!frm.doc.update_value){
				frappe.throw(__('Field "value" is mandatory. Please specify value to be updated'));
			}
			else{
				frappe.call({
					method: 'massedit.mass_edit.doctype.bulk_edit.bulk_edit.update',
					args: {
						doctype: frm.doc.document_type,
						field: frm.doc.field,
						value: frm.doc.update_value,
						condition_list: frm.doc.conditions,
					},
					callback: function() {
						frappe.hide_progress();
					}
				});
			}
		});
	},
	document_type: function(frm) {
		// set field options
		if(!frm.doc.document_type) return;

		frappe.model.with_doctype(frm.doc.document_type, function() {
			var options = $.map(frappe.get_meta(frm.doc.document_type).fields,
				function(d) {
					if(d.fieldname && frappe.model.no_value_type.indexOf(d.fieldtype)===-1) {
						return d.fieldname;
					}
					return null;
				}
			);
			frm.set_df_property('field', 'options', options);
			frm.set_df_property('cond_field', 'options', options);
		});
	},
	add:function(frm){
		cur_frm.add_child("conditions",{"cfield":frm.doc.cond_field,"cond":frm.doc.condition,"cval":frm.doc.cond_value});
		refresh_field("conditions");
	}
});
