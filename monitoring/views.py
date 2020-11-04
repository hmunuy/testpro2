from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.template import loader
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Host
from .models import get_interface
from .models import get_cpu_ram
from .models import get_uptime
from .models import get_traffic
from .models import get_clients
from .models import get_clients_detail
import datetime
# from .models import snmpdata
import requests
from django.http import HttpResponse




# Create your views here.
url = 'https://notify-api.line.me/api/notify'
token = 'NuuUuOmWepLTjLylkfdFwppgMhxjTeNiF4wE6Kdg70a'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

#Query Data Host_snmp show in table on home.html page
# def hello(request):
#     data11 = "hnubyy"
#     return render(request,'home.html',{'hostname':data11})

def index(request):
    return render(request,'index.html')


def comming(request):
    return render(request,'comming.html')

def index2(request):
    return render(request,'index3.html')
def home(request):
    #Qury Data Show on Table in home.html
    username = request.session['username']
    # data = list(Host.objects.all().distinct())
    # in_time = Host.objects.latest('insert_time')
    # data = Host.objects.all().filter(insert_time='in_time').order_by('-description')
    data = get_uptime.objects.order_by("-id")[:20]
    data2 = get_clients.objects.order_by('-id')[:3]
    data3 = get_cpu_ram.objects.order_by("-id")[:20]
    data4 = get_traffic.objects.filter(ip_hostname='10.99.0.1').order_by('-id')[:5]

    sum_user = 0
    num_user = 0
    sum_out = 0
    sum_in = 0
    sum_in1 = 0
    sum_out1 = 0
    in_x = 0
    out_y = 0
    cal_in = 0
    cal_out = 0
    for qry in data2 :
        num_user = qry.clients 
        sum_user = sum_user + num_user
    x_sum = str(sum_user)
    
    
    for qry in data4 :
        if qry.interface  == 'GigabitEthernet0/0/1':
            in_x = qry.inbound 
            out_y = qry.outbound 
            sum_in = sum_in + int(in_x)
            sum_out = sum_out + int(out_y)
            cal_in = float("{:.2f}".format(sum_in/1073741824))
            cal_out = float("{:.2f}".format(sum_out/1073741824))
    sum_in1 = str(cal_in)
    sum_out1 = str(cal_out)
    # x = data.query
    if username != "" :
       return render(request,'home.html',{'data':data,'data2':x_sum,'hostname':data3,'sum_in':sum_in1,'sum_out':sum_out1})
    else:
        return render(request,'registeradmin.html')
           
    
    # Check Login
    # username = request.GET['username']
    # password = request.GET['password']
    # if ((username == 'admin') and  (password == 'admin'))  :
    #     msg = ("เข้าสู่ระบบ โดย คุณ :"+username)
    #     r = requests.post(url, headers=headers , data = {'message':msg})
    


    
    # else:
    #     msg = ("มีการพยายามเข้าสู่ระบบ โดย คุณ :"+username)
    #     r = requests.post(url, headers=headers , data = {'message':msg})
    #     return render(request,'index.html')
def registeradmin(request):
    
    return render(request,'registeradmin.html')

def monitor(request):
    username = request.session['username']
    data = get_interface.objects.order_by('-id')[:589]
    # x_time = datetime.datetime.now()
    # x_time_sum = x_time.strftime('%d:'+'%A:'+'%B:'+'%Y:'+'%H:'+'%M')
    #hostname = ['WLC_FITM1','WLC_FITM2','WLC_FITM3']
    #data2 = snmp_ap.objects.all().filter(hostname='WLC_FITM1').order_by('-id')
    data2 = get_clients.objects.order_by('-id')[:3]
    data3 = get_clients_detail.objects.order_by('-id')
    data4 = get_traffic.objects.order_by('-id')[:589]
    
    sum_user = 0
    num_user = 0
    for qry in data2 :
        num_user = qry.clients 
        sum_user = sum_user + num_user
    x_sum = str(sum_user)

    
        
    if username != "" :
       return render(request,'monitor.html',{'data':data,'data2':x_sum,'data3':data3,'data4':data4}) 
       
    else:
        return render(request,'registeradmin.html')
    return render(request, 'monitor.html', {"username" : username})
   
    # device = request.POST('device')
       
    # try:
    #     print(device)
    #     return render(request,'topology.html')
    # except NameError:
    #     print("Error")
    # else:
    #     return render(request,'home.html')
    
    # if request.method == 'POST' and 'device' in request.POST:
    #    device = request.POST['device']
    #    if device is not None and device !='':
    #       data = list(User.objects.filter(username=device).distinct())
    #       return render(request,'monitor.html',{'data':data})
    #    else:
    #         pass

def wlc_ap(request):
    username = request.session['username']
    butthon = request.POST['butthon']
    if butthon == 'butthon' :
        num_wlc = get_clients.objects.all().latest
       
        return render(request, 'monitor.html',{'num_wlc':num_wlc})
    else : return redirect('monitor.html')


def main1(request):
    if request.session.has_key('username'):
       username = request.session.GET['username']
       return render(request, 'main.html', {"username" : username})
    else:
       return render(request, 'index.html', {})
    return render(request,'home.html')


  

def topology(request):
    username = request.session['username']
    
    
    # if request.POST['search'] =='' :
    #     device = request.POST['search']
    #     return render(request,'/infodevice/',device)
    return render(request,'topology.html',{'username':username})

def infodevice(request,serach):
    username = request.session['username']
    #device = serach
    return render(request,'infodevice.html',{'username':username})    

def topology_serach(request):
    username = request.session['username']
    serach = request.POST['serach']
    if serach :
    
        return redirect('/infodevice/',serach)
    #infodevice(serach)

def register(request):
    username = request.session['username']
    data = list(User.objects.filter(username=username).distinct())
    
    return render(request,'register.html',{'data':data})

def report(request):
    data1 = list(get_uptime.objects.all().distinct())
    return render(request,'report.html',{'data':data1})

def addUser(request):
    username = request.session['username']
    username1 = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password==repassword :
        if User.objects.filter(username=username1).exists():
            messages.info(request,'UserName นีมีคนใช้แล้ว')
            return redirect('/registeradmin/')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email นี้เคยลงทะเบียนแล้ว')
            return redirect('/registeradmin/')
        else :
            user =  User.objects.create_user(
                username = username1,
                password = password,
                email = email,
                first_name = firstname,
                last_name = lastname
                )
            user.save()
            msg = ("คุณ : "+username1+" ถูกลงทะเบียนโดย : "+username+" เรียบร้อยกรุณาตรวจสอบ")
            r = requests.post(url, headers=headers , data = {'message':msg})
            messages.info(request,'ลงทะเบียนสำเร็จ')
            return redirect('/registeradmin/')  
    else  :
         messages.info(request,'รหัสผ่านไม่ตรงกัน')
         return redirect('/registeradmin/')   
    
        
       
        # return redirect('/registeradmin/')

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    #check username ,password
    user=auth.authenticate(username=username,password=password)

    if user is not None :
       request.session.set_expiry(86400)
       auth.login(request,user)
       username = user.username
       request.session['username'] = username
       msg = ("เข้าระบบโดย :"+username)
       r = requests.post(url, headers=headers , data = {'message':msg})
       return redirect('home')
    else :
        messages.info(request,'ไม่พบข้อมูล')
        msg = ("พยายามเข้าระบบโดย :"+username)
        r = requests.post(url, headers=headers , data = {'message':msg})
        return redirect('/')
    

def logout(request):
    auth.logout(request)
    user_logout = request.session.get('username', None)
    current_expiry = request.session.get('username')
    if user_logout:
        request.session['username'] = user_logout
        if current_expiry:
           request.session['username'] = current_expiry
           msg = ("ออกจากระบบเเล้ว")
           r = requests.post(url, headers=headers , data = {'message':msg})
    return render(request,'index.html')





