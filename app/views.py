from django.shortcuts import render
from django.db import connection

# Create your views here.

def get():
	return connection.cursor()

def index(request):
	cursor = get()
	cursor.execute("select * from book")
	books = cursor.fetchall()
	return render(request,'index.html',context={"books":books})


def add_book(request):
	return render(request,'add_book.html')


def book_detail(request,book_id):
	return render(request,'book_detail.html')