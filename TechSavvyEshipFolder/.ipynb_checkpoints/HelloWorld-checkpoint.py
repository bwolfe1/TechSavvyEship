print ('Hello, World!')

minutes=42
seconds=42
km_mi=1.61
kms=10
def Seconds (minutes, seconds):
    Secondstotal=minutes*60
    Secondstotal+= seconds
    return Secondstotal

def miles (kms, km_mi):
    milestotal= km_mi * kms
    return milestotal

def racespeed ():
    mile=miles(kms, km_mi)
    second=Seconds(minutes, seconds)
    speed=second/mile
    return speed

def min_sec():
    speed_sec=racespeed()
    speed_min=0
    while speed_sec>60:
        speed_min+=1
        speed_sec+=-60
    return (str(speed_min) + " min, " + '{:.2f}'.format(speed_sec) + " sec")

def mi_hour():
    speed_sec=racespeed()
    speed_hr=speed_sec/(60*60)
    return speed_hr
    
print(Seconds(minutes, seconds))
print(miles(kms, km_mi))
print('{:.2f}'.format(racespeed()))
print(min_sec())
print('{:.5f}'.format(mi_hour()))


    