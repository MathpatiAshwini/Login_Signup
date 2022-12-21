import json
def my():
    user=input("Enter 1 Login or 2 Signup: ")
    if  user=='2':
        userName=input("Enter your Name,,:")
        password=input("Enter your Password,,:")
        l,b,c,d=0,0,0,0
        special_chr="@!#$%^&*()"
        p=len(password)
        for i in password:
            if i.isupper():
                l=l+1
            if i.islower():
                b=b+1
            if i.isdigit():
                c=c+1
            if i in special_chr:
                d=d+1
        if p>=6:
            if l>=1 and b>=1 and c>=1 and d>=1 :
                print("Right Password")
                password2=input("Entewr your password again,,:")
                if password==password2:
                    print("comfire password")
                    dic={}
                    l=[]
                    d={}
                    d1={}
                    dic["username"]=userName
                    dic["password"]=password
                    d["description"]=input("Enter your Description,,:")
                    d["D.O.B"]=input("Enter your D.O.B,,:")
                    d["Gender"]=input("Enter your Gender,,:")
                    d["Habbies"]=input("Enter your Hobbies,,:")
                    dic["profile"]=d
                    l.append(dic)
                    d1["user"]=l
                    file=open("signup.json","w+")
                    json.dump(d1,file ,indent=4)
                    file.close() 
                    print("siginup succesfully")
                else:
                    print("both the password are not same")
            else:
                print("invilid")
        else:
           print("password should contain atleast 6 chr")

    elif user=='1':
        a=open("signup.json","r")
        f=json.load(a)
        name=input("Enter your login name,,:")
        l_password=input("Enter your login password,,:")
        for i in f["user"]:      
            if name==i['username']:
                if l_password==i['password']:
                    print("Login Successful")
                    print(i)
                else:
                    print("Check your password,,:")
            else:
                print("Check your  username,,:")
    else:
        print("You can,t Login/Signup")
my()