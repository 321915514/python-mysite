from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from django import views
from django.utils.decorators import method_decorator
def outer(func):
    def inner(request,*args,**kwargs):
        print(request.method)
        return func(request,*args,**kwargs)
    return inner
# Create your views here.
class login(views.View):
    # def dispatch(self, request, *args, **kwargs):
    #     if request.method=='GET':
    #         return HttpResponse('??')
    #     ret = super(login,self).dispatch(request,*args,**kwargs)
    #     return ret
    # @method_decorator(outer)
    def get(self,request,*args,**kwargs):
        return render(request,'login.html',{'msg':''})
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        pwd=request.POST.get('password')
        c = models.Admin.objects.filter(username=username, password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username']=username
            rep = redirect('/index.html')
            return rep
        else:
            message = '用户名或密码错误'
            return render(request, 'login.html', {'msg': message})

def index(request):
    # if request.method == 'POST':
    #     user = request.POST.get('username')
    #     print(user)
        if request.session.get('is_login'):
         username=request.session['username']
         # user = request.COOKIES.get('username')
         if username:
             return render(request, 'index.html',{'name':username})
         else:
            return redirect('/login.html')
# def login(request):
#         # models.Admin.objects.create(username='root',password='123123')
#         message=''
#         v=request.session
#         print(type(v))
#         if request.method=="POST":
#             username=request.POST.get('username')
#             pwd=request.POST.get('password')
#             c=models.Admin.objects.filter(username=username,password=pwd).count()
#             if c:
#                  request.session['is_login']= True
#                  request.session['username']=username
#                  rep = redirect('/index.html')
#                  # rep.set_cookie('username', username)
#                  return rep
#             else:
#                  message= '用户名或密码错误'
#         obj= render(request,'login.html', {'msg': message })
#         return obj
# def home(request):
#     return render(request,'home.html')
def logout(request):
    request.session.clear()
    return redirect('/login.html')

# def test(request):
#     message=""
#     if request.method=='POST':
#         user=request.POST.get('username')
#         pwd=request.POST.get('password')
#         c=models.Admin.objects.filter(username=user,password=pwd).count()
#         if c:
#             rep=redirect('/index.html')
#             rep.set_cookie('username',user)
#             return rep
#         else:
#             message='error'
#     return render(request,'login.html',{'msg':message})
def classes(request):
    current_user=request.session.get('username')
    cls_list=models.classes.objects.all()
    return render(request,'clesses.html',{'cls_list':cls_list})
def student(request):
    return render(request,'student.html')
def teacher(request):
    return render(request,'teacher.html')

