from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from post.controller.post_controller import rest as post_api
from post.controller.comment_controller import rest as comment_api
from account.controller import rest as profile_api
from community.controller import rest as community_api
from rest_framework_simplejwt import views as jwt_views
from chat.controller import rest as chat_api
from account.controller import rest as profile_api
from redditv1 import settings
import account
from community.controller import urls as community_urls
from post.controller.post_controller import urls as post_urls
from post.controller.comment_controller import urls as comment_urls
from account.controller import urls as account_urls

urlpatterns = [
    # admin urls
    path('admin/', admin.site.urls),
    # post
    path('api/post/', include(post_urls)),
    # 31
    # comment
    path('api/comment/', include(comment_urls)),
    # 11
    # profile
    path('api/profile/', include(account_urls)),
    # 10
    # community
    path('api/community/', include(community_urls)),
    # 7 community.controller.urls
    # char api
    path('api/chatroom/create/<str:username>', chat_api.create_chat_room),
    path('api/chatroom/chat/<str:username>', chat_api.create_chat),
    path('api/chatroom/view/<str:username>', chat_api.get_chat_view),
    # 6
    # token
    path('api/search/', profile_api.search_v0),
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/login', profile_api.login_via_react_view),
    path('api/logout', profile_api.logout_view_js),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
