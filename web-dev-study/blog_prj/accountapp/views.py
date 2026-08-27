from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# from django.shortcuts import render
from django.views import generic 

# 장고 기능 이용, class 매핑 가능 - Class Base View 방식, 함수이용하는거는 FBV 방식
# 다루고자 하는 것 : CRUD - 떄문에 껍데기, 반복적으로 코딩되는 것을 generic 클래스에 다 구현해둠.

# Create your views here.
# AccountCreatView, AccountDetailView, AccountUpdateView, AccountDeleteView
class AccountCreatView(generic.CreateView):
    model=User  # 모델연결
    form_class=UserCreationForm  # user 생성 화면에 보여지는 폼, User 모델과 연결된 폼.
    success_url = reverse_lazy("mvtapp:detail") # 계정생성 성공하면 보내지는 url, 상속class 함수 오버라이딩
    template_name='accountapp/create.html' # 랜더링되는 html
    context_object_name = 'objUser'  # 아무렇게 지정해도 됨. 
    # DB 정보 - 그 정보를 담을 이름. - Create 할 때는 없어도 상관없음. 
    # DB 넣었다가 빼오지 않으니까. 그런데, class 베이스 뷰는 5개를 반드시 오버라이딩 해야함. 


# detail 보고자하는 테이블, form 없음. 입력받는 거 없음. 그것에 대한 성공, 실패 필요없음
# 위의 5가지 중 3개만 있으면 됨.
class AccountDetailView(generic.DetailView):
    model=User
    template_name = 'accountapp/detail.html'
    context_object_name = 'objUser' # 랜더링시 데이터 담아가는 이름. 
    # 연결된 db 의 해당 user 에 대한 정보를 담아서 html 랜더링 할때 붙여줌.

class AccountUpdateView(generic.UpdateView):
    pass

class AccountDeleteView(generic.DeleteView):
    pass
