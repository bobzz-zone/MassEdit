# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobzz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import cint

class BulkEdit(Document):
	pass
@frappe.whitelist()
def update(doctype, field, value, condition):

	if ';' in condition:
		frappe.throw('; not allowed in condition')

	items = frappe.db.sql_list('''select name from `tab{0}`{1} '''.format(doctype,
		condition), debug=1)
	n = len(items)

	for i, d in enumerate(items):
		doc = frappe.get_doc(doctype, d)
		doc.set(field, value)

		try:
			doc.save()
		except Exception, e:
			frappe.msgprint(_("Validation failed for {0}").format(frappe.bold(doc.name)))
			raise e

		frappe.publish_progress(float(i)*100/n,
			title = _('Updating Records'), doctype='Bulk Edit', docname='Bulk Edit')

	# clear messages
	frappe.local.message_log = []
	frappe.msgprint(_('{0} records updated').format(n), title=_('Success'), indicator='green')