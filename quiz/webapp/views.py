from django.shortcuts import render , redirect , HttpResponse
from .models import *
from django.core.mail import send_mail
from django.conf import  settings
import random


pro = []
ids = []

def data_questions():
    global pro , ids
    pro.clear()
    ids.clear()
    while len(pro) < 25:
        x = random.randint(1,100)
        if x not in ids:
            ids.append(x)
            pro.append(Test_questions.objects.get(id = x ))


def login(req):
    
    if req.method == "GET":
        return render(req, "login.html")
    if req.method == "POST":
        mail = req.POST.get("email")
        password = req.POST.get("password")
        data = Student.objects.all()
        for i in data:
            if  mail == i.email or mail == i.contact :
                if password == i.password:
                    if i.auth != "allow":
                        return render (req , "login.html" , {"error" : "your account is not activated!" })
                    response = redirect("home")
                    response.set_cookie('user', i.name)  
                    response.set_cookie('id', i.id)
                    response.set_cookie('exam', i.test_no) 

                    
                    return response
                
                else:
                    return render (req , "login.html" , {"error" : "this is a wrong password!" })
        return render (req , "login.html" , {"error" : "this email is not regesterd!" })
    return render(req ,"login.html")

def signup(req):
    if req.method == "POST" :
        name = req.POST.get('name')
        user = req.POST.get("user")
        mail = req.POST.get("mail")
        pswd = req.POST.get("pswd1")
        pswd2 = req.POST.get("pswd2")
        code = req.POST.get("pswd3")
        hallticket = req.POST.get("token")

        data = Student.objects.all()
        for i in data:
            if  mail == i.email or user == i.contact :
                if pswd == pswd2:   
                    return render (req , "signup.html" , {"error" :  "this mail already have account, please login !"} )
                else:
                    return render (req , "signup.html" , {"error" :  "re-enterd password didn't sink with password !"} )

        user = Student(name = name , contact= user , email = mail , password = pswd , test_no = 0 , test_avg = 0 , total = 0 , college = code , studentId = hallticket )
        user.save()

        return render (req , "signup.html" , {"error" :  "student regestered sucessfully you can login after your account activation!"} )

    return render(req ,"signup.html")

def forgot(req):
    if req.method == "POST":
        mail = req.POST.get("email")
        data = Student.objects.all()
        for i in data:
            if  mail == i.email :
                url = "settings/login-unable/forgot-passkey/reset-password/"+ str(i.id)
                send_mail( subject="PASSWORD RESET", message=url, from_email=settings.EMAIL_HOST_USER,recipient_list=[mail])            
                return render (req , "forgotPass.html" , {"error" : "mail sended to your mail!" })

        return render (req , "forgotPass.html" , {"error" : "this email is not regesterd!" })
        
    return render(req ,"forgotPass.html")

def reset(req , key):
    data = Student.objects.get(id= key)
    if req.method == "POST" :
        pswd = req.POST.get("pswd1")
        pswd2 = req.POST.get("pswd2")
        if pswd == pswd2: 
            data.password = pswd
            data.save()
            return render(req,"passlogin.html")
        return render(req , "reset.html" ,  {"error" : "password and re-enterd password is not matched!" } )

    return render(req , "reset.html" )

def home(req):
    user_name = req.COOKIES['user']
    val_id = req.COOKIES['id']
    try:
        if user_name and val_id:
            data = Student.objects.get(id = val_id)
            return render(req , "index.html" , {"user_name" :user_name , "user": data})
        else:
            return redirect ("login")

    except:
        return redirect ("login")
    
def profile(req):
    user_name = req.COOKIES['user']
    val_id = req.COOKIES['id']
    try:
        if user_name and val_id:
            data = Student.objects.get(id = val_id)
            return render(req , "profile.html" ,  {"user_name" :user_name , "user": data})
        else:
            return redirect ("login")

    except:
        return redirect ("login")
    
def update(req):
    user_name = req.COOKIES['user']
    val_id = req.COOKIES['id']
    try:
        if user_name and val_id:
            data = Student.objects.get(id = val_id)
            if req.method == "POST" :
                call = req.POST.get('name')
                user = req.POST.get("user")
                mail = req.POST.get("mail")
                data.name = call
                data.contact = user
                data.email = mail
                data.save()
                user_name = call
                return render(req, "updateprofile.html", {"user_name" :user_name , "user": data})
            return render(req, "updateprofile.html", {"user_name" :user_name , "user": data})
        else:
            return redirect ("login")

        
    except:
        return redirect ("login")

def result(req , exam , id  , val):
    test = Test.objects.get(user_id = id)
    for i in test:
        if i.test_no == exam:
            return render(req , "testresult.html" , {"msg" : " Congratulations !you had compleated this test watch your score !"  , "val" : val , "data" : i})

def test(req , val):
    global  pro , ids
    user_name = req.COOKIES['user']
    val_id = req.COOKIES['id']
    user = Student.objects.get(id = val_id )
    try:
        if user_name and val_id:        
            if user.test_no < val:
                if user.test_no < val and user.test_no == (val-1):
                    data_questions()
                    
                    return render(req, "setup.html" , {"val":val })
                return render(req, "testdone.html" , {"msg" : "you haven't access for this test" , "val" : val })

            test = Test.objects.all()
            for i in test:
                print(i.test_no , val)
                if  int(i.test_no) == int(val) and i.user_id == user.studentId :
                    print(i.user_id ,user.studentId ,  i.test_no , val, "test" )   
                        
                    return render(req , "testresult.html" , { "val": val ,"msg" : " Congratulations ! you had compleated this test watch your score is " + i.marks ,"user":user  })
                
            
                # return render(req , "testresult.html" , { "val": val ,"msg" : " Congratulations ! you had compleated this test watch your score is " + i.marks ,"user":user  })
        else:
            return redirect ("login")


    except:
        return redirect ("login")
    
def logout(req):
    return redirect("login")

def updatedpasskey(req):
    return render(req, "passlogin.html")

def setup(req  ):
    global pro
                
    
    val_id = req.COOKIES['id']
    val  = int(req.COOKIES['exam'])
    user = Student.objects.get(id = val_id )
            
    if req.method == "POST" :
        ans = list(req.POST)
        del ans[0]
        n = len(ans)
        marks = 0
        print("after submit")
        for i in range(0,n):
            form = req.POST.get(ans[i])
            
            print( pro[i].ans ,form)
            if form == pro[i].ans :
                marks +=1
                user.total += 1
                user.save()
        user.test_no += 1
        user.test_avg  =(float( int(user.total) / int(user.test_no)  )) 

        user.save()
        new_test = Test(user_id = user.studentId ,name = user.name ,  marks = marks , test_no =user.test_no  ) 
        new_test.save()
        val+=1
        req.COOKIES['exam'] = val
        return render(req, "testdone.html" , {"msg" : "CONGRATES YOU HAVE COMPLEATED THIS TEST!" })
    
    for i in pro:
        print(i.ans) 
    
    return render(req, "test.html" ,  {"pro":pro })

