from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.base import ContextMixin
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse
from .models import Book,BookInstance,Reviews
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User

def not_in_admin(user):
    return not user.groups.filter(name='Admin').exists() and not user.groups.filter(name='Book Manager').exists()
def in_student(user):
    return  user.groups.filter(name='Student/Teacher').exists() 
@user_passes_test(not_in_admin, login_url='login')
def index(request):
    book_list=Book.objects.order_by('-title')
    
    context={'book_list':book_list}
    
    return render(request,'catalog/index.html',context)
@user_passes_test(not_in_admin, login_url='login')
def SearchView(request):
    model=Book
    if request.method=="POST":
        temlplate_name="catalog/search_results.html"
        query=request.POST.get('q')
        object_list=model.objects.filter(Q(title__icontains=query))
        context={'book_list':object_list}
        return render(request,temlplate_name,context)
class BookDetailView(DetailView):
    model = Book

class ReviewCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Reviews
    fields=['review']
    success_url="/catalog/"
    def get_context_data(self, **kwargs):
        ctx = super(ReviewCreateView, self).get_context_data(**kwargs)
        ctx['Book'] = Book.objects.get(id=self.kwargs['pk'])

        return ctx
    def form_valid(self, form):
        ctx=self.get_context_data()
        form.instance.book=ctx['Book']
        form.instance.Reviewuser = self.request.user
        return super().form_valid(form)
    def test_func(self):
        return self.request.user.groups.fitler(name='Student/Teacher').exists() 
@user_passes_test(in_student, login_url='login')
def ReserveBook(request,pk):
    Instance=BookInstance.objects.get(id=pk)
   
    if request.user.is_authenticated==True:
        if Instance.status=='a':
            Instance.status='r'
            Instance.BookUser=request.user
            Instance.save()
        else:
            messages.error(request, 'BOOK ALREADY RESERRVED')
        return redirect('/catalog/')
    else:
        messages.error(request, 'NEED TO BE LOGIN TO RESERVE BOOK')
        return redirect('login')
"""class ReserveBook(ContextMixin,View):
    model=BookInstance
    def get_context_data(self, **kwargs):
        ctx = super(ReserveBook,self).get_context_data(**kwargs)
        ctx['BookInstance']=BookInstance.objects.get(pk)
        return ctx
    def get(self, request, *args, **kwargs):
        ctx=self.get_context_data()
        ctx['BookInstance'].status="a"
        return redirect('/catalog/')"""