from django.urls import path
from .views import PostWorkerView, PostEnterpriseView, EnterpriseView, WorkerView

app_name = 'main'

urlpatterns = [
    path('post_worker/', PostWorkerView.as_view()),
    path('post_enterprise/', PostEnterpriseView.as_view()),
    path('enterprise/', EnterpriseView.as_view()),
    path('worker/', WorkerView.as_view()),
]

