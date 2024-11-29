# CATII_question2

# 1. Create & Activate Virtual Environment
Create a virtual environment using 
the following command 'python -m 
venv venv'

Activate the environment using the
 following code, '.
 \venv\Scripts\activate'

# 2. Install the Django Rest_Framework
Using the code, 'pip install django djangorestframework'

# 3. Start a New Django Project
Create a project in the Virtual environment, use the code, 
'django-admin startproject product_api' to create the 
project, and navigate to it using, 'cd product_api'

# 4. Create a new Django App
Create the Django APP in this case called products using 
the code, 'python manage.py startapp products'

# 5. Configure settings in the REST_API folder
In settings.py, adjust the following, 

INSTALLED_APPS = [
    'rest_framework',
    'products',
]

# 6. Define the Product model in the Products folder
In models.py, add the following, 

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name

# 7. Run and save the migrations
This is to save the changes made above and also apply 
migrations to the Django APP. 
Use these codes, 
python manage.py makemigrations // To save changes
python manage.py migrate // To add the migrations

# 8. Create a Serializer in the Products Folder
Serializers are for converting data from python objects to
JSON requests. 
Use the code,

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

# 9. Create API Views in the Products Folder

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({'message': 'Product deleted'}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

# 10. Set Up URLS in both the Products and REST_API Folders
For the products folder, these are applied in the urls.py 
files respectively

from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]

for the REST_API folder

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
]

# 11. Run the server
Use python manage.py runserver
Once in the server, http://127.0.0.1:8000/api/products
to view and add the products

## TESTING THE API ENDPOINTS ##

# Creating a Product
On the server link, type, 
{
  "name": "Laptop",
  "description": "A high-end gaming laptop",
  "price": 1500.99
}
this is to create a product, once done press on POST to 
post

# Get Product by ID
On the server link, edit the http to, 
http://127.0.0.1:8000/api/products/1/
This will portray the first product

# Retrieve and print the list of all products
On the server link, the GET button will retrieve and print 
the list of all products created alongside their ID's

# Bad request 400
On the server link, when creating a product, try, 
{
  "name": "Laptop",
  "description": "A high-end gaming laptop",
  "price": error INSTEAD OF INT e.g 15099.2
}
This will display an error code 400, with a message, 
"whoops, something went wrong"

# Successful Request
On the server link, when creating a product, try
{
  "name": "Laptop",
  "description": "A high-end gaming laptop",
  "price": 1500.99
}
This will display a success code 201, with a message, "Product Added Successfully!"


















