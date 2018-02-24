from django.shortcuts import render, reverse
from django.views.generic.base import View
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import Course, CourseResource
from operation.models import UserFavorite, CourseComments


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')  # 按照时间添加的逆序排序，降序，即最新顺序

        hot_course = Course.objects.all().order_by('-click_num')[:3]
        # 课程排序
        sort = request.GET.get('sort', "")  # 找不到就为空''
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


class CourseInfoView(View):
    """
    课程章节信息
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resource = CourseResource.objects.filter(course=course)  # 用get的话只能获得一个资源文件，filter筛选所有满足的资源文件
        context = {
            'course':course,
            'all_resource': all_resource
        }
        return render(request, "course-video.html", context)


class CommentsView(View):

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resource = CourseResource.objects.filter(course=course)  # 用get的话只能获得一个资源文件，filter筛选所有满足的资源文件
        all_comments = CourseComments.objects.all()
        context = {
            'course': course,
            'all_resource': all_resource,
            'all_comments': all_comments
        }
        return render(request, "course-comment.html", context)


class AddCommentsView(View):
    """
    用户添加课程评论
    """
    def post(self, request):
        if not request.user.is_anthenticated():
            # 判断用户状态
            return HttpResponse('{"status": "fail", "msg":"用户未登录"}', content_type='application/json')
        course_id = request.POST.get('course_id', 0)
        comments = request.POST.get('comments', '')
        if course_id > 0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status": "success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg":"添加失败"}', content_type='application/json')



