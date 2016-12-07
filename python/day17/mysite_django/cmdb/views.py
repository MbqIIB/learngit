from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
import json
# Create your views here.
# 处理用户请求


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        user = request.POST.get('user', None)   # 第二个参数默认值为None
        password = request.POST.get('password', None)
        mail = request.POST.get('mail', None)
        qq = request.POST.get('qq', None)
        tel = request.POST.get('tel', None)

        models.UserInfo.objects.create(user=user, password=password, mail=mail, qq=qq, tel=tel)

        data_list = models.UserInfo.objects.all()

        return render(request, 'data.html', {'data': data_list})
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user', None)  # 第二个参数默认值为None
        password = request.POST.get('password', None)
        try:
            ret = models.UserInfo.objects.get(user=user, password=password)
            return render(request, 'index.html')
        except:
            return render(request, 'login.html', {'error': "用户名或密码错误"})

    else:
        return render(request, 'login.html')


def data(request):
    data_list = models.UserInfo.objects.all()

    return render(request, 'data.html', {'data': data_list})


def data1(request, p1, p2):
    mun = p1 + p2
    return HttpResponse(mun)


def data2(request, p1):
    mun = p1
    return HttpResponse(mun)


def huang(reques):
    return render(reques, '小黄人.html')


USER_LIST = []

for item in range(94):
    temp = {"id": item, 'username': 'liang' + str(item), 'email': 'liang' + str(item) + '@163.com'}
    USER_LIST.append(temp)


def list(requst, page):
    page = int(page)
    start = (page - 1) * 10
    end = page * 10
    user_list = USER_LIST[start:end]

    return render(requst, 'data.html', {'user_list': user_list})


def detail(requst, nid):
    nid = int(nid)
    current_detail_dict = USER_LIST[nid]

    return render(requst, 'detail.html', {'current_detail_dict': current_detail_dict})


def template(requst):
    return render(requst, 'template.html', {'k1': 'VVV'})


def assets(requst):
    assets_list = []
    for i in range(10):
        temp = {'hostname': 'h' + str(i), 'port': 80}
        assets_list.append(temp)
    return render(requst, 'assets.html', {'assets_list': assets_list})


def userinfo(requst):
    user_list = []
    for i in range(10):
        temp = {'username': 'u' + str(i), 'salary': 80}
        user_list.append(temp)
    return render(requst, 'userinfo.html', {'user_list': user_list})


def ajax_demo(request):
    if request.method == 'POST':
        ret = {'status': False, 'message': ''}
        user = request.POST.get('user', None)
        password = request.POST.get('password', None)

        if user == '111' and password == '222':
            ret['status'] = True
            return HttpResponse(json.dumps(ret))
        else:
            ret['message'] = "用户名或密码错误"
            return HttpResponse(json.dumps(ret))
    return render(request, 'ajax_demo.html')



