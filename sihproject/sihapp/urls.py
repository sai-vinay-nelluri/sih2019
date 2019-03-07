from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login_user, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('ajax/grp/all', views.ajax_grp_whole, name="ajax-grp-all"),
    path('populate', views.populate, name="populate"),
    path('sale', views.sale, name="sale"),
    path('ajax/grp/<str:type>', views.ajax_grp_type, name="ajax-grp-type"),
    path('suggest', views.suggest, name="suggest"),
    path('logout', views.logout_user, name="logout")
]