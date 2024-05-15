from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class CustomSetting(models.TransientModel):
    _inherit = 'res.config.settings'
    credit_limit = fields.Float(
        string='Credit Limit')

    def set_values(self):
        res = super(CustomSetting, self).set_values()
        self.env['ir.config_parameter'].set_param('po_credit_limit.credit_limit', self.credit_limit)

    @api.model
    def get_values(self):
        res = super(CustomSetting, self).get_values()
        sudo = self.env['ir.config_parameter'].sudo()
        notes = sudo.get_param('po_credit_limit.credit_limit')
        res.update(
            credit_limit=notes
        )
        return res


class CustomSetting1(models.Model):
    _inherit = 'res.partner'
    Partner_credit_limit = fields.Float(
        string='Credit Limit')


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection(
        selection_add=[('first_approval', 'First Approval'), ('second_approval', 'Second Approval')])

    compute_settings_credit_limit = fields.Float(default=0.00, store=True,
                                                 compute='_compute_settings_credit_limit')

    def _compute_settings_credit_limit(self):
        self.compute_settings_credit_limit = self.env['ir.config_parameter'].sudo().get_param(
            'po_credit_limit.credit_limit')

    def button_confirm(self):
        for i in self:
            credit_limit = float(i.env['res.config.settings'].get_values()['credit_limit'])
            print('-----------', )
            if i.state == 'draft' or i.state == 'sent':
                i.write({'state': 'first_approval'})
            elif (i.state == 'first_approval' and
                  i.partner_id.Partner_credit_limit <= credit_limit):
                i.write({'state': 'second_approval'})
            elif (i.state == 'first_approval' and
                  i.partner_id.Partner_credit_limit > credit_limit):
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'message': _('Can not confirm the order!'),
                        'type': 'warning',
                        'sticky': True,
                    },
                }
            elif i.partner_id.Partner_credit_limit <= credit_limit and (
                    i.state == 'second_approval'):
                i.button_approve()
            elif i.partner_id.Partner_credit_limit > credit_limit and (
                    i.state == 'second_approval'):
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'message': _('Can not confirm the order!'),
                        'type': 'warning',
                        'sticky': True,
                    },
                }
            else:
                return super(PurchaseOrder, i).button_confirm()
