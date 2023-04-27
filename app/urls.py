from . import views
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('' , views.login_page, name='login'),
    path('login_user' , views.login_user, name='login_user'),
    path('index/' , views.index , name='index'),
    path('logout/' , views.logout_user , name='logout'),

    # urls for categorie admin 
    path('employeurs/' , views.employeurs.as_view() , name='employers'),
    path('materiaux/' , views.materiau.as_view() , name='materiaux'),
    path('holidays_list/' , views.holidays_list , name="holidays_list"),
        # delete
    path('delete_employers/' ,views.delete_models , name='delete_employers' ),
    path('delete_materiaux/' , views.delete_models , name='delete_materiaux'),
    path('delete_date/' , views.delete_models , name='delete_date'),
        # add
    path('add_employer/' , views.add_employer.as_view() , name='add_employer'),
    path('add_materiaux/' , views.add_materiaux.as_view() , name='add_materiaux'),
    path('add_date/' , views.calendrier , name='add_date' ),
        #edit
    path('update_employer/<int:id>' , views.updatemodels , name='update_employer'),
        #calendar
    path('calendrier/' , views.calendrier , name='calendrier'),
    path('calendar_refresh/' , views.refresh_calendar , name='calendar_refresh'),
    path('get_days/' ,views.get_days , name='get_days' ),

]
