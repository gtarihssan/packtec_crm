from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate , login , logout , update_session_auth_hash
from django.http import HttpResponseRedirect
from .forms import LoginUserForm  ,employerform ,materiauxform,holidaysform , userform
from django.views.generic.edit import FormView , UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import employer , materiaux , holidays
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
import calendar
from datetime import datetime
import datetime as dt
from datetime import datetime , timedelta
import json
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm


# Create your views here.

#=========== working on =======================
@login_required(login_url='login')
def index(request):
    emplye=request.user.employer
    context={
        'operator' : emplye
    }
    return render(request , 'app/index.html' , context)


#===================== views for urls and mechanisme of the categorie admin ==============================
class employeurs(LoginRequiredMixin,ListView):
    template_name = 'app/employer.html'
    model = employer
    context_object_name = 'employeurs'
    paginate_by = 10
    login_url = '/login/'

def delete_models(request):
    if request.method =='POST':
        if request.path == '/delete_employers/':
            print('employers deletation')
            users_id=request.POST.getlist("models_ids")
            users_id_int=[int(x) for x in users_id]
            employers=employer.objects.filter(id__in=users_id_int)
            for i in employers:
                i.user.delete()
        elif request.path == '/delete_materiaux/' :
            print('materiaux deletation')
            materiau_ids=request.POST.getlist("models_ids")
            materiaux_id_int=[int(x) for x in materiau_ids]
            materiau=materiaux.objects.filter(id__in=materiaux_id_int)
            for i in materiau:
                i.delete()
            return redirect('/materiaux/')
        elif request.path == '/delete_date/':
            print('dates deletation')
            date_ids=request.POST.getlist("models_ids")
            date_id_int=[int(x) for x in date_ids]
            dates=holidays.objects.filter(id__in=date_id_int)
            for i in dates:
                i.delete()
            return redirect('/holidays_list/')

    return redirect('/employeurs/')




def updatemodels(request , id):
    emp=employer.objects.get(id=id)
    user=emp.user
    form=userform(instance=user)
    employerforme=employerform(instance=emp)
    if request.method =='POST':
        form=userform(request.POST , instance=user)
        employerforme=employerform(request.POST , instance=emp)
        if form.is_valid() and employerforme.is_valid():
            empp=employerforme.save(commit=False)
            userr=form.save(commit=False)
            empp.mdp=form.cleaned_data['password2']
            empp.save()
            userr.set_password(form.cleaned_data['password2'])
            userr.save()
            return redirect('/employeurs/')
    return render(request, 'app/models_form.html', {'form':form , 'employerforme':employerforme})


class materiau(LoginRequiredMixin , ListView):
    template_name = 'app/materiaux.html'
    model = materiaux
    context_object_name = 'materiels'
    paginate_by = 10
    login_url = '/login/'

class add_employer(LoginRequiredMixin , FormView):
    template_name = 'app/models_form.html'
    form_class = userform
    success_url = reverse_lazy('employers')
    form_class_second  = employerform

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['employerforme'] = employerform
        return context


    def form_valid(self, form ,employerform ,request): # should add messages for the submitation
        p1=form.cleaned_data['password1']
        p2=form.cleaned_data['password2']
        if p1!=p2 :
            messages.error(request , "verifier votre mot de pass")
            return self.form_invalid(form)
        elif User.objects.filter(username=form.cleaned_data['username']).exists():
            return self.form_invalid(form)
        else : 
            username=form.cleaned_data['username']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            password=form.cleaned_data['password1']
            user=User.objects.create_user(username=username , first_name=first_name , last_name=last_name , password=password)
            user.save()
            emp=employerform.save(commit=False)
            emp.user=user
            emp.mdp=password
            emp.save()
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form_second = employerform(request.POST)

        if form.is_valid() and form_second.is_valid():
            return self.form_valid(form, form_second , request)
        else:
            return self.form_invalid(form)

class add_materiaux(LoginRequiredMixin , FormView):
    template_name ='app/models_form.html'
    form_class = materiauxform
    success_url = reverse_lazy('materiaux')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
#================  working on the calendar !!!!

@login_required(login_url='login')    
def calendrier(request):
    days=calendar.monthrange(2023 , 1)
    x=[i for i in range(1,days[1]+1)]
    fdir=8-days[0]  # first day in the rest weeks (7 - b_days + 1)
    if (days[1]-(fdir+20))<7:
            weeks_rest=[
        range(fdir , fdir+7),
        range(fdir+7 , fdir+14),
        range(fdir+14 , fdir+21),
        range(fdir+21 , days[1]+1)
    ]
    else :
        weeks_rest=[
        range(fdir , fdir+7),
        range(fdir+7 , fdir+14),
        range(fdir+14 , fdir+21),
        range(fdir+21 , fdir+28),
        range(fdir+28 , days[1]+1),
        ]
    context={'days' : x  ,
              'first_week' : range(7) ,
              'b_days' : -days[0],#the days that match with the previous month and i turn it to negative to use the add filtre (line 31 calednrier.html)
              'rest_weeks' : weeks_rest,
              'month_days' : days[1],
              'last_days' : range((35-days[0])-days[1]),
              'form' : holidaysform,
              'holidays' : holidays.objects.all()
              } 
    
    print(holidays.objects.all())
    
    return render(request , 'app/calendrier.html' , context )


def refresh_calendar(request): # refresh calender with ajax
    month=request.GET.get('month')
    year=request.GET.get('year')

    days=calendar.monthrange(int(year) , int(month))
    x=[i for i in range(1,days[1]+1)]
    fdir=8-days[0]  # first day in the rest weeks (7 - b_days + 1)
    if (days[1]-(fdir+21))<7: 
        nbr_weeks=4
    else : 
        nbr_weeks=5
    context={'days' : x  ,
              'b_days' : days[0],#the days that match with the previous month and i turn it to negative to use the add filtre (line 31 calednrier.html)
              'fdir':fdir,
              'last_day':days[1],
              'nbr_weeks':nbr_weeks
              }
    return JsonResponse(context)

def count_weekends(start_date, end_date):
    days = (end_date - start_date).days 
    weekends = 0
    for i in range(days):
        date = start_date + dt.timedelta(i)
        if date.weekday() >= 5:
            weekends += 1
    return weekends

def get_days(request):  
    start_day=request.POST.get('start_date')
    end_day=request.POST.get('end_date')
    occasion=request.POST.get('occasion')
    list_weekends=json.loads(request.POST.get('weekends_list'))
    days_list=[]
    d1=(datetime.strptime(start_day , '%Y-%m-%d'))
    if end_day!='':     
        d2=(datetime.strptime(end_day , '%Y-%m-%d'))
    else:
         d2=d1
    dv=d1
    while dv<=d2:
        days_list.append(dv.date().isoformat())
        dv+=timedelta(days=1)
    print(days_list)
    nbr_days=len(days_list) # i add 1 because i want to pick not from day 1 to 2 but inmpelemnt the two days within the days number
    net_days=nbr_days-len(list_weekends)
    holiday=holidays.objects.create(
        first_day=d1,
        last_day=d2,
        occasion=occasion,
        days=days_list,
        weekends=list_weekends
    ).save()


    data={
        'success':'success'
    }
    return JsonResponse(data)

    #holidays list 
def holidays_list(request):
    holiday=holidays.objects.all()
    return render(request , 'app/holidays_list.html' , {'holidays':holiday})

#==================== end calendar ================================


#============================================================

# logout
def logout_user(request):
    logout(request)
    return redirect('login')

# loading the login page 
def login_page(request):
    if request.user.is_authenticated:
        user=request.user
        id=employer.objects.get(user=user).id
        return redirect('index/')
    return render(request , 'app/login.html' ,{'form' : LoginUserForm})

# this function related with ajax to verife if the user authenticate or not
def login_user(request):
    username=request.POST.get('username').rstrip()
    password=request.POST.get('password')
    
    user = authenticate(username = username , password = password)
    if not User.objects.filter(username=username).exists():
        messages.error(request , 'username worng')
        return login_page(request)
    elif user is None:
        messages.error(request ,'username or password wrong ')
        return login_page(request)
    else : 
        emplye=employer.objects.get(user=user)
        login(request , user)
        messages.success(request , 'connect')
        return redirect('index/')        
    

    
        


    