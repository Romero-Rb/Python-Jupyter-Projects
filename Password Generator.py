#Romero's Structure for a random password generator

import string
import random

def password_generator():
    
    #Custom length value should user request it
    
  
    
    #Creating truth values for required parts of the password
    
    lower = False
    cap = False
    numb = False
    symb = False
    
    #Creating a list for each range of values for the class of characters
    #using the string package
    
    ps1 = list(string.digits)
    ps2 = list(string.punctuation)
    ps3 = list(string.ascii_lowercase)
    ps4 = list(string.ascii_uppercase)
    
    #combined list 
    ps5 = ps1 + ps2 + ps3 +ps4
    #Seeting a value for a preffered length
    #If preflen stays as -1 it will use the minimum requirement
    
    minlen = 0
    preflen = -1
    #Getting input on the length and required parts
    #Using a while loop that continues until exit
    while True:
        try:
            minlen = int(input("Minimum password length (greater than 6): "))
        
            if minlen <= 6:
                print ("Please try again")
            else:
                    break
        except:
           print("This isn't a number")
    while True:
        try:
            cusstr = str(input("Would you like a custom length? (Yes/No): "))
            cusstr = cusstr.strip()
            cusstr = cusstr.lower()
    
            if cusstr == "yes":
                preflen = int(input("Enter the length: "))
                break
            elif cusstr == "no":
                preflen = -1
                break
            
            else:
                print ("Please enter yes or no")
        except:
            print("This isn't a number")
        
    while True:
        
        numreq   = str(input("Does your password require a number/digit?: "))
        numreq = numreq.strip()
        numreq = numreq.lower()
    
        if numreq == "yes":
            numb = True
            break
        elif numreq == "no":
            numb = False
            break
        else:
            print  ("Please enter a valid answer.")
    
    while True:
        
        punctreq = str(input("Does your password require a symbol?: "))
        punctreq = punctreq.strip()
        punctreq = punctreq.lower()
        
        if punctreq == "yes":
            symb = True
            break
        elif punctreq == "no":
            symb = False
            break
        else:
            print  ("Please enter a valid answer.")
    
        
    while True:
        upperreq = str(input("Does your password require an uppercase letter?: "))
        upperreq = upperreq.strip()
        upperreq = upperreq.lower()
    
        
        if upperreq == "yes":
            cap = True
            break
        elif upperreq == "no":
            cap = False
            break
        else:
            print  ("Please enter a valid answer.")
        
    while True:
        lowerreq = str(input("Does your password require an lowercase letter?: "))
        lowerreq = lowerreq.strip()
        lowerreq = lowerreq.lower()
    
        
        if lowerreq == "yes":
            lower = True
            break
        elif lowerreq == "no":
            lower = False
            break
        else:
            print  ("Please enter a valid answer.")
            
    #Creating a variable for the final password
    #Creating a variables for checking requirements
    
    cheqlower = False
    cheqnumb = False
    cheqsymb = False
    cheqcap  = False
    
    finalpass = []
    strfinal = ""
    
    #Scrambling the list containing all characters
    random.shuffle(ps5)
    
    #Setting up the preferred length of the Password checking 
    #If it should just be the minimum value or a custom length
    
    if preflen == -1:
        preflen = minlen
    else:
        preflen = preflen
    

#Various If Statements to check what the user's password requires
#Contains Paramaters for 
#Lowercase letters, uppercase, digits and symbols
    for i in range(preflen):
        cheqnumb = False
        cheqsymb = False
        cheqcap  = False
    
    
#Check occurs halfway through to check password requirements
#Uppercase, lowercase, digits and symbols
#If a required field is not found it takes from the list containing the required
#value and adds it to the list, then continues the loop to check the rest of the conditions 

        if i >= preflen // 2:
            if numb == True:
                for x in finalpass:
                    if cheqnumb == True:
                        break
                    if x in ps1:
                        cheqnumb = True
                        numb = False
                if cheqnumb == False:
                    finalpass.append(ps1[random.randint(0,len(ps1))])
                    numb = False
                    continue
             
            
            if lower == True:
                for x in finalpass:
                    if cheqlower == True:
                        break
                    if x in ps3:
                        cheqlower = True
                        lower = False
                if cheqnumb == False:
                    finalpass.append(ps3[random.randint(0,len(ps3))])
                    lower = False
                    continue
                
            if symb == True:
                for x in finalpass:
                    if cheqsymb == True:
                        break
                    if x in ps2:
                        cheqsymb = True
                        symb = False
                if cheqnumb == False:
                    finalpass.append(ps2[random.randint(0,len(ps2))])
                    symb = False
                    continue
                
            if cap == True:
                for x in finalpass:
                    if cheqcap== True:
                        break
                    if x in ps4:
                        cheqcap = True
                        cap = False
                if cheqcap == False:
                    finalpass.append(ps4[random.randint(0,len(ps4))])
                    cap = False
                    continue
                
#If all conditions are satisfied the password just appends a random symbol to the final list             
        finalpass.append(ps5[i])
    for i in finalpass:
        strfinal = strfinal + i
    strfinal = strfinal.strip()
    
#The list converst into a string and then is printed out for the user
    print ("This is your new password! " + strfinal)
    return strfinal

password_generator();