from django.shortcuts import render
# Added Imports
from .models import Category, Photo


def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
        
    else:
        photos = Photo.objects.filter(category__name=category)
        
    categories = Category.objects.all()
    
    context = {
        'categories': categories,
        'photos': photos
    }
    # Form
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
            
        else:
            category = None
            
        photo = Photo.objects.create(
            category=category,
            description = data['description'],
            image = image,
        )
            
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        "photo": photo
    }
    return render(request, 'photos/photo.html', context)

def addPhoto(request):
    return render(request, 'photos/add.html')
