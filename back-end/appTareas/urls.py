from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from appTareas import views

routerTarea=routers.DefaultRouter()
routerTarea.register(r'',views.TareaView,'/tarea')


urlpatterns = [
    path("api/v1/tarea/", include(routerTarea.urls)),
    path("docs/",include_docs_urls(title="Tienda API"))
]


#genera los: GET, POST, PUT, DELETE para cada entidad