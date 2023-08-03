from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

company_work = (
    ('product', 'Product Based Company'),
    ('service' , 'Service Based Company')
)

work_status = (
    ('home' , 'work from home'),
    ('office' , 'work from office')
)

# student = (
#     ('graduate' , 'Graduate'),
#     ('undergraduate' , 'Under Graduate(College Student)'),
# )



class Company(models.Model):
    
    Company_name = models.CharField(max_length=50 , verbose_name="Registered Company Name"  , help_text="Enter Company Name which is written into Registration Form" , blank=True)
    
    
        
    email = models.EmailField(max_length=50 , help_text="Enter Company Email", blank=True)
    
    
    description = models.TextField(verbose_name="Company Description" , help_text="Enter about Company's Goals , Aim and Contribution or Ideas", blank=True)
    
    website = models.URLField(max_length=60 ,null=True, blank=True,  verbose_name="Company website" , help_text="Enter Company's official Website")
    
    
  
    
    



    Contact_Number = PhoneNumberField(blank=True)
    
class Student(models.Model):
    Full_Name = models.CharField(max_length=60,blank=True)
    
    Key_Skills = models.CharField(max_length=60 , help_text="Enter Your Skills " ,blank=True)
    
    Contact_Number = PhoneNumberField(blank=True)
    
    Alternative_Number = PhoneNumberField(blank=True)
    
    
    portfolio = models.URLField(max_length=60 ,null=True, blank=True, verbose_name="Portfolio" , help_text="Enter Candidate's Portfolio URL")
    
    college_name = models.CharField(max_length=100 , verbose_name="College Name"  , help_text="Enter College Name " ,blank=True)
    
  
    
    birth_date = models.DateField(verbose_name="Date Of Birth" , default=timezone.now , help_text="Enter Date of Birth",blank=True)
    
    cgp = models.DecimalField(max_digits=5 , decimal_places=2 ,help_text="Enter CGP or Percentage of Last Year", verbose_name="CGP Or Percentage",blank=True)
    
    email = models.EmailField(max_length=50 , help_text="Enter Candidate's Email",blank=True)
    
    file = models.FileField(upload_to='app1/static/candidate', blank=True ,help_text="Upload Your Resume with demanded skills by company", verbose_name="Upload Resume")
    
    description = models.TextField(verbose_name="Cover Page" , help_text="Why should you hire ",blank=True)
    
    choice = models.CharField(max_length=20  , help_text="Are You Graduate or Under Graduate",blank=True)

class Recruitment(models.Model):

    name = models.CharField(blank=True,max_length=50)

    work = models.CharField(max_length=20 ,  help_text="choose working mode" ,verbose_name="working status",blank=True)
    
    Last_update = models.DateTimeField(auto_now=True , help_text="Last update in This Form", blank=True)

    recruit = models.CharField(max_length=20 ,  help_text="Which Kind of Candidate requirement (Fresher , Experience )" ,blank=True)

    vacancy = models.IntegerField(default=0)


    
    demanded_skill = models.CharField(max_length=50,help_text="Enter Demanded Skill"  , blank=True)
    
    status = models.CharField(max_length=50,help_text="Want Full Time or Part Time" , verbose_name="Required", blank=True)
    
    contact = PhoneNumberField(blank=True)
    
    salary_scale = models.CharField( blank=True,max_length=40)
    
    job_description = models.TextField(verbose_name="job description" , help_text="what kind of candidate you are Wanting",blank=True)

    
class Contact(models.Model):
    email = models.EmailField(max_length=50 , help_text="Enter Candidate's Email",blank=True)
    
    contact = PhoneNumberField(blank=True)
    
    add1 = models.CharField(max_length=60,blank=True)
     
  
    
    query = models.TextField(blank=True)
    
  
