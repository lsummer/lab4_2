from django.shortcuts import render_to_response,HttpResponse
from books.models import Book, Author
#i am here to show that lab4 i have done!
# Create your views here.
def intr(request):
    book_list =Book.objects.all()
    return render_to_response("intr.html",{'book_list':book_list})
  
def books_insert(request):
    try:
        if request.POST:
            post=request.POST
            name1=post["name"]
            try:
                Author.objects.get(name=name1)
            except Author.DoesNotExist:
                return render_to_response("notfindauthor.html")
            else:
                if Author.objects.get(name=name1):
                    authors_id1 =Author.objects.get(name=name1).id
                    newbook=Book(
                        title = post["title"],
                        authors_id=authors_id1,
                        publisher = post["publisher"],
                        publishdate = post["publishdate"],
                        price = post["price"])
                    newbook.save()
                    return render_to_response("books_successed.html")
        return render_to_response("books_insert.html")
    except:
        return render_to_response("fail.html")      

def author_insert(request):
    try:
        if request.POST:
            post=request.POST
            newauthor = Author(
                 name = post["name"],
                 age = post["age"],  
                 country = post["country"])
            newauthor.save()
            return render_to_response("author_success.html")
        return render_to_response("author_insert.html")
    except:
        return render_to_response("fail.html")  
    
def search_books(request):
    if 'search_name' in request.GET and Author.objects.filter(name=request.GET['search_name']):
        author=Author.objects.get(name=request.GET['search_name'])
        authorid = author.id
        book_list = Book.objects.filter(authors=authorid)       
        return render_to_response('search_books.html', {'book_list':book_list,"author":author})
    else:
        return render_to_response('noa.html')
        
def search(request):
    author_list = Author.objects.all()
    return render_to_response("search.html",{'author_list':author_list})  

def Delete(request):
    get_id = request.GET["id"]
    Book.objects.get(id=get_id).delete()
    Book.objects.all()
    return render_to_response("delete.html")

def full(request):
    get_id = request.GET["id"]
    book=Book.objects.get(id=get_id)
    author=Author.objects.get(id=book.authors_id)
    return render_to_response("fullinformation.html",{"book":book,"author":author})
    
def main(requset):
    return render_to_response("main.html")

def noauthor(request):
    try:
        if request.POST:
            post=request.POST
            newauthor = Author(
                 name = post['name'],
                 age = post["age"],  
                 country = post["country"])
            newauthor.save()
            return render_to_response("books_successed.html")
        return render_to_response("notfindauthor.html")
    except:
        return render_to_response("fail.html")  
    
def update(request):  
    get_id = request.GET["id"]
    book1 = Book.objects.get(id=get_id)
    author=Author.objects.get(id=book1.authors_id)
    try:
        if request.POST:        
            
            post = request.POST
            try:
                Author.objects.get(name=post["name"])
            except Author.DoesNotExist:
                return render_to_response("notfindauthor.html")
            else:
                book1.authors_id = Author.objects.get(name=post["name"]).id
                book1.publisher = post["publisher"]
                book1.publishdate = post["publishdate"]
                book1.price = post["price"] 
                book1.save()
                #book1.objects.all()
                return render_to_response("update_success.html")  
        return render_to_response("update.html", {'book':book1,'author':author}) 
    except:
        return render_to_response("fail.html")  
        
