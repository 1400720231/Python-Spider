from django.shortcuts import render
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from .models import CourseOrg, CityDict
# Create your views here.
from .forms import UserAskForm
#from courses.models import Course


class OrgView(View):
    """课程机构列表功能 筛选功能等"""
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 热门课程，按照click_nums倒序
        hot_orgs = all_orgs.order_by("-click_num")[0:3]
        # 城市
        all_citys = CityDict.objects.all()
        # 下面的每次筛选就会重新复赋值给all_orgs，保证了all_orgs是满足筛选的
        # 筛选出城市
        city_id = request.GET.get('city', "")  # city的值来自于a标签：<a href="?city={{ city.id }}">
                                               # 传进来的是city.id是来自CotyDict queryset的实例创建id，数据库中的all_orgs的city_id是CityDict的外键，所以这种filter是对的
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))  # city字段是外键，在数据库中以city_id名字保存
            # CourseOrg中city字段是个CityDict对象(因为是外键)，但是在数据库中是以city_id字段保存，因为CourseOrg中的默认主键是id
        # 类别筛选
        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(category=category)
        sort = request.GET.get('sort', "")
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by("-students")
            elif sort == 'courses':
                all_orgs = all_orgs.order_by("-course_nums")

        # 计数
        org_nums = all_orgs.count()

        # 对机构分页,这里是第三方库pagenation的内置格式，只是换了一下数据字段
        try:
            page = request.GET.get('page', 1)  # 这个page字段是安装库后自己有的，不用管
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 3, request=request)  # 教程文档中没有3这个参数，其实个参数在源码中是per_page,这个参数表示每页显示几个的意思
        orgs = p.page(page)
        context = {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
            'city_id': city_id,  # 回传city_id只是为了增加选中时候的判断功能
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort
        }
        return render(request, 'org-list.html', context)


class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():  # 是否合法
            user_ask = userask_form.save(commit=True)  # commit属于ModelForm的方法
            # 如果是commit= False的话 user_ask就是一个model对象
            return HttpResponse("status: success")  # 声明json格式
        else:
            return HttpResponse("{'status': 'fail', 'msg':'添加出错'}")


class OrgHomeView(View):
    """
    机构首页
    """
    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        # course_set表示反向取外键的值,也是queryset对象
        all_course = course_org.course_set.all()[:3]
        all_teacher = course_org.teacher_set.all()[:1]  # 反向获取到teacher
        context = {
            'all_course': all_course,
            'all_teacher': all_teacher,
            'course_org': course_org,
            'current_page': current_page
                    }
        return render(request, 'org-detail-homepage.html', context)


class OrgCourseView(View):
    """
    课程首页
    """
    def get(self, request, org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        # course_set表示反向取外键的值,也是queryset对象
        all_course = course_org.course_set.all()

        context = {
            'all_course': all_course,
            'course_org': course_org,
            'current_page': current_page
        }
        return render(request, 'org-detail-course.html', context)


class OrgDescView(View):
    """
    机构介绍页
    """
    def get(self, request, org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        # course_set表示反向取外键的值,也是queryset对象
        all_course = course_org.course_set.all()

        context = {

            'course_org': course_org,
            'current_page': current_page
        }
        return render(request, 'org-detail-desc.html', context)


class OrgTeacherView(View):
    """
    教师介绍页
    """
    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))
        # course_set表示反向取外键的值,也是queryset对象
        all_teachers = course_org.teacher_set.all()

        context = {
            'all_teachers': all_teachers,
            'course_org': course_org,
            'current_page': current_page
        }
        return render(request, 'org-detail-teachers.html', context)

class AddFavView(View):
    """
    课程收藏功能

    """
    def post(self, request):
