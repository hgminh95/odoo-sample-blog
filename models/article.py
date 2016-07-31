# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Article(models.Model):
    _name = 'blog.article'

    title = fields.Char(string="Title", required=True)
    content = fields.Text(string="Content")
    state = fields.Selection(string="State", selection=[
        ("draft", "Draft"),
        ("review", "In Review"),
        ("done", "Done")
    ])
    preview = fields.Char(
        string="Preview",
        compute="_compute_preview",
        store=False
    )

    @api.depends('content')
    def _compute_preview(self):
        for r in self:
            r.preview = r.content[:50] + "..."

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_review(self):
        self.state = 'review'

    @api.multi
    def action_done(self):
        self.state = 'done'
