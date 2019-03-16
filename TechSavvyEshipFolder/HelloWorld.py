#print ('Hello, World!')

minutes=62
seconds=10
km_mi=1.61
kms=10
def Seconds (minutes, seconds):
    Secondstotal=minutes*60
    Secondstotal+= seconds
    return Secondstotal

def miles (kms, km_mi):
    milestotal= kms/ km_mi
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
    return 'minutes and seconds a mile: {} min, {:.2f} sec'.format(speed_min, speed_sec)
def mi_hour():
    speed_sec=racespeed()
    speed_hr=(60*60)/speed_sec
    return speed_hr
    
print("total seconds: " + str(Seconds(minutes, seconds)))
print("total miles: " + str(miles(kms, km_mi)))
print('Speed in seconds a mile: {:.2f}'.format(racespeed()))
print(min_sec())
print('miles/hour: {:.5f}'.format(mi_hour()))


    