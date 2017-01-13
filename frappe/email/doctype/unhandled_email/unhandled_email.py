# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class UnhandledEmail(Document):
	def on_trash(self):
		frappe.db.set_value("Email Account",self.email_account,"no_remaining",None)
