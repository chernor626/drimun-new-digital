from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.programs, name='programs'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('events/<slug:event_slug>/', views.event_detail, name='event_detail'), 
    path('impact/', views.impact, name='impact'),
    path('contact/', views.contact, name='contact'),
    path('get-involved/', views.get_involved, name='get_involved'),
    path('apply/', views.application, name='application'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('partner/', views.partner, name='partner'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('programs/conference/', views.conference, name='conference'),
    path('programs/leadership/', views.leadership, name='leadership'),
    path('programs/peacebuilding/', views.peacebuilding, name='peacebuilding'),
    path('programs/protocol/', views.protocol, name='protocol'),
    path('programs/gender/', views.gender, name='gender'),
    path('programs/mentorship/', views.mentorship, name='mentorship'),
]