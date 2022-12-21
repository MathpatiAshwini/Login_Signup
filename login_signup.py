
import json 

user=input("enter the user choise login or signup:--")

if user=="1":
    name=input("enter user name:--")
    password=input("enter your strong password:--")
    a,b,c,d=0,0,0,0
    z=len(password)
    spe="@#!$*&%"
    for i in password:
        if i.upper():
            a+=1
        if i.lower():
            b+=1
        if i in spe:
            c+=1
        if i.isdigit():
            d+=1 
    if z>=8:
        if a>=1 and b>=1 and c>=1 and d>=1:
            print("simple password")
            password2=input("enter your password for conforming:--")
            if password==password2:
                print("your both passwords are  same:")
                dic1={}
                dic2={}
                l=[]
                d={}
                dic1["name"]=name
                dic1["password"]=password
                dic2["description"]=input("enter about you")
                dic2["DOB"]=input("enter youe d/o/b")
                dic2["gender"]=input("enter your gender")
                dic2["habbits"]=input("what you like")
                dic1["profile"]=dic1
                l.append(dic1)
                d["user"]=l
                f=open("login.json","w+")
                json.dump(f,indent=4)
                f.close()
                print("your sign up is successful")
            else:
                print("both passward not same")
        print("inviladed")
    print("8 charter")
elif user=="2":
    file=open("login.json","r")
    app=json.load(file)
    name=input("enter your name:--")
    password=input("enter your password:--")
    for i in app["user"]:
        if name==i["name"]:
            if password==i["password"]:
                print("succesfull")
                print(i)
            else:
                print("cheak your password")
        else:
            print("cheack your name:--")
        
        
