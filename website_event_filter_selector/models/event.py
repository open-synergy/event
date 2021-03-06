# -*- coding: utf-8 -*-
# © 2016 Jairo Llopis <jairo.llopis@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class EventEvent(models.Model):
    _inherit = "event.event"

    city = fields.Char(related="address_id.city", store=True)
