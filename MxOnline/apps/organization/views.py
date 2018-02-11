from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg, CityDict
# Create your views here.


class OrgView(View):
    """课程机构列表功能"""
    def get(self, request):
        #课程机构
        all_orgs = CourseOrg.objects.all()
        org_nums =all_orgs.count()  # 计数
        #城市
        all_citys = CityDict.objects.all()
        context = {
            'all_orgs': all_orgs,
            'all_citys': all_citys,
            'org_nums': org_nums
        }
        return render(request, 'org-list.html', context)