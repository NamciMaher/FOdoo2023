# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LifetimeProduct(models.Model):
    _name = 'lifetime.product'

    name = fields.Char(string='Name')
    product_id = fields.Many2one('product.product', string='Product')

    @api.multi
    def choose_product(self):
        products = self.env['product.product'].search([])
        return {
            'name': 'Choose Product',
            'type': 'ir.actions.act_window',
            'res_model': 'lifetime.product',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_product_id': products[0].id},
        }

class LifetimeView(models.Model):
    _inherit = 'lifetime.product'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(LifetimeView, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            res['arch'] = '''
                <form string="Lifetime">
                    <field name="product_id"/>
                </form>
            '''
        return res
