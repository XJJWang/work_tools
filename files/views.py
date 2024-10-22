import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser

from .forms import DocumentForm
from .models import Document

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('file_list')  # Redirect to your desired page after login
            else:
                messages.error(request, '用户名或密码错误。')
        else:
            # Handle form errors, e.g., display them in the template
            pass  # Or add specific error handling logic
    else:
        form = AuthenticationForm()

    return render(request, 'files/login.html', {'form': form})

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = DocumentForm()
    return render(request, 'files/model_form_upload.html', {'form': form})

@login_required
def file_list(request):
    documents = Document.objects.all()
    return render(request, 'files/file_list.html', {'documents': documents})

@login_required
def search_files(request):
    query = request.GET.get('q')
    results = []
    if query:
        # 搜索文件名
        results = Document.objects.filter(document__icontains=query)
    return render(request, 'files/search_results.html', {'results': results})

@login_required
def delete_file(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if document.document:
        # 删除文件
        if os.path.isfile(document.document.path):
            os.remove(document.document.path)
    document.delete()
    return redirect('file_list')