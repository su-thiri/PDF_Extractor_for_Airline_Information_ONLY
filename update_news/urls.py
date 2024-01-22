from django.urls import path
from .views import upload_image, generated,upload_list,agent_generate

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('generated/<int:pk>/', generated, name='generated'),
    path('upload_list/',upload_list,name="upload_list"),
    path('agent_generate/<int:pk>/',agent_generate,name="agent_generate")
]
