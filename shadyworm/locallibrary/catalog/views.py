from django.shortcuts import render

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_instances_not_available = BookInstance.objects.filter(status__exact='o').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances_available': num_instances_available,
        'num_instances_not_available': num_instances_not_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
        
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
     
class BookDetailView(generic.DetailView):
    model = Book
    
    from django.shortcuts import get_object_or_404

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})
        
from django.views import generic

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    
class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author
    
