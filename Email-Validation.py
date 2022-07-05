email = input("Enter Your E-mail :") # ex : sahilkumarj82@gmail.com
k,j,d = 0,0,0;
#now we will use if fuction for length of email
if len(email)>=6: # email should be 6 digit 
    if email[0].isalpha(): # if the first index of email (ex : sahil..@gmail.com) is alphabet then follow down code
        # Now if the first len -> is 6 then second if -> first leter of email is alphabet then now check for @ in email -> no of @ should be 1
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."): # coz checking from last of email if in ( ex : sahil@gmail.in) --> index no of "." is 3 and (sahil@gmail.com) --> index no of "." is 4 
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper(): # ex : W --> W==W
                            j=1;
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i == "@":
                        continue
                    else:
                        d = 1
                if k==1 or j==1 or d==1:
                    print("Wrong Email --> spacing or Upper case")
                else:
                    print("Right Email")
            else:
                print("Wrong Email --> Check your email")
        else:
            print("Wrong Email --> Check @ in your E-MAIL ") 
    else:
        print("Worng Email --> Check your first letter of email -> should be alphabet") # if not then print wrong code (ex: 1sahil..@gmail.com) --> which is invalid 

else:
    print(" Worng Email --> email should be of 6 letter") # if email is less than 6 characters