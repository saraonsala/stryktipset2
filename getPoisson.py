import math

def getPoisson(l,n,t):
        #medelvärdet, hur många maskiner pajar i snitt per dag
        #l = 43.5
        #Förekomsten av att 6 maskiner pajar på två dagar
        #n = 50
        # tid
        #t = 1
        e = 2.71828
        result = ((l*t)**n)*(e**-(l*t))/math.factorial(n)
        #print (result)
        return result