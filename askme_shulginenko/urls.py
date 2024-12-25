from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('ask/', views.ask, name='ask'),
    path('question/<int:q_id>/', views.question_page, name='question'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('profile/edit/', views.profilesettings, name='profile'),
    path('tag/<str:tag_label>', views.tag, name='tag'),
    path('hot/', views.hot, name='hot'),
    path('logout', views.logout_view, name="logout"),
    path('like/question', views.like_question, name='like_q'),
    path('like/answer', views.like_answer, name='like_a'),
    path('answer/correct', views.correct, name='correct'),

    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
