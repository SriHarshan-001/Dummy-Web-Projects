from django.db import models

# Create your models here.
class adminis(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)

    def __str__(self):
        return f" Username:{self.username} Password:{self.password}"
        
class Empid(models.Model):
     empid=models.CharField(max_length=100,primary_key=True)

     def __str__(self):
         return f"Employee_Id:{self.empid}"


class Employee(models.Model):
    empid=models.ForeignKey(Empid,on_delete=models.CASCADE,db_constraint=False)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)

    def __str__(self):
        return f"Employee_Id:{self.empid}  Username:{self.username} Password:{self.password}" 
    
class geoloc(models.Model):
    empid=models.ForeignKey(Empid,on_delete=models.CASCADE,db_constraint=False)
    geotag=models.CharField(max_length=10)

    def __str__(self):
        return f"Employee_Id:{self.empid} Geolocation:{self.geotag}"

