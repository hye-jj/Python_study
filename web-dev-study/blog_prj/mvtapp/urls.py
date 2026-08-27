from django.urls import path
from mvtapp.views import detail, result

app_name = 'mvtapp'

# path 순서 path, function, name
urlpatterns = [
    path('detail/', detail, name='detail'),  #name 보통 function 이름과 같다.
    path('result/', result, name='result'),
]

