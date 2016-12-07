from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
import json
# Create your views here.


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

        return render(request, 'index.html')
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


def data(request, page=1):
    # models.HostInfo.objects.create(hostname='web1', address='10.101.201.10', port=80, status='上线',)
    # models.HostInfo.objects.create(hostname='web2', address='10.101.201.11', port=80, status='上线',)
    # models.HostInfo.objects.create(hostname='web3', address='10.101.201.12', port=80, status='上线',)
    # models.HostInfo.objects.create(hostname='web4', address='10.101.201.13', port=80, status='上线',)

    class db():
        ret = {'status': False, 'message': ''}

        def __init__(self, nid, hostname, address, port, status):
            self.nid = nid
            self.hostname = hostname
            self.address = address
            self.port = port
            self.status = status

        def update(self):
            try:
                h_obj = models.HostInfo.objects.get(nid=self.nid)
                h_obj.hostname = self.hostname
                h_obj.address = self.address
                h_obj.port = self.port
                h_obj.status = self.status
                h_obj.save()

                self.ret['status'] = True
                self.ret['message'] = '变更成功'
                return self.ret
            except Exception as error:
                self.ret['status'] = False
                self.ret['message'] = '变更失败:[%s]' % error
                return self.ret

        def delete(self):
            try:
                models.HostInfo.objects.get(nid=self.nid).delete()
                self.ret['status'] = True
                self.ret['message'] = '删除成功'
                return self.ret
            except Exception as error:
                self.ret['status'] = False
                self.ret['message'] = '删除失败:[%s]' % error
                return self.ret

        def add(self):
            try:
                models.HostInfo.objects.create(hostname=self.hostname, address=self.address, port=self.port, status=self.status)
                self.ret['status'] = True
                self.ret['message'] = '添加成功'
                return self.ret
            except Exception as error:
                self.ret['status'] = False
                print(error)
                self.ret['message'] = '添加失败:[%s]' % error
                return self.ret

    if request.method == 'POST':
        active = request.POST.get('active')
        nid = request.POST.get('nid')
        hostname = request.POST.get('hostname')
        address = request.POST.get('address')
        port = request.POST.get('port')
        status = request.POST.get('status')

        print(active, nid, hostname, address, port, status)
        if active:
            obj = db(nid, hostname, address, port, status)
            if hasattr(obj, active):
                func = getattr(obj, active)
                ret = func()

            data_list = models.HostInfo.objects.all()

            print(ret)
            return HttpResponse(json.dumps(ret))
            # return render(request, 'data.html', {'data': data_list, 'result': ret})

        return render(request, 'data.html')
    else:
        # 一页显示得内容
        content_num = 15
        # 路由系统传过来的参数默认是字符串
        page = int(page)
        start = (page - 1) * content_num
        end = page * content_num
        data_num = models.HostInfo.objects.all().count()
        total_page, remainder = divmod(data_num, content_num)
        if remainder > 0:
            total_page += 1
        page_list = []
        for num in range(total_page):
            num += 1
            page_list.append(num)

        crrunt_data = models.HostInfo.objects.all()[start:end]
        return render(request, 'data.html', {'data': crrunt_data, 'page_list': page_list})

