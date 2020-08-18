from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(Product.objects.get(id=int(request.POST["product-id"])).price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

    return redirect('/post_checkout')

def checkout_display(request):
    all_orders = Order.objects.all()
    sum_total = 0
    count = 0

    for curr_order in all_orders:
        sum_total += curr_order.total_price
        count += curr_order.quantity_ordered
    
    context = {
        "order": Order.objects.last(),
        "all_prices": sum_total,
        "count": count
    }
    return render(request, "store/checkout.html", context)