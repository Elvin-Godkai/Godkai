from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Godkai'
    site_title = 'Godkai 管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')