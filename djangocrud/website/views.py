from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddCustomerForm,AddProductForm
from.models import *
# Create your views here.

def home(request):
  Customers = Customer.objects.all()
  Products = Product.objects.all()
  
  #check to see if logging in
  if request.method=="POST":
    username = request.POST['username']
    password =request.POST['password']
    
    #authenticate
    user = authenticate(request,username=username,password=password)
    
    if user is not None:
      login(request,user)
      messages.success(request,"you have been logged in")
      return redirect('home')
    else:
      messages.success(request,"there was an error logging in please try again...")
      return redirect('home')
  
  else:
    return render(request,'home.html',{'customer':Customers,'product':Products})



def logout_user(request):
  logout(request)
  messages.success(request,'you have logged out...')
  return redirect('home')
  



def customer_record(request,pk):
    if request.user.is_authenticated:
      customer_record = Customer.objects.get(id=pk)
      return render(request,'record.html',{'customer_record':customer_record}) 
    else:
      messages.success(request,'you must be logged in to view that page')
      return redirect('home')
  
def delete_customer_record(request,pk):
  if request.user.is_authenticated:
    delete_cust = Customer.objects.get(id=pk)
    delete_cust.delete()
    messages.success(request,'Recored deleted successfully')
    return redirect('home')
  else:
    messages.success(request,'You need to login to delete Record')
    return redirect('home')

def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
      if request.method == "POST":
        if form.is_valid():
          add_customer = form.save()
          messages.success(request,"Customer added")
          return redirect('home')     
      return render(request,'addcustomer.html',{"form":form})
    else:
      messages.success(request,"you need to be logged in")
      return redirect('home')
    

 
      
def update_customer_record(request,pk):
  if request.user.is_authenticated:
    current_customer = Customer.objects.get(id=pk)
    form = AddCustomerForm(request.POST or None,instance=current_customer)
    if form.is_valid():
      form.save()
      messages.success(request,"Customer Detail has been updated")
      return redirect('home') 
    return render(request,'updatecustomer.html',{"form":form})
  else:
    messages.success(request,"you need to be logged in")
    return redirect('home') 
  

 
def product_record(request,pk):
    if request.user.is_authenticated:
      product_record = Product.objects.get(id=pk)
      return render(request,'product.html',{'product_record':product_record}) 
    else:
      messages.success(request,'you must be logged in to view that page')
      return redirect('home') 
    

def add_product(request):
  if request.user.is_authenticated:
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            add_product = form.save()
            add_product.user = request.user
            add_product.save()
            messages.success(request, "Product added")
            return redirect('home')
    else:
        form = AddProductForm()
    return render(request, 'addproduct.html', {"form": form}) 
  else:
      messages.success(request,"you need to be logged in to add product")
      return redirect('home')
  
def delete_product_record(request,pk):
  if request.user.is_authenticated:
    delete_prod = Product.objects.get(id=pk)
    delete_prod.delete()
    messages.success(request,'Recored deleted successfully')
    return redirect('home')
  else:
    messages.success(request,'You need to login to delete Product')
    return redirect('home')
  



def update_product_record(request, pk):
    if request.user.is_authenticated:
        current_Product = Product.objects.get(id=pk)
        if request.method == "POST":
            form = AddProductForm(request.POST, request.FILES, instance=current_Product)
            if form.is_valid():
                form.save()
                messages.success(request, "Product Detail has been updated")
                return redirect('home') 
        else:
            form = AddProductForm(instance=current_Product)
        return render(request, 'updateproduct.html', {"form": form})
    else:
        messages.success(request, "You need to be logged in to update a product")
        return redirect('home')
