from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'Kandarp Parikh',
		'title': 'Blog Post 1',
		'content': 'First Post Content',
		'date_posted': 'July 26 , 2020'

	},
	{
		'author': 'Sharad Parikh',
		'title': 'Blog Post 2',
		'content': 'Second Post Content',
		'date_posted': 'July 26 , 2020'

	},

]


def home(request):
    context = {'posts': posts}    
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})