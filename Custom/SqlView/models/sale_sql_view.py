from odoo import models, fields, tools

class SaleSqlView(models.Model):
    _name = 'sale.sql.view'
    _description = 'Sale SQL View'
    _auto = False

    id = fields.Integer(string='ID', readonly=True)   # must exist
    sale_number = fields.Char('Sales Number', readonly=True)
    customer_name = fields.Char('Customer', readonly=True)
    order_date = fields.Datetime('Order Date', readonly=True)
    amount = fields.Monetary('Amount', readonly=True)
    currency_id = fields.Many2one('res.currency', string='Currency', readonly=True)

    def init(self):
        # safely drop existing view then create it
        tools.drop_view_if_exists(self.env.cr, 'sale_sql_view')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW sale_sql_view AS (
                SELECT
                    row_number() OVER () as id,
                    so.name as sale_number,
                    rp.name as customer_name,
                    so.date_order as order_date,
                    so.amount_total as amount,
                    rc.id as currency_id
                FROM sale_order so
                JOIN res_partner rp ON so.partner_id = rp.id
                LEFT JOIN res_currency rc ON so.currency_id = rc.id
            )
        """)
