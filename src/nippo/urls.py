from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.NippoListView.as_view(), name="nippo-list"),
    path("detail/<int:number>/", views.nippoDetailView,name="nippo-detail"),
    path("create/<int:pk>/",views.nippoUpdateFormView,name="nippo-create"),
    path("delete/<int:pk>/", views.nippoDeleteView, name="nippo-delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)