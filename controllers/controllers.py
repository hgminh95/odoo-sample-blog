# -*- coding: utf-8 -*-
from odoo import http


class Blog(http.Controller):

    @http.route('/blog/articles', auth='public')
    def index(self, **kw):
        Articles = http.request.env['blog.article']
        return http.request.render('blog.article_index', {
            'articles': Articles.search([('state', '=', 'done')])
        })

    @http.route('/blog/articles/<model("blog.article"):article>/', auth='public')
    def object(self, article, **kw):
        return http.request.render('blog.article_show', {
            'article': article
        })
