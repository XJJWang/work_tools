import os
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser
from taggit.models import Tag

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
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        
        form = DocumentForm(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                document = form.save()
                return JsonResponse({'status': 'success'})
            except Exception as e:
                print(f"Error saving document: {str(e)}")
                return JsonResponse({
                    'status': 'error',
                    'message': f'保存文件时出错: {str(e)}'
                }, status=400)
        else:
            print(f"Form errors: {form.errors}")
            return JsonResponse({
                'status': 'error',
                'message': str(form.errors)
            }, status=400)
    else:
        form = DocumentForm()

    return render(request, 'files/model_form_upload.html', {
        'form': form
    })

@login_required
def file_list(request):
    tag = request.GET.get('tag')
    if tag:
        documents = Document.objects.filter(tags__name=tag)
    else:
        documents = Document.objects.all()
    return render(request, 'files/file_list.html', {'documents': documents, 'selected_tag': tag})

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

@csrf_exempt
def add_tag(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_tag_name = data.get('new_tag')
            if new_tag_name:
                # 检查标签是否已存在
                tag, created = Tag.objects.get_or_create(name=new_tag_name)
                if created:
                    return JsonResponse({
                        'success': True,
                        'tag_id': tag.pk,
                        'tag_name': tag.name
                    })
                else:
                    return JsonResponse({
                        'success': False,
                        'error': '标签已存在'
                    })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    return JsonResponse({'success': False, 'error': '无效的请求'})
