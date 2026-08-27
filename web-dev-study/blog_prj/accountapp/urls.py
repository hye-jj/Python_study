from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # 장고 class 베이스 
from accountapp.views import AccountCreatView, AccountDetailView, \
    AccountUpdateView, AccountDeleteView

# 웹 프로그램을 만들 떄 
app_name = 'accountapp'

# path 순서 path, function, name 
# 기능에 따른 url 필요 - url 만들고 함수 만들어나감.
# as_view: class base view
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),  #name 보통 function 이름과 같다. - 하이퍼링크 할 때도 이용, url 노출 막음
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreatView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
# LoginView.as_view(template_name='login.html') : 기능 콜링, 직접적으로 html 렌더링 자동 수행 - 함수 생성 필요 없음. *함수 매핑 안하고 렌더링.
# as_view : class 를 메모리에 올리면서, render기능까지 가지고있는 기능

# detail int pk : auth_user 의 아이디 - 고유번호
# detail/1 :1번째 auth_user row의 정보 
# pk : view 가 물고있는 db 아이디 - 자동부여됨. 모델 만들때 무조건 자동 pk(primary key) 등록됨.

