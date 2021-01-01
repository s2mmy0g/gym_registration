from django.db import models
from customer.models import Customer
# Create your models here.
class Register(models.Model):
    register_id = models.AutoField(auto_created=True, primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    time=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    class Meta:
        db_table = "register"
