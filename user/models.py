from django.db import models

class Tender(models.Model):
    tenderid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    subcatname=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    sdate=models.DateField()
    edate=models.DateField()
    tenderfilename=models.CharField(max_length=100)
    uid=models.CharField(max_length=50)
    info=models.CharField(max_length=50)    

class Funds(models.Model):
    txnid=models.AutoField(primary_key=True)
    uid=models.CharField(max_length=50)
    amt=models.IntegerField()
    info=models.CharField(max_length=50)    


    