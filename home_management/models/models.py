from lxml.objectify import set_pytype_attribute_tag
from pip._internal.commands import search

from odoo import models, fields, api


class HomeManagement(models.Model):
    _name = 'home.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Home Management.'

    name = fields.Char("Name")
    age = fields.Integer("Age")
    date = fields.Date('Date')
    add_id = fields.Many2one('res.users', string='Add ID')
    adding_ids = fields.Many2many('res.partner', 'home_management_adding_rel', 'home_adding', 'home_ids',
                                  string='Adding_IDS')

    selection = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'Posted')
    ], string='State')

    def action_draft(self):
        self.state = 'draft'

    def action_posted(self):
        self.state = 'posted'

    def check_orm(self):
        search_var = self.env['home.management'].search([('selection','=','male')])
        print("search_var--------", search_var)
        for i in search_var:
            print('name----',i.name,'age----------',i.age,'date----',i.date,'selection------',i.selection)
