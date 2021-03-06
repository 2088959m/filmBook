from django.conf.urls import patterns, url
from movies import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^genre/(?P<genre_name_slug>[\w\-]+)/$', views.genre, name='genre'),
                       url(r'^movie/(?P<movie_name_slug>[\w\-]+)/$', views.movie, name='movie'),
                       url(r'^actor/(?P<actor_name_slug>[\w\-]+)/$', views.actor, name='actor'),
                       url(r'^genres/$', views.genres, name='genres'),
                       url(r'^actors/$', views.actors, name='actors'),
                       url(r'^add_movie/$', views.add_movie, name='add_movie'),
                       url(r'^user/(?P<username>[\w\-]+)/profile_registration/$', views.user_profile_registration, name='user_profile_details'),
                       url(r'^user/(?P<username>[\w\-]+)/edit_profile/$', views.edit_profile, name='edit_profile'),
                       url(r'^(?P<movie_slug>[\w\-]+)/add_character/$', views.add_character, name='add_character'),
                       url(r'^(?P<movie_slug>[\w\-]+)/add_actor/$', views.add_actor, name='add_actor'),
                       url(r'^(?P<movie_slug>[\w\-]+)/edit_movie/$', views.edit_movie, name='edit_movie'),
                       url(r'^assign_actor/$', views.assign_actor, name='assign_actor'),
                       url(r'^(?P<movie_slug>[\w\-]+)/apply/$', views.send_notification, name='apply'),
                       url(r'^search/$', views.search, name='search'),
                       url(r'^user/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
                       url(r'^rate/$', views.rate, name='rate'),
                       url(r'^add_to_watchlist/$', views.add_to_watchlist, name='watchlist'),
                       )
