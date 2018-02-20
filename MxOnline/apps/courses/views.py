from django.shortcuts import render, reverse
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import Course


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')  # 按照时间添加的逆序排序，降序，即最新顺序

        hot_course = Course.objects.all().order_by('-click_num')[:3]
        # 课程排序
        sort = request.GET.get('sort', "")
        if sort == 'students':
            all_courses = all_courses.order_by('-students')
        elif sort == 'hot':
            all_courses = all_courses.order_by('-click_num')
        # 对course分页,这里是第三方库pagenation的内置格式，只是换了一下数据字段
        try:
            page = request.GET.get('page', 1)  # 这个page字段是安装库后自己有的，不用管
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 3, request=request)
        # 教程文档中没有3这个参数，其实个参数在源码中是per_page,这个参数表示每页显示几个的意思
        courses = p.page(page)
        context = {

            'all_courses': courses,
            'sort': sort,  # 把sort传回去，做html选择状态
            'hot_course': hot_course
        }
        return render(request, 'course-list.html', context)


class CourseDetailView(View):
    """课程详情页"""

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.click_num += 1
        course.save()
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:2]
        else:
            relate_courses = []
        context = {
            'course': course,
            'relate_courses': relate_courses
        }
        return render(request, 'course-detail.html', context)