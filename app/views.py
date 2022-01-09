
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import  Product
from .forms import ProductRegisterForm
from django.contrib.auth.decorators import login_required,permission_required
from .sales import Sale




@login_required
def home(request):
    
    user = request.user
    if user.has_perm('app.is_admin'):
        return redirect(reverse('adminhome'))
    elif user.has_perm('app.is_seller'):
        return redirect(reverse('sellerhome'))
    
    
    

@permission_required('app.is_admin')
def adminhome(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminhome')
    
    else:
        form = ProductRegisterForm()

    context = {'products':products,
                 'form':form}
    
    return render(request, 'app/adminhome.html', context)



@permission_required('app.is_admin')
def deleteproduct(request, skuproduct):
    product = Product.objects.get(sku=skuproduct)
    product.delete()
    return redirect('adminhome')



@permission_required('app.is_admin')
def editproduct(request, skuproduct):
    product = Product.objects.get(sku=skuproduct)
    if request.method == 'POST':
        form = ProductRegisterForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('adminhome')

    else:
        form = ProductRegisterForm(instance=product)

    context = {
        'form':form
    }

    return render(request, 'app/editproduct.html', context)



@permission_required('app.is_seller')
def sellerhome(request):

    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request, "app/seller.html", context)



@permission_required('app.is_seller')
def seller_addsale(request, sku):
    
    sale = Sale(request)
    product = Product.objects.get(sku=sku)
    if product.quantity > 0:
    
        sale.addproduct(product=product)

        product.quantity -= 1
        product.save()
       
        
    return redirect("sellerhome")





@permission_required('app.is_seller')
def seller_quitproduct(request, sku):
    sale = Sale(request)
    product = Product.objects.get(sku=sku)
    sale.quit_product(product=product)
    product.quantity += 1
    product.save()
        
    return redirect("sellerhome")    



@permission_required('app.is_seller')
def make_sale(request):
    sale = Sale(request)

    return render(request,'app/salesuccesfull.html')



@permission_required('app.is_seller')
def clean_sale(request):
    sale=Sale(request)
    sale.clean()

    return redirect("sellerhome")