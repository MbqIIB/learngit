from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
import os
import django
from mysite import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from app01 import models


# def index(request):
#     if request.method == "POST":
#         obj = request.FILES.get('up_file')
#         f = open(obj.name, 'wb')
#         for chunk in obj.chunks():
#             f.write(chunk)
#         f.close()
#     return render(request, 'index.html')



from django.utils.safestring import mark_safe

class PageInfo(object):
    def __init__(self,current,totalItem,peritems=5):
        self.__current=current
        self.__peritems=peritems
        self.__totalItem=totalItem
    def From(self):  # 从
        return (self.__current-1)*self.__peritems
    def To(self):  # 到
        return self.__current*self.__peritems
    def TotalPage(self):   # 总页数
        result=divmod(self.__totalItem,self.__peritems)
        if result[1]==0:
            return result[0]
        else:
            return result[0]+1


def Custompager(baseurl,currentPage,totalpage):   # 基础页，当前页，总页数
    perPager=11
    # 总页数<11
    # 0 -- totalpage
    # 总页数>11
        # 当前页大于5 currentPage-5 -- currentPage+5
            # currentPage+5是否超过总页数,超过总页数，end就是总页数
        # 当前页小于5 0 -- 11
    begin=0
    end=0
    if totalpage <= 11:
        begin=0
        end=totalpage
    else:
        if currentPage>5:
            begin=currentPage-5
            end=currentPage+5
            if end > totalpage:
                end=totalpage
        else:
            begin=0
            end=11
    pager_list=[]
    if currentPage<=1:
        first="<a href=''>首页</a>"
    else:
        first="<a href='%s%d'>首页</a>" % (baseurl,1)
    pager_list.append(first)

    if currentPage<=1:
        prev="<a href=''>上一页</a>"
    else:
        prev="<a href='%s%d'>上一页</a>" % (baseurl,currentPage-1)
    pager_list.append(prev)

    for i in range(begin+1,end+1):
        if i == currentPage:
            temp="<a href='%s%d' class='selected'>%d</a>" % (baseurl,i,i)
        else:
            temp="<a href='%s%d'>%d</a>" % (baseurl,i,i)
        pager_list.append(temp)
    if currentPage>=totalpage:
        next="<a href='#'>下一页</a>"
    else:
        next="<a href='%s%d'>下一页</a>" % (baseurl,currentPage+1)
    pager_list.append(next)
    if currentPage>=totalpage:
        last="<a href=''>末页</a>"
    else:
        last="<a href='%s%d'>末页</a>" % (baseurl,totalpage)
    pager_list.append(last)
    result=''.join(pager_list)
    return mark_safe(result)   #把字符串转成html语言



# def publish(request):
#     ret = {'status': False, 'data': '', 'error': '', 'summary': ''}
#     if request.method == 'POST':
#         request_form = models.PublishForm(request.POST)
#         if request_form.is_valid():
#             request_dict = request_form.clean()
#             print(request_dict)
#             ret['status'] = True
#             return render(request, 'index.html', {'error': ret})
#         else:
#             error_msg = request_form.errors.as_json()
#             ret['error'] = json.loads(error_msg)
#             return render(request, 'index.html', {'error': ret})
#     return render(request, 'index.html', {'error': ret})





# # F 使用查询条件的值
# from django.db.models import F
# models.Tb1.objects.update(num=F('num')+1)
#
# # Q 构建搜索条件
# from django.db.models import Q
# con = Q()
#
# q1 = Q()
# q1.connector = 'OR'
# q1.children.append(('id', 1))
# q1.children.append(('id', 10))
# q1.children.append(('id', 9))
#
# q2 = Q()
# q2.connector = 'OR'
# q2.children.append(('c1', 1))
# q2.children.append(('c1', 10))
# q2.children.append(('c1', 9))
#
# con.add(q1, 'AND')
# con.add(q2, 'AND')
#
# models.Tb1.objects.filter(con)
#
# # SQL
# from django.db import connection
# cursor = connection.cursor()
# cursor.execute("""SELECT * from tb where name = %s""", ['Lennon'])
# row = cursor.fetchone()


#
# # models.UserInfo.objects.create(name='liang',user_type=1,email='liang@163.com')
# user_info_obj = models.UserInfo.objects.filter(id=1).first()
#
# # models.UserProfile.objects.create(user_info=user_info_obj, username='liang', password='123',)
#
#
# print(user_info_obj.user_type)
# print(user_info_obj.get_user_type_display())
# print(user_info_obj.userprofile.password)
#
# user_info_obj = models.UserInfo.objects.filter(id=1).values('email', 'userprofile__username').first()
# print(list(user_info_obj.keys()))
# print(user_info_obj.values())



# user_info_obj = models.UserInfo.objects.filter(name='liang')[0]
# user_info_objs = models.UserInfo.objects.all()
#
#
# models.UserGroup.objects.create(caption='liang')
# models.UserGroup.objects.create(caption='lianglian')
#
#
# group_obj = models.UserGroup.objects.get(caption='liang')
# group_objs = models.UserGroup.objects.all()
#
# # 添加数据
# group_obj.user_info.add(user_info_obj)
# group_obj.user_info.add(*user_info_objs)  # '*kwarg'
#
# # 删除数据
# group_obj.user_info.remove(user_info_obj)
# group_obj.user_info.remove(*user_info_objs)
#
# # 添加数据
# user_info_obj.usergroup_set.add(group_obj)
# user_info_obj.usergroup_set.add(*group_objs)
#
# # 删除数据
# user_info_obj.usergroup_set.remove(group_obj)
# user_info_obj.usergroup_set.remove(*group_objs)
#
# # 获取数据
# print(group_obj.user_info.all())
# print(group_obj.user_info.all().filter(id=1))
#
# # 获取数据
# print(user_info_obj.usergroup_set.all())
# print(user_info_obj.usergroup_set.all().filter(caption='liang'))
# print(user_info_obj.usergroup_set.all().filter(caption='lianglian'))


