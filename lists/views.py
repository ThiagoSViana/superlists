from django.shortcuts import render, redirect
from lists.models import List, Item

def new_list(request):
    # Create a new list
    list_ = List.objects.create()
    
    # Create a new item with text and priority if provided
    Item.objects.create(
        text=request.POST['item_text'],
        priority=request.POST.get('item_priority', 'prioridade baixa'),  # Default priority if not provided
        list=list_
    )
    
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    # Get the existing list by ID
    list_ = List.objects.get(id=list_id)
    
    # Create a new item with text and priority if provided
    Item.objects.create(
        text=request.POST['item_text'],
        priority=request.POST.get('item_priority', 'prioridade baixa'),  # Default priority if not provided
        list=list_
    )
    
    return redirect(f'/lists/{list_.id}/')
