from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Production"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "CM Production Order",
					"description": _("Orders released for production."),
                    "label": _("Production Order")
				},
				{
					"type": "doctype",
					"name": "CM Shared Production Order",
					"description": _("Shared Production Orders."),
                    "label": _("Shared Production Order")
				},
            ]
        },
        {
            "label": _("Stock"),
            "items": [
				{
					"type": "doctype",
					"name": "CM Paper Roll Register",
                    "label": _("Register Paper Rolls")
				},
                {
                    "type": "doctype",
                    "name": "CM Paper Roll",
                    "label": _("Paper Rolls")
                }
			]
		},
		{
			"label": _("Bill of Materials"),
			"items": [
				{
					"type": "doctype",
					"name": "CM Box Description",
					"description": _("Bill of Materials (BOM)"),
					"label": _("Box Description")
				},
				{
					"type": "doctype",
					"name": "BOM",
					"icon": "fa fa-sitemap",
					"label": _("BOM Browser"),
					"description": _("Tree of Bill of Materials"),
					"link": "Tree/BOM",
				},
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Manufacturing Settings",
					"description": _("Global settings for all manufacturing processes."),
				}
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "doctype",
                    "name": "CM Product Costs"
				},
			]
		},
	]