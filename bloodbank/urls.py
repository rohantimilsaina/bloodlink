from django.urls import path
from . import views,func,camp,profile

urlpatterns = [
    path('', views.BloodAndCamp, name='home'),
    path('blood/create/', views.blood_create, name='blood_create'),
    path('blood/list/', views.blood_list, name='blood_list'),
    path('blood/update/<int:pk>/', views.blood_update, name='blood_update'),
    path('blood/delete/<int:pk>/', views.blood_delete, name='blood_delete'),
    path("about_us",views.about_us,name="about_us"),
    path('contact-us/', views.contact_us, name='contact_us'),


    # URLs for Campaign CRUD operations
    path('signup',func.signup,name="signup"),
    path('login',func.user_login,name="login"),
    path("logout",func.user_logout,name="logout"),
    
    
    
    
    path("update_provider",views.provider_profile_create,name="update_provider"),
    path("provider_profile",views.provider_profile,name="provider_profile"),
    path("provider_profile/<int:id>/",views.provider_profile_for_user,name="provider_profile_availa"),

    path('update_profile_user/<int:id>/', profile.update_profile_user, name='update_profile_user'),
    
    path("update_profile_bloodbank/<int:id>/",views.update_profile_bloodbank,name="update_profile_bloodbank"),
]

urlpatterns += [
    path('campaign_list/', camp.campaign_list, name='campaign_list'),
    path('campaign/<int:id>/', camp.campaign_detail, name='campaign_detail'),
    
    path('campaign/create/', camp.campaign_create, name='campaign_create'),
    path('campaign/<int:pk>/update/', camp.campaign_update, name='campaign_update'),
    path('campaign/<int:pk>/delete/', camp.campaign_delete, name='campaign_delete'),
]

urlpatterns += [
    path('profile_create/', profile.profile_create, name='profile_create'),
    path('update_profile_user/<int:id>/', profile.update_profile_user, name='update_profile_user'),
    path('user_profile/', profile.user_profile, name='user_profile'),
    path('view_availablity/', profile.view_availablity, name='view_availablity'),
    path('blood/search/', profile.blood_search, name='blood_search'),
]

urlpatterns += [
    path('terms/', views.terms_and_conditions, name='terms'),
    path('privacy_concern/', views.privacy_concern, name='privacy_concern'),   
]

