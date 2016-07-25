# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ReadList(models.Model):
    _name = 'blog.readlist'

    name = fields.Char(string="Title", required=True)
    article_ids = fields.Many2many('blog.article', string="Articles")
    length = fields.Integer(
        string="Length",
        compute='_compute_length',
        store=False
    )

    @api.depends('article_ids')
    def _compute_length(self):
        for r in self:
            r.length = len(r.article_ids)
