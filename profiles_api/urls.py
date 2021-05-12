from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
# the router will already create 4 routes for us so we don't need to define a forward slash here
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# no need to provide a basename because we have a query set. If we have a queryset
# Django will figure out the name from the model thats assigned to it
router.register('profile', views.UserProfileViewSet)

router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
