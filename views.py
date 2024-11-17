from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator('per_page', 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'myblog/post_list.html', {'page_obj': page_obj})




# Create your views here.
