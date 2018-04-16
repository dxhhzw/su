#-*-coding:utf-8-*-
from openerp import models, fields, api
class MainBusiness(models.Model):
    _name = 'su.business.list'
    _description="My Test"
    name=fields.Char(u'主业务单',required=True)
    #如何设置成不可编辑状态？
    order_date=fields.Datetime(u'订单日期',required=True)
    partner_id=fields.Many2one(u'客户名称',required=True)
    contact_id=fields.Many2one(u'联系人',required=True)
    partner_ref=fields.Char(u'客户单号',required=True)
    #order_type=fields.seletion('业务类型',required=True)
    #order_type = fields.seletion('业务需求', required=True)
    #cost_dst=fields.Seletcion((('n','c')),'cost_dst',required=True)
    #stock_type=fields.Selection((('n','c')),'仓储类型',required=True)
    trade_type=fields.Many2one('业务模式',required=True)
    contract_id=fields.Many2one('合同号',required=True)
    agent_id = fields.Many2one('所属代理', required=True)
    service_section_id = fields.Many2one('商务团队', required=True)
    company_id = fields.Many2one('所属公司', required=True)
    create_uid = fields.Many2one('单据创建', required=True)
    pricelist_id=fields.Many2one('价格表',required=True)
    err_msg=fields.Many2one('异常信息信息',required=True)

    need_my = fields.Boolean('贸易', required=True)
    need_cg = fields.Boolean('采购', required=True)
    need_xs = fields.Boolean('销售', required=True)
    need_df = fields.Boolean('代付', required=True)

    need_bj = fields.Boolean('需要报检', required=True)
    need_hd = fields.Boolean('需要换单', required=True)
    need_sj = fields.Boolean('送检', required=True)
    need_jksw = fields.Boolean('进口税务', required=True)
    need_cksw = fields.Boolean('出口税务', required=True)
    need_xggw = fields.Boolean('香港关务', required=True)

    need_dc = fields.Boolean('订车', required=True)
    need_ys = fields.Boolean('运输', required=True)

    need_rkzl = fields.Boolean('入库指令', required=True)
    need_ckzl = fields.Boolean('出口指令', required=True)
    need_dkzl = fields.Boolean('调库指令', required=True)
    need_hb = fields.Boolean('换标', required=True)
    need_tb = fields.Boolean('贴标', required=True)
    need_dt = fields.Boolean('打托', required=True)
    need_zzfw = fields.Boolean('增值服务', required=True)
    need_zx = fields.Boolean('装卸', required=True)

    need_sh= fields.Boolean('是散货', required=True)
    need_jzx = fields.Boolean('是集装箱', required=True)

    hwxx=fields.Char('货物信息')
    #状态类型
    desc = fields.Text('备注')
    WORKFLOW_STAT_SELECTION=[
        ('draft','草稿'),
        ('open','确认'),
        ('process','处理中'),
        ('bill', '结算中'),
        ('filling', '待归档'),
        ('cancel', '已完成')
    ]

    def do_toggle_done(self):
        self.name = "2018-03-08"
        return True
