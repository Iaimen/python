import time
t=time.strftime('%H,%M,%S')
hour=(int(time.strftime('%H')))
print(hour)

# measurement of time through hours
if(hour>=0 and hour<12):
    print('Good Morning')
elif(hour>=12 and hour<18):
    print('Good Afternoon')
elif(hour>=18 and hour<24):
    print('Good Night')