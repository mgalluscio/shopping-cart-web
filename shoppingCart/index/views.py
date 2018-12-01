from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Products, Customers, Orders, Order_Items
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
class HomePageView(TemplateView):
    products = Products.objects.all()

    context = {
        'products': products
    }
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=self.context)

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
        return render(request, self.template_name, {'form': form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = 'login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.error(request, 'Your account has been disabled')
                    return render(request, self.template_name)
            else:
                messages.error(request, 'Invalid login!')
                return render(request, self.template_name)
        return render(request, self.template_name)

class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

class CartView(View):
    template_name = 'cart.html'
    
    def get(self, request):
        cart_items = Order_Items.objects.filter(order_id__customer_id = request.user)
        #cart_total = sum([cart_items.product_id.product_price for product in cart_items])
        context = {
            'cart_items': cart_items
        }
        return render(request, self.template_name, context=context)


@login_required
def AddToCart(request, **kwargs):
    customer = get_object_or_404(User, username=request.user)
    #print(customer.id)
    product = Products.objects.filter(id=kwargs.get('item_id', "")).first()
    #print(product)
    user_order, status = Orders.objects.get_or_create(customer_id=customer, is_ordered=False)
    order_item = Order_Items.objects.create(product_id=product, order_id=user_order)
    if status:
        #print(user_order)
        user_order.save()
        order_item.save()
    messages.success(request, 'Item added to cart!')
    return redirect('index')

@login_required
def RemoveCartItem(request, **kwargs):
    product = Order_Items.objects.filter(id=kwargs.get('item_id', ""))
    if product.exists():
        product.delete()
        messages.info(request, 'Your item has been removed from the cart.')
    return redirect('cart')
