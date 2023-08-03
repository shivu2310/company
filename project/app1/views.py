from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Company , Student ,Recruitment, Contact

# Create your views here.
def home(request):
    company_count = Company.objects.all().count()
    student_count = Student.objects.all().count()
    Total_count = User.objects.all().count()
    counter = {'company': company_count , 'student': student_count , 'total': Total_count}
    return render (request, 'app1/home.html' , counter)

def about(request):
    return render (request, 'app1/about.html')

def service(request):
    return render (request, 'app1/service.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        add1 = request.POST.get('add1')
        add2= request.POST.get('add2')
        query = request.POST.get('query')
        errory = None
        if (not email):
            errory = "Please Enter Email Field"
            
        elif (not contact):
            errory = "Please Enter Contact Field"
        elif (not add1):
            errory = "Please Enter Address Field"
        
        elif (not query):
            errory = "Please Enter Query Field"
    
        if not errory:
            contact = Contact(email=email, contact=contact , add1=add1,query=query)
            contact.save()
            messages.info(request,"Send Your Details We will contact you shortly")
        else:
            error = {'error': errory}
            return render (request, 'app1/contact.html',error)
    return render (request, 'app1/contact.html')

def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('companyname')
        # print(username)
        password1 = request.POST.get('pass1')
        # print(password1)
        
# --------------------------------------------------------------------------------------
# Validation

        error_count = None

        if (not username):
            error_count = "Please Enter Company Name or Student's Username Field"
            
        elif (not password1):
            error_count = "Please Enter Password Field"
#--------------------------------------------------------------------------------------
 #After keep empty field do login those field which filled already come with filled field
           
        come_value = { 'username' : username , 'passwrd':password1 }


#--------------------------------------------------------------------------------------
        if (not error_count):
            user = authenticate(request,username=username,password=password1)
        
        
            if user is not None:
                login(request, user)
                userman=user.username
                cosuser = {'cosuser': userman}
                model = Recruitment.objects.all()
                data = {'data' : model}
                logger = {'cosuser': cosuser , 'data':data}
                return render(request, "app1/profile.html" ,logger)
            
    
            else:
                messages.info(request, "We have not found your Account in our Database.")
                # return HttpResponse ("You did not Signin")
                return redirect('home')
        else:
            pass_data1 = { 
                     'error':error_count , 'value_field' :come_value 
                }
            return render (request, 'app1/login.html' , pass_data1)

                        
    return render (request, 'app1/login.html')




@ login_required(login_url='login')
def profile(request):
    model = Recruitment.objects.all()
    data = {'data' : model}
    logger = {'data':data}
            
    return render (request, 'app1/profile.html' , logger)


@ login_required(login_url='login')
def postPage(request):
    
    current_user = request.user
    
    if request.method == 'POST':
        # context = {'user_name' : user_name}
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        
        vacancy = request.POST.get('vacancy')
        skill = request.POST.get('skill')
        salary = request.POST.get('salary')
        destination = request.POST.get('destination')
        fresher = request.POST.get('fresher')
        fulltime = request.POST.get('fulltime')
        jobdes = request.POST.get('job_description')
# -------------------------------------------------------------------------------------

        # validation
        error_messages = None
        if (not vacancy):
            error_messages = " Vacant Seat Field is required"

        elif (not name):
            error_messages = "Company Name Field is required"   

        elif (not contact):
            error_messages = "Contact Field is required"   

        elif (not skill):
            error_messages = "Skill Demand Field is required"   
        elif (not salary):
            error_messages = "Salary Field is required"
        elif (not destination):
            error_messages = "Destination Field is required"
        elif (not fresher):
            error_messages = "Status Field is required"
        elif (not fulltime):
            error_messages = "State Field is required"
        elif (not jobdes):
            error_messages = "Job Description Field is required"
# ------------------------------------------------------------------------------------        
# value remain

        value_comer = { 'name': name , 'vacant' : vacancy ,'skill' : skill , 'salary': salary , 'destination' : destination  , 'fresher' : fresher , 'fulltime' : fulltime , 'jobdes': jobdes , 'contact' : contact}
# -------------------------------------------------------------------------------
        if not error_messages:
            recruiting = Recruitment(name=name,work=fulltime, recruit=fresher, vacancy=vacancy , job_description=jobdes ,demanded_skill=skill, status=destination , salary_scale=salary , contact = contact)
            recruiting.save()
            

            messages.info(request,"Your Job Post has been Posted")  
            
            model = Recruitment.objects.all()
            data = {'data' : model}
            logger = {'data':data}
            
            
            return render (request, 'app1/profile.html' , logger)
        else:
            error_value = { 'error': error_messages , 'value' : value_comer}
            return render (request, 'app1/companypost.html' , error_value)
    return render (request, 'app1/companypost.html',{'username': current_user})

def logoutPage(request):
    logout(request)
    return redirect ('/login')

def signcos(request):
    if request.method=='POST':
        pass1 = request.POST.get('pass1')
        companyName = request.POST.get('companyname')
        pass2 = request.POST.get('pass2')
        if pass1!=pass2:
            messages.info(request,'Password and Confirm Password is not Matching')
        else:
            email = request.POST.get('email')
            owner = request.POST.get('owner')
            street = request.POST.get('street')
            country = request.POST.get('country')
            state_ut = request.POST.get('state-ut')
            zip = request.POST.get('zip')
            website = request.POST.get('website')
                                
            nominalcap = request.POST.get('nominalcap')
                        
                                    
            industry = request.POST.get('industry')

            mobile = request.POST.get('mobile')
            altermobile = request.POST.get('altermobile')
            cosdes = request.POST.get('cosdes')
            
            
#--------------------------------------------------------------------------------------- -
            #After keep empty field do sign in those field which filled already come with filled field
           
            value_come = { 'nCompany' : companyName , 'email':email , 'owname':owner,'street': street , 'country' :country, 'state_ut':state_ut , 'zip':zip , 'website': website, 'nominalcap': nominalcap , 'industry':industry , 'mobile': mobile , 'altermobile': altermobile , 'cosdes1': cosdes
                    
                    }
            







#------------------------------------------------------------------------------------------
            # validations of field


            error_msg = None
            if (not companyName):
                error_msg = "Company Name is required"
            elif (not pass1):
                error_msg = "Password is required"
            elif len(pass1) < 8:
                error_msg = "Password must be 8 Character or Number long"
            elif (not pass2):
                error_msg = "Confirm Password is required"
            
            elif (not email):
                error_msg = "Email is required"
            elif (not owner):
                error_msg = "Owner Name is required"
            elif (not state_ut):
                error_msg = "State-Union Territories Field is required"
            elif (not website):
                error_msg = "Website Field is required"
            elif (not nominalcap):
                error_msg = "Nominal Capital Field is required"
            elif (not industry):
                error_msg = "Industry Field is required"
            elif (not mobile):
                error_msg = "Mobile Number Field is required"
            elif len( mobile)<10:
                error_msg = " Mobile Number must be 10 Digit "
            elif (not cosdes):
                error_msg = "Company Description Field is required"
            elif len(mobile)>10:
                error_msg = " Mobile Number field Exceed 10 Digit "
                
# ---------------------------------------------------------------------------------------- 
            if not error_msg:
                  
                # Created Object
                company = Company(Company_name=companyName, email=email,description=cosdes,website=website,Contact_Number=mobile)
                company.save()
                # x=Recruitment(name=companyName)
                # postPage(x)
                # x.save()
                          
                my_user = User.objects.create_user(companyName,email,pass1)
                my_user.first_name = nominalcap
                my_user.last_name = industry
                my_user.save()
                messages.success(request, 'Company has been Registered ')
                return redirect ('/login')
            else:
                pass_data = { 
                     'error':error_msg , 'value_field' :value_come 
                }
                return render (request, 'app1/signcos.html',pass_data)            

    return render (request, 'app1/signcos.html')



def stusign(request):
    if request.method == 'POST':
        pass1 = request.POST.get('pass1') 
        pass2 = request.POST.get('pass2') 
        if pass1!=pass2:
            messages.info(request, "Password and Confirm Password is not Matching")
        else:
            username = request.POST.get('username')
            fullname = request.POST.get('fullname') 
            email = request.POST.get('email')
            street = request.POST.get('street')
            country = request.POST.get('country')
            state_ut = request.POST.get('state-ut')
            zip = request.POST.get('zip')
            portfolio = request.POST.get('portfolio')
            collegename = request.POST.get('collegename')
            industry = request.POST.get('industry')
            cgp = request.POST.get('cgp')
            qualification = request.POST.get('qualification')
            resume = request.POST.get('resume')
            mobile = request.POST.get('mobile')
            altermobile = request.POST.get('altermobile')
            birthday = request.POST.get('birthday')
            skills = request.POST.get('skills')
            coverpage = request.POST.get('coverpage')
            
#------------------------------------------------------------------------------------

            value_come = {'username': username , 'fullname' : fullname ,  'email':email,    'street' : street ,'country':country ,'state_ut':state_ut ,'zip': zip ,'portfolio': portfolio ,'collegename':collegename  ,'industry':industry ,'cgp': cgp, 'qualification':qualification, 'resume':resume, 'mobile':mobile , 'altermobile' : altermobile, 'birthday' : birthday , 'skills' : skills , 'coverpage': coverpage
                
            }



# ----------------------------------------------------------------------------------

# validation
            error_message = None
            if (not pass1):
                error_message = "Password Field is required"
            elif (not pass2):
                error_message = "Confirm Password Field is required"
            
            elif (not username):
                error_message = "Username Field is required"
            
            elif (not fullname):
                error_message = "Full Name Field is required"
            
            elif (not email):
                error_message = "Email Field is required"

            elif (not street):
                error_message = "Street Field is required"

            elif (not country):
                error_message = "Country Field is not Selected"

            elif (not state_ut):
                error_message = "State Union Territory Field is not Selected"
    
            elif ( not zip):
                error_message = "Zip Field is required"

            elif (not collegename):
                error_message = "College Field is required"

            elif ( not industry):
                error_message = "Industry Field is not Selected"

            elif (not cgp):
                error_message = "CGP Field is required"

            elif (not qualification):
                error_message = "Qualification Field is not Selected"

            elif (not resume):
                error_message = "Resume is not uploaded"

            elif ( not mobile):
                error_message = "Mobile Number Field is required"

            elif (not altermobile):
                error_message = "Alternative Mobile Number Field is required"
                
            elif len( mobile)<10:
                error_message = " Mobile Number must be 10 Digit "
          
            elif len(mobile)>10:
                error_message = " Mobile Number field Exceed 10 Digit "    

            elif (not birthday):
                error_message = "Please Choose Birth Date Field"

            elif (not skills):
                error_message = "Key Skills Field is required"

            elif (not coverpage):
                error_message = "Cover Page Field is required"
                
#-------------------------------------------------------------------------------------- 
            if (not error_message):
                student = Student(Full_Name=fullname,  Key_Skills=skills, Contact_Number=mobile, Alternative_Number=altermobile, portfolio=portfolio, college_name=collegename, birth_date=birthday , cgp =cgp,email=email ,  file = resume , description=coverpage, choice=qualification)
                student.save()
                
                my_user = User.objects.create_user(username,email,pass1)
                my_user.first_name = fullname
                my_user.last_name = coverpage
                my_user.save()
                messages.success(request,"Student has been Registered in our Database")  
                return redirect ('/login')
            else:
                pass_info = {
                    'error': error_message , 'valuer':value_come
                }
                return render (request, 'app1/stusign.html', pass_info)

    return render (request, 'app1/stusign.html')



