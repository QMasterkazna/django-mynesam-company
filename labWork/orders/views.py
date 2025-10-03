from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='/register/')
def create_order(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            messages.success(request, "Заявка успешно создана!")
            return redirect('create_order')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form':form, 'orders':orders} )