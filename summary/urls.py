from django.urls import path
from . import views

urlpatterns =[
   
    path('pdf2/generate_summary', views.generate_summary_view, name='generate_summary'),
    
    path('pdf2', views.process_pdf_view, name='pdf2'),
    path('', views.homepage, name='homepage'),
    path('text2', views.tool, name='text2'),

    path('random',views.random, name='random' )

    
]