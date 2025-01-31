from django.urls import path
from apps.common import views
from django.conf import settings 
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),

    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('kworks/', KworkListCreateView.as_view(), name='kwork-list-create'),

    path('kworks/<int:pk>/', KworkDetailView.as_view(), name='kwork-detail'),

    path('seller-skills/', SellerSkillListCreateView.as_view(), name='seller-skill-list-create'),

    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),

    path('portfolios/', PortfolioListCreateView.as_view(), name='portfolio-list-create'),

    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)