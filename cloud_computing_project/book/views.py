from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse, HttpResponse

# Create your views here.
def books_json(request):
    students = Book.objects.all()
    serializer = BookSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)

def book_json(request, id):
    student = Book.objects.get(id=id)
    serializer = BookSerializer(student)
    return JsonResponse(serializer.data, safe=False, status=200)

def book_html(request, id):
    ret = "<html><body><p>"

    b = Book.objects.get(id=id)
    ret += "Name: "
    ret += b.name
    ret += " Author name: "
    ret += b.author_name
    ret += " Year: "
    ret += str(b.year)
    ret += " Price: "
    ret += str(b.price)
    ret += "</p></body></html>"

    return HttpResponse(content=ret, status=200)