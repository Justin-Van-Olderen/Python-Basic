import time #Importeer de time library

#Geeft de variablen aan
h  = int(input("Enter hours:"))
m  = int(input("Enter minutes:"))
s  = int(input("Enter seconds:"))

while True:
    if(h==24 and m==60 and s==60):  #Waaneer de tijd 23:59:59, reset de timer en gaat terug 00:00:00
        #Dit geeft de waarde 0 van de tijd
        h = 0
        m = 0
        s = 0
        for h in range(0,24,1):
            for m in range(0,60,1):
                for s in range(0,60,1):
                    time.sleep(1)   #Dit maakt een 1 seconden timer
                    print('{0:02}'.format(h) + ":" + '{0:02}'.format(m) + ":" + '{0:02}'.format(s)) #Resets timer to 00:00:00 in output. #Shouws 2 base numbers on output

    else:  
        for h in range(h,25,1): #houdt de tijd onder 25 uur
            #Waarneer uren 24 zijn, reset hij
            if h == 24:
                h = 0
            else:
                for m in range(m,61,1): #Houdt de minuten onder de 61
                    #Waarneer de minuten 60 zijn, reset hij
                    if m == 60:
                        m = 0
                    else:
                        for s in range(s,61,1): #Houdt de seconden onder de 61
                            #Waarneer de seconden 60 zijn, reset hij
                            if s == 60:
                                s = 0
                            else:
                                time.sleep(1)   #Hierdoor Komt er 1 seconden bij telkens(gaat ie niet te snel)
                                print('{0:02}'.format(h) + ":" + '{0:02}'.format(m) + ":" + '{0:02}'.format(s)) #Hier wordt de timer geprint op het scherm
