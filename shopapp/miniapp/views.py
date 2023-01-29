from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from miniapp.models import *
from miniapp.form import *

# Create your views here.
def dashboard(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    total=orders.count()
    delivered=Order.objects.filter(status="delivered").count()
    pending=Order.objects.filter(status="pending").count()
    out_for_delivery=Order.objects.filter(status="out for delivery").count()
    return render(request,'dashboard.html',{
        'customers':customers,
        'orders':orders,
        'total':total,
        'delivered':delivered,
        'pending':pending,
        'out_for_delivery':out_for_delivery
    })

def customers(request,id):
    customer=Customer.objects.get(id=id)
    orders=customer.order_set.all()
    order_count=orders.count()
    
    return render(request,'customers.html',{
        'customer':customer,
        'orders':orders,
        'order_count':order_count,
        
    })
    
def customer(request):
    customer=Customer.objects.all()
    return render(request,'customer.html',{
        'customer':customer
    })

def customerCreate(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shopapp/customer')
    else:
        form = CustomerForm()

        return render(request,'customer_form.html',{
        'form':form
    })

def customerUpdate(request,id):
    customer=Customer.objects.get(id=id)
    form = CustomerForm(instance=customer)
    if request.method=="POST":
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/shopapp/customer')

    return render(request,'customer_form.html',{
         'form':form
    })

def customerDelete(request,id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
        customer.delete()
        return redirect('/shopapp/customer')

    return render(request,'customer_delete.html',{
        'customer':customer
    })

def products(request):
    products=Product.objects.all()
    return render(request,'products.html',{
        'products':products
    })

def productCreate(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shopapp/products')
    else:
        form = ProductForm()

        return render(request,'product_form.html',{
        'form':form
    })

def productUpdate(request,id):
    product=Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method=="POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/shopapp/products')

    return render(request,'product_form.html',{
         'form':form
    })

def productDelete(request,id):
    product=Product.objects.get(id=id)
    if request.method=="POST":
        product.delete()
        return redirect('/shopapp/products')

    return render(request,'product_delete.html',{
        'product':product
    })

def orders(request):
    orders=Order.objects.all()
    total=orders.count()
    delivered=Order.objects.filter(status="delivered").count()
    pending=Order.objects.filter(status="pending").count()
    out_for_delivery=Order.objects.filter(status="out for delivery").count()
    return render(request,'orders.html',{
        'orders':orders,
        'total':total,
        'delivered':delivered,
        'pending':pending,
        'out_for_delivery':out_for_delivery
    })

def orderCreate(request,customerId):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer=Customer.objects.get(id=customerId)
    formset = OrderFormSet(instance=customer,queryset=Order.objects.none())
    if request.method=="POST":

        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/shopapp/orders')

    return render(request,'order_form.html',{
        'formset':formset
    })

def orderUpdate(request,orderId):
        order=Order.objects.get(id=orderId)
        form = OrderForm(instance=order)
        if request.method=="POST":
            form = OrderForm(request.POST,instance=order)
            if form.is_valid():
                form.save()
                return redirect('/shopapp/orders')

        return render(request,'order_form.html',{
            'form':form
        })

def orderDelete(request,orderId):
    order=Order.objects.get(id=orderId)
    if request.method=="POST":
        order.delete()
        return redirect('/shopapp/orders')

    return render(request,'order_delete.html',{
        'order':order
    })

def tags(request):
    tags=Tag.objects.all()
    return render(request,'tags.html',{
        'tags':tags
    })

def tagCreate(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shopapp/tags')
    else:
        form = TagForm()

        return render(request,'tag_form.html',{
        'form':form
    })

def tagUpdate(request,id):
    tag=Tag.objects.get(id=id)
    form = TagForm(instance=tag)
    if request.method=="POST":
        form = TagForm(request.POST,instance=tag)
        if form.is_valid():
            form.save()
            return redirect('/shopapp/tags')

    return render(request,'tag_form.html',{
         'form':form
    })

def tagDelete(request,id):
    tag=Tag.objects.get(id=id)
    if request.method=="POST":
        tag.delete()
        return redirect('/shopapp/tags')

    return render(request,'tag_delete.html',{
        'tag':tag
    })