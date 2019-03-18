import math
r=20.16
r1=9.13
r2=11.55
r_list=[r,r1,r2]
def Area (r): 
    Area_= math.pi * (r**2)
    return Area_

#for r in r_list:
    #print ("area of circle with radius of " + str(r) + ": \n" + str(Area(r)))
#secret_code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#decoded=""  

#for letter in secret_code:
    #if letter!= " " or "." or "'" or "(" or ")":
       # num = ord(letter)
        #num+=2
       # decoded += chr(num)
    #else: 
      #  decoded += letter

#print(decoded)

def sqr_1(a):
    result = a*a +1
    return result

#print (sqr_1(10))

def Quadratic(a,b,c):
    if (b**2 - 4*a*c)/2*a >=0:
        add_x=math.sqrt((b**2 - 4*a*c)/(2*a))
        sub_x=math.sqrt((b**2 - 4*a*c)/(2*a))
        add_x="{:.2f}".format(add_x)
        sub_x="{:.2f}".format(sub_x)
    else:
        add_x=math.sqrt(abs((b**2 - 4*a*c)/(2*a)))
        sub_x=math.sqrt(abs((b**2 - 4*a*c)/(2*a)))
        add_x="-" + str(b)+ "+" + "{:.2f}".format(add_x)+"i"
        sub_x="-" + str(b)+ "-" + "{:.2f}".format(sub_x)+"i"
    return add_x + ", "+ sub_x

#a=int(input("type a number"))
#b=int(input("type a number"))
#c=int(input("type a number"))

#print("the two roots are: "+ Quadratic(a,b,c))

def BMI(lbs, inch):
    BMI_score=703*lbs/(inch**2)
    if BMI_score<18.5:
        print("underweight")
    elif BMI_score<24.9:
        print("normal weight")
    elif BMI_score<29.9:
        print("overweight")
    else: 
        print("obese")
        
    return BMI_score
        
#lbs=int(input("Type weight in lbs: \n"))
#inch=int(input("Type height in inches: \n"))
#BMIs=str(BMI(lbs, inch))

#print("With BMI of:" + BMIs)

team="New England Patriots"

#letter=team[1]

prefixes= ['J', 'K', 'L', 'M', 'N', 'Ou', 'P', 'Qu']
suffix = 'ack'

#for letter in prefixes:
   # print (letter + suffix)

    
#print(team[4:11]) #England

#print(team[12:]) #Patriots

#print (team[::2]) #Every other Character

#print(team[::-1]) #Backwords

#print(team.find('e')) #finds the first instance of the given character

#print(team.endswith("ts")) # tells you if the actual suffix matches given suffix

#print(team.endswith("t"))

