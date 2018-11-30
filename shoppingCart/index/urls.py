from django.conf.urls import url
from index import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout_user/$', views.LogoutUserView.as_view(), name='logout_user'),
    url(r'^add_to_cart/(?P<item_id>[-\w]+)/$', views.AddToCart, name='add_to_cart'),
    url(r'^cart/$', views.CartView.as_view(), name='cart'),
]