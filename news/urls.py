from django.urls import URLPattern, path
from news import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('book/<str:book_title>/detail/', views.detail_book_view, name='detail-book'),
    path('book/create/', views.Create_Book_View, name='create-book'),
    path('book/<str:book_review_title>/review', views.CreateReviewView.as_view(), name='review'),
    path('book/search/', views.Search_Book, name='search'),
    path('book/Narrow_down/business/', views.Categorize_by_business, name='narrow-down-business'),
    path('book/Narrow_down/science・Technology/', views.Categorize_by_science_and_Technology, name='narrow-down-science・Technology'),
    path('book/Narrow_down/Humanities・ideas/', views.Categorize_by_Humanities_and_ideas, name='narrow-down-Humanities・ideas'),
    path('book/Narrow_down/computer・IT/', views.Categorize_by_computer_and_IT, name='narrow-down-computer・IT'),
    
]

