from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    path('search_polls/', views.searchbar, name='search-polls'),
    # path('<int:question_id>/polldetail/', views.polldetail, name='polldetail'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('tag/<slug:tag_slug>/', views.index, name='poll_list_by_tag'),



]
