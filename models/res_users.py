from odoo import models, fields
class ResUsers(models.Model):
    _inherit = 'res.users'
    sidebar_visible = fields.Boolean("Show App Sidebar", default=True)
    def __init__(self, pool, cr):
        init_res = super(ResUsers, self).__init__(pool, cr)
        type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        type(self).SELF_WRITEABLE_FIELDS.extend(['sidebar_visible'])
        type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        type(self).SELF_READABLE_FIELDS.extend(['sidebar_visible'])
        return init_res