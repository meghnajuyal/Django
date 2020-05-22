from django.urls import path,re_path
from blog_app import views


urlpatterns=[
   path('',views.PostListView.as_view(),name='postlist'),
   path('about/',views.AboutView.as_view(),name='aboutview'),
   re_path('^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='detailview'),
   path('post/new/',views.CreatePostView.as_view(),name='create_post'),
   re_path('^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_delete'),
   re_path('^post/(?P<pk>\d+)/edit/$',views.UpdatePostView.as_view(),name='post_edit'),
   path('drafts/',views.DraftListView.as_view(),name='post_draft'),
   re_path('^post/(?P<pk>\d+)/comment/$',views.add_comment_post,name="add_comment"),
   re_path('^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name="comment_approve"),
   re_path('^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name="comment_remove"),
    re_path('^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

]
