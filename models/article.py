# -*- coding: utf-8 -*-

from openerp import models, fields, api


class article(models.Model):
    _name = 'blog.article'

    title = fields.Char(string="Title", required=True)
    content = fields.Text(string="Content")
    state = fields.Selection(string="State", selection=[
        ("draft", "Draft"),
        ("review", "In Review"),
        ("done", "Done")
    ])

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_review(self):
        self.state = 'review'

    @api.multi
    def action_done(self):
        self.state = 'done'
