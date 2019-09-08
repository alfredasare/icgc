from django.conf.urls import url
from . import views

app_name = 'newwine'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url('^about/$', views.AboutView.as_view(), name='about'),
    url(r'^executives/$', views.ExecutiveView.as_view(), name='executives'),
    url(r'^department/$', views.DepartmentView.as_view(), name='department'),
    url(r'^documents/$', views.DocumentsView.as_view(), name='documents'),
    url(r'^images/$', views.ImagesView.as_view(), name='images'),
    url(r'^sermons/$', views.SermonsView.as_view(), name='sermons'),
    url(r'^videos/$', views.VideosView.as_view(), name='videos'),
    url(r'^registration/$', views.RegistrationFormView.as_view(), name='registration'),
    url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),
    url(r'^department/(?P<pk>[0-9]+)/$', views.DepartmentView.as_view(), name='detail'),
    url(r'^theme/$', views.ThemeListView.as_view(), name='theme'),
    url(r'^gender-coordinators/$', views.GenderListView.as_view(), name='gender'),
    url(r'^articles/$', views.ArticlesListView.as_view(), name='articles'),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.ArticlesDetailView.as_view(), name='article-details'),
    url(r'^testimonies/$', views.TestimonyListView.as_view(), name='testimonies'),
    url(r'^testimonies/(?P<pk>[0-9]+)/$', views.TestimonyDetailView.as_view(), name='testimony-details'),
    url(r'^teachings/$', views.NoteListView.as_view(), name='teachings'),
    url(r'^teachings/(?P<pk>[0-9]+)/$', views.NoteDetailView.as_view(), name='teaching-details'),
    url(r'^bible-study-outlines/$', views.OutlineListView.as_view(), name='outlines'),
    url(r'^bible-study-outlines/(?P<pk>[0-9]+)/$', views.OutlineDetailView.as_view(), name='outline-details'),
    url(r'^team/(?P<pk>[0-9]+)/$', views.TeamsListView.as_view(), name='team-detail'),
    url(r'^coordinator/(?P<pk>[0-9]+)/$', views.CoordinatorListView.as_view(), name='coordinator')
]
