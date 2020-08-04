from django.shortcuts import render

from . import util

from django.http import HttpResponseRedirect, Http404

import random

from django import forms

from django.urls import reverse 

import markdown 

from django.core.files.base import ContentFile



entries = util.list_entries()



class NewEntryForm(forms.Form):
      title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
      content = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8', 'rows' : 10}))  
      


      



def index(request):
    return render( request, "encyclopedia/index.html", {
        "entries": util.list_entries()
         })

def entry(request, title): 
     return render( request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
         "title": f"{title}"
        })

def choose(request):   
     return render( request, "encyclopedia/choose.html",{
        "choose": random.choice(util.list_entries())
        })


def new(request):
   if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
              title = form.cleaned_data["title"]
              content = form.cleaned_data["content"]
              if title in entries:
                  return render( request, "encyclopedia/error.html")
              else:
                  util.save_entry(title, content)
                  entries.append(title)
                  entries.append(content)
                  return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            form = NewEntryForm()
            return render( request, "encyclopedia/new.html",{
             "form":form
        })
             
   return render( request, "encyclopedia/new.html",{
             "form":NewEntryForm()
        })


def e(request, title):
  
    post = util.get_entry(title)
    if post is None: 
        return render(request, "encyclopedia/index.html", { "entries": util.list_entries() })
    
    else:
             form = NewEntryForm()
             form.fields["title"].initial = title
             form.fields["content"].initial = post
             
             
             return render(request, "encyclopedia/edit.html", { "form": form})
    
    
def edit(request, title):
  
    post = util.get_entry(title)
    if post: 
        return render(request, "encyclopedia/slim.html", { "content": post})
    
    else:
       
             
             return render(request, "encyclopedia/index.html", { "entries": util.list_entries()})



def empty(request):
    return render( request, "encyclopedia/empty.html")


def add(request):
    return render( request, "encyclopedia/add.html", {
        "entry": util.list_entries()
         })
      
     
def error(request):
    return render( request, "encyclopedia/error.html")
   
def search(request): 
       post = request.GET.get('q','') 
       if util.get_entry(post):
          return render(request, "encyclopedia/entry.html", {"entry": util.get_entry(post)})
       else: 
          list = [] 
          for entry in util.list_entries(): 
               if post.capitalize() in entry.capitalize():
                  list.append(entry) 
                  return render(request, "encyclopedia/index.html", { "entries": list })
       return render( request, "encyclopedia/empty.html")


def edt(request, entry): 
     entryPage = util.get_entry(entry)
     if entryPage is None:
        return render(request, "encyclopedia/entry.html", { "entry": entry }) 
     else: 
        form = NewEntryForm()
        form.fields["title"].initial = entry  
        form.fields["title"].widget = forms.HiddenInput()
        form.fields["content"].initial = entryPage     
        form.fields["edit"].initial = True
        return render(request, "encyclopedia/newEntry.html", { "form": form, "edit": form.fields["edit"].initial, "entryTitle": form.fields["title"].initial })

         




       



           




     



          
       
       
       



