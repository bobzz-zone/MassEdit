// Copyright (c) 2016, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bulk Edit', {
	refresh: function(frm) {
		
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
			frm.set_df_property('cfield', 'options', options);
		});
	}
});
