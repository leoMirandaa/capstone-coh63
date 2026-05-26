from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Product, Category, Order, OrderItem
from django.contrib.auth.decorators import login_required


# Create your views here.
"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn

"""


class ProductList(ListView):
    model = Product
    template_name = "store/catalog.html"

    def get_queryset(self):
       category = self.request.GET.get("category")

       if not category:
           # no filter, return all
           return Product.objects.all()
       else:
           # filter by category
           # iexact = exact match (ignore casing)
           return Product.objects.filter(category__name__iexact=category)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        return context
    

@login_required
def add_to_cart(request):
    # get the data
    product_id = request.POST.get("product_id")
    if not product_id:
        return redirect("catalog")

    quantity = int(request.POST.get("quantity"))
    user = request.user # logged in user

    product = Product.objects.get(id=product_id)

    # get/create the order
    order, created = Order.objects.get_or_create(
        user=user, 
        paid=False, 
        defaults= { 
            "total": 0, 
            "paid": False 
        }
    )
    order.total = order.total + (product.price * quantity)
    order.save()

    # add the OrderItem to the order
    item = OrderItem.objects.create(
        order=order,
        product=product,
        quantity=quantity
    )
    item.save()

    return redirect("catalog")


@login_required
def cart(request):
    user = request.user

    order = Order.objects.filter(user=user, paid=False).first()
    if not order:
        return render(request, "store/cart.html", {"order": None, "items": []})
    
    items = OrderItem.objects.filter(order=order)

    return render(request, "store/cart.html", {"order": order, "items": items})
