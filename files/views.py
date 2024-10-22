import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser

from .forms import DocumentForm
from .models import Document

# 创建索引目录
if not os.path.exists("indexdir"):
    print('exists indexdir正在使用')
    os.mkdir("indexdir")

# 定义索引的Schema
schema = Schema(content=TEXT(stored=True))

# 创建或打开索引
if not os.listdir("indexdir"):
    print('exists indexdir正在使用')
    ix = create_in("indexdir", schema)
else:
    ix = open_dir("indexdir")

def index_file(filepath):
    writer = ix.writer()
    print('index file正在使用')
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        writer.add_document(content=content)
    writer.commit()

def search(query_str):
    print('serch正在使用')
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query)
        return [hit['content'] for hit in results]

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = DocumentForm()
    return render(request, 'files/model_form_upload.html', {'form': form})

def file_list(request):
    documents = Document.objects.all()
    return render(request, 'files/file_list.html', {'documents': documents})

def search_files(request):
    query = request.GET.get('q')
    results = []
    if query:
        # 搜索文件名
        results = Document.objects.filter(document__icontains=query)
    return render(request, 'files/search_results.html', {'results': results})

def delete_file(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if document.document:
        # 删除文件
        if os.path.isfile(document.document.path):
            os.remove(document.document.path)
    document.delete()
    return redirect('file_list')