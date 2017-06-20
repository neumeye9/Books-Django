from django.shortcuts import render
from . models import Books

# Create your views here.

def index(request):
    book = Books.objects.create(title="Pride and Prejudice", author="Jane Austen", published_date="1813-01-28", category="Romance")
    book = Books.objects.create(title="Great Expectations", author="Charles Dickens", published_date="1861-05-31", category="Drama")
    book= Books.objects.create(title="Willy Wonka and the Chocolate Factory", author="Roald Dahl", published_date="1964-01-17", category="Children's Fantasy")
    book = Books.objects.create(title="Green Eggs and Ham", author = "Dr. Seuss", published_date="1960-08-12", category="Chidlren's Literature")
    book = Books.objects.create(title="A Wrinkle In Time", author="Madeleine L'Engle", published_date="1963-05-31", category="Young Adult")

    return render(request,'books_app/index.html')