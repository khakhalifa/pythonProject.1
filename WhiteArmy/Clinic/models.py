from django.db import models
import datetime

class Date_of_examination (models.Model):
    examination_date = models.DateTimeField()
    consultation_date = models.DateTimeField()
    followup_date = models.DateField()

class Id (models.Model):
    patient_name = models.CharField(max_length=64)
    gender= models.Choices ('male','female')
    national_id_number = models.IntegerField()
    phone_number = models.IntegerField()
    marital_status = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    other =models.TextField(default="")
    time = models.ForeignKey('Date_of_examination',on_delete=models.SET_NULL, null=True, related_name='time')

    def age(self):
        import datetime
        return int((datetime.datetime.now() - self.birthday).days / 365.25)

    age = property(age)

    def __str__(self):
        return f"{self.patient_name} {self.gender} {self.marital_status} {self.national_id_number} {self.phone_number} {self.address} {self.email} {self.age} {self.other}"


class Present_complaint (models.Model):
    site = models.CharField(max_length=200)
    onset = models.CharField(max_length=200)
    character= models.CharField(max_length=200)
    radiation= models.CharField(max_length=200)
    associations= models.CharField(max_length=300)
    time_course = models.CharField(max_length=200)
    exacerbation = models.CharField(max_length=200)
    relieving_factors= models.CharField(max_length=200)
    severity= models.CharField(max_length=200)
    post_medical_history= models.TextField()
    other_medical_problems= models.TextField()
    drug_history= models.TextField()
    family_history = models.TextField()
    special_habits = models.CharField(max_length=300)
    notes=models.TextField(default="")
    name= models.ForeignKey('Id',on_delete=models.SET_NULL, null=True, related_name='name')



class Past_history(models.Model):

    cardiovascular_system =models.CharField(max_length=200)
    respiratory = models.CharField(max_length=200)
    gastrointestinal_tract= models.CharField(max_length=200)
    neurology = models.CharField(max_length=200)
    genitourinary= models.CharField(max_length=200)
    renal= models.CharField(max_length=200)
    musculoskeletal=models.CharField(max_length=200)
    psychiatry= models.CharField (max_length=200)
    complaint = models.ForeignKey('Present_complaint',on_delete=models.SET_NULL, null=True, related_name='complaint')


class Advise (models.Model):
    investigation= models.CharField(max_length=400)
    lab= models.CharField(max_length=100)
    visual= models.CharField(max_length=100)
    step_medication= models.CharField(max_length=400)
    note= models.TextField()
    history = models.ForeignKey('Past_history', on_delete=models.SET_NULL, null=True, related_name='hitory')



class Management (models.Model):
    treatment= models.CharField(max_length=200)
    patient = models.ForeignKey('Id', on_delete=models.SET_NULL, null=True, related_name='patient')



