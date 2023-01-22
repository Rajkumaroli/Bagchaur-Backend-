from django.db import models

# Create your models here.
class Contact(models.Model):
    name =  models.CharField(max_length=50)
    email = models.EmailField(max_length=24)
    comment = models.TextField()

    def __str__(self):
        return self.name
    
class Janpratinidhi(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    worda = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
    
class Staff(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

class Ward1(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Ward2(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ward3(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ward4(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ward5(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ward6(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ward7(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ward8(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ward9(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ward10(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ward11(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ward12(models.Model):
    photo = models.ImageField(upload_to='images', default="")
    name = models.CharField(max_length=30)
    post  = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class MunicipalD(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    title = models.TextField()
    document = models.TextField()

    def __str__(self):
        return self.name
    

class Gazette(models.Model):
    name = models.CharField(max_length=200)
    document = models.CharField(max_length=1000)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
    
class News(models.Model):
    news = models.TextField()

    def __str__(self):
        return self.news
    
class Publications(models.Model):
    name = models.CharField(max_length=600)
    document = models.CharField(max_length=700)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

class AnnualPR(models.Model):
    name = models.CharField(max_length=600)
    document = models.CharField(max_length=700)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    

