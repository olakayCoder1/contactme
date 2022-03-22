from django.shortcuts import redirect, render
from .models import Contacts

# Create your views here.






def index(request):
    contacts = Contacts.objects.order_by('first_name')
    context = { 'contacts': contacts}
    return render(request, 'contacts/home.html', context)

def add_contact(request):
    
    if request.method == "POST":
        if request.POST.get('first-name') == '' or request.POST.get('number') == '':
            return redirect('/')
        contact = Contacts.objects.create(
        first_name = request.POST.get('first-name'),
        last_name = request.POST.get('last-name'),
        email = request.POST.get('email'),
        number = request.POST.get('number'),
        relationship = request.POST.get('relationship'),
        address = request.POST.get('address')
        )
        contact.save()
        return redirect('/')

    return render(request, 'contacts/add.html')


def about_contact(request, id):
    contact = Contacts.objects.get(pk=id)
    context = { 'contact': contact}
    return render(request, 'contacts/about.html', context)


def edit_contact(request, id):
    contact = Contacts.objects.get(pk=id)
    if request.method == "POST": 
        contact.first_name = request.POST.get('first-name')
        contact.last_name = request.POST.get('last-name')
        contact.email = request.POST.get('email')
        contact.number = request.POST.get('number')
        contact.relationship = request.POST.get('relationship')
        contact.address = request.POST.get('address')
        contact.save()
        return redirect('contact/about/'+str(contact.id))
    context = { 'contact': contact}

    return render(request, 'contacts/edit.html', context)

def delete_contact(request, id):
    contact = Contacts.objects.get(pk=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    context = { 'contact': contact}
    return render(request, 'contacts/delete.html', context)


def search_contact(request):
    search_word = request.GET['search']
    result = Contacts.objects.filter(first_name__icontains=search_word)
    return render(request, 'contacts/search.html', {'results': result})