from django.shortcuts import render , redirect
from .models import Trainer
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def trainers(request):
    trainers = Trainer.objects.all()
    return render( request,'trainers.html',{'trainers':trainers})



from .forms import MemberForm
@login_required
def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')  # we will create this next
    else:
        form = MemberForm()

    return render(request, 'add_member.html', {'form': form})

from .models import Member

from django.utils import timezone

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def member_list(request):
    members = Member.objects.all()
    today = timezone.now().date()

    return render(request, 'member_list.html', {
        'members': members,
        'today': date.today()
    })

from django.shortcuts import get_object_or_404
@login_required
def update_member(request, id):
    member = get_object_or_404(Member, id=id)

    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)

    return render(request, 'add_member.html', {'form': form})
@login_required
def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('member_list')



from django.shortcuts import get_object_or_404
from datetime import date

@login_required
def customer_dashboard(request):
    if request.user.is_staff:
        return redirect('member_list')

    member = get_object_or_404(Member, user=request.user)

    return render(request, 'customer_dashboard.html', {
        'member': member,
        'today': date.today()
    })



from .forms import ContactForm
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})