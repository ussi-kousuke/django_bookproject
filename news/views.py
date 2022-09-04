import environ
from django.shortcuts import render, redirect
from django.urls import  reverse, reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Avg, Q,  Prefetch
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from news.models import  Book, Review
from news.forms import BookForm
from news.consts import ITEM_PER_PAGE
import requests
from pprint import pprint
from apiclient.discovery import build

# Create your views here.

env = environ.Env()
env.read_env('.env')

REQUEST_URL = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404'
APP_ID = env('APP_ID', str)

YOUTUBE_DATE_API_ID = env('YOUTUBE_DATE_API_ID', str)

DEVELOPER_KEY = YOUTUBE_DATE_API_ID
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

GOOGLE_API_KEY = env('GOOGLE_API_KEY', str)

CUSTOM_SEARCH_ENGINE_ID = env('CUSTOM_SEARCH_ENGINE_ID', str)



def index_view(request):
 
    object_list = Book.objects.order_by('-id')
    # paginator = Paginator(object_list, ITEM_PER_PAGE)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.page(page_number)
    book_information_list = []

    for item in object_list:
        paramas = {
        'applicationId': APP_ID,
        'format': 'json',
        'title': item.title,
    }
    
    
        response = requests.get(REQUEST_URL, paramas).json()["Items"][0]['Item']

        for key in list(response):
            if not key in ['author', 'itemCaption', 'title', 'itemPrice', 'itemUrl', 'largeImageUrl', 'publisherName',  'salesDate']:
                del response[key]
        

        book_information_list.append(response)

        
    
    context = {
        'page_obj': book_information_list,
    }

   
    return render(request, 'book/index.html', context)
    



def detail_book_view(request, book_title):

    detailbookview = DetailBooKView(book_title)
    book_information_list = detailbookview.get_book_detail_date_with_rakuten_API()
    youtube_video_url_dict = detailbookview.get_youtube_video_url()
    Google_search_result_date_url = detailbookview.get_Google_search_result_date_url()
    review_book_list = detailbookview.get_review_book_date()
   

    context = {
        'page_obj': book_information_list,
        'book_title':book_title,
        'youtube_video_url_dict': youtube_video_url_dict,
        'Google_search_result_date_url': Google_search_result_date_url,
        'review_book_list': review_book_list,
        
    }
    
    
    

    return render(request, 'book/book_detail.html', context)



def Create_Book_View(request):
    if request.method == 'POST':
        obj = Book()
        form = BookForm(request.POST, instance=obj)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(to='index')
        

    context = {
        'BookForm': BookForm(),
   }
    
    return render(request, 'book/book_create.html', context)
    


class CreateReviewView(CreateView, LoginRequiredMixin):
    template_name = 'book/review_form.html'
    model = Review
    fields = ('book', 'title', 'text', 'rate')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.filter(title__icontains=self.kwargs['book_review_title'])
        print(context)
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('index')
   


def Search_Book(request):
    object_list = Book.objects.order_by('-id')
    keyword = request.GET.get('keyword')
    if keyword:
        object_list = object_list.filter(
            Q(title__icontains=keyword)
        )
        messages.success(request, '{}の検索結果'.format(keyword))
    
    
        book_information_list = []
        
        for item in object_list:
            paramas = {
            'applicationId': APP_ID,
            'format': 'json',
            'title': item.title,
        }
        
        
            response = requests.get(REQUEST_URL, paramas).json()["Items"][0]['Item']
            for key in list(response):
                if not key in ['author', 'itemCaption', 'title', 'itemPrice', 'itemUrl', 'largeImageUrl', 'publisherName',  'salesDate']:
                    del response[key]

            book_information_list.append(response)

    context = {
        'page_obj': book_information_list,
    }


    return render(request, 'book/book_search.html', context)

    
def Categorize_by_business(request):

    object_list = Book.objects.filter(category='business')
    # paginator = Paginator(object_list, ITEM_PER_PAGE)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.page(page_number)

    book_information_list = []
    
    for item in object_list:
        paramas = {
        'applicationId': APP_ID,
        'format': 'json',
        'title': item.title,
    }
    
    
        response = requests.get(REQUEST_URL, paramas).json()["Items"][0]['Item']
        for key in list(response):
                if not key in ['author', 'itemCaption', 'title', 'itemPrice', 'itemUrl', 'largeImageUrl', 'publisherName',  'salesDate']:
                    del response[key]

        book_information_list.append(response)
    
    context = {
        'page_obj': book_information_list,
    }
    
    return render(request, 'book/categorize_by_category.html' ,context)
    

def Categorize_by_science_and_Technology(request):
    
    object_list = Book.objects.filter(category='science ・Technology')
    # paginator = Paginator(object_list, ITEM_PER_PAGE)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.page(page_number)
    book_information_list = []
    
    for item in object_list:
        paramas = {
        'applicationId': APP_ID,
        'format': 'json',
        'title': item.title,
    }
    
    
        response = requests.get(REQUEST_URL, paramas).json()["Items"][0]['Item']

        for key in list(response):
                if not key in ['author', 'itemCaption', 'title', 'itemPrice', 'itemUrl', 'largeImageUrl', 'publisherName',  'salesDate']:
                    del response[key]

        book_information_list.append(response)
    
    context = {
        'page_obj': book_information_list,
    }
    
    
    return render(request, 'book/categorize_by_category.html' ,context)


def Categorize_by_Humanities_and_ideas(request):
    
    object_list = Book.objects.filter(category='Humanities・ideas')
    # paginator = Paginator(object_list, ITEM_PER_PAGE)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.page(page_number)
    book_information_list = []
    
    for item in object_list:
        paramas = {
        'applicationId': APP_ID,
        'format': 'json',
        'title': item.title,
    }
    
    
        response = requests.get(REQUEST_URL, paramas).json()["Items"][0]['Item']

        for key in list(response):
            if not key in ['author', 'itemCaption', 'title', 'itemPrice', 'itemUrl', 'largeImageUrl', 'publisherName',  'salesDate']:
                del response[key]
       

        book_information_list.append(response)
    
    context = {
        'page_obj': book_information_list,
    }
    
    return render(request, 'book/categorize_by_category.html' ,context)

def Categorize_by_computer_and_IT(request):
    
    object_list = Book.objects.filter(category='computer・IT')
    # paginator = Paginator(object_list, ITEM_PER_PAGE)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.page(page_number)
    book_information_list = []
    
    for item in object_list:
        paramas = {
        'applicationId': APP_ID,
        'format': 'json',
        'title': item.title,
    }
    
    
        response = requests.get(REQUEST_URL, paramas).json()["Items"][0]['Item']

        for key in list(response):
            if not key in ['author', 'itemCaption', 'title', 'itemPrice', 'itemUrl', 'largeImageUrl', 'publisherName',  'salesDate']:
                del response[key]
        

        book_information_list.append(response)
    

    context = {
        'page_obj': book_information_list,
    }
   
    
    return render(request, 'book/categorize_by_category.html' ,context)


def Categorize_by_assesment(request):
    
    object_list = Book.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')
    # paginator = Paginator(object_list, ITEM_PER_PAGE)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.page(page_number)
    book_information_list = []
        
    for item in object_list:
            paramas = {
            'applicationId': APP_ID,
            'format': 'json',
            'title': item.title,
    }
        
        
            response = requests.get(REQUEST_URL, paramas).json()["Items"][0]['Item']
            for key in list(response):
                if not key in ['author', 'itemCaption', 'title', 'itemPrice', 'itemUrl', 'largeImageUrl', 'publisherName',  'salesDate']:
                    del response[key]
                
            book_information_list.append(response)
        
    context = {
            'page_obj': book_information_list,
    }
   
    return render(request, 'book/categorize_by_category.html' ,context)




class DetailBooKView(object):
    
    def __init__(self, book_title) -> None:
        self.book_title = book_title
        
    

    def get_book_detail_date_with_rakuten_API(self):
        object_list = Book.objects.filter(title__icontains=self.book_title)
        book_information_list = []
        for item in object_list:
            paramas = {
                'applicationId': APP_ID,
                'format': 'json',
                'title': item.title,
            }
    

        response = requests.get(REQUEST_URL, paramas).json()['Items'][0]['Item']

        for key in list(response):
            if not key in ['author', 'itemCaption', 'title', 'itemPrice', 'itemUrl', 'largeImageUrl', 'publisherName',  'salesDate']:
                del response[key]

        book_information_list.append(response)
        
        return book_information_list

    def get_youtube_video_url(self):
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        youtube_video_url_dict = {}


        search_response = youtube.search().list(
            part="snippet",
            order="viewCount",
            maxResults=20,
            q=self.book_title,
        )
        

        search_response = search_response.execute()['items']
        

        for search_result in search_response:
            if self.book_title in search_result['snippet']['title']:

                youtube_title = search_result['snippet']['title']

                youtube_video_id = search_result['id']['videoId']
                youtube_video_url = f'https://www.youtube.com/watch?v={youtube_video_id}'

                youtube_video_url_dict[youtube_title] = youtube_video_url
     
            else:
                pass

            if len(youtube_video_url_dict) == 5:
                break
        
        return youtube_video_url_dict

    def get_Google_search_result_date_url(self):
        Google_search_result_date_url = {}
        keyword = f'{self.book_title} 書評'  

        search_book_review_date = build('customsearch',
                'v1',
                developerKey=GOOGLE_API_KEY)

        result_book_review_date = search_book_review_date.cse().list(q=keyword,
                        cx=CUSTOM_SEARCH_ENGINE_ID,
                        lr='lang_ja',
                        num=10,
                        start=1).execute()

        result_book_review_date = result_book_review_date['items']


        
        
        for title in result_book_review_date:

            search_result_title = title['title']
            search_result_link = title['link']
            Google_search_result_date_url[search_result_title] = search_result_link


        return Google_search_result_date_url
    
    def get_book_primary_key(self):
        
        object_list = Book.objects.filter(title__icontains=self.book_title)
        id = 0
        for object in object_list:
            id += object.id
        return id
        
    
    def get_review_book_date(self):
        object_list = Book.objects.filter(title__icontains=self.book_title)
        review_book_list = Review.objects.filter(book__in=object_list)
        return review_book_list
        
        
        

        


    


    


