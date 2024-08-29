#this shit is to tell me when to put the thingy in the ruby or jade slot to get bonus cps
#don't ask, i have too much free time

import datetime
import math
import os

timeZone = -3

#--------------------------------------------------------------------------------

def calcJade(time):
    jade = 15 * math.sin( ((2*math.pi)/24) * (time - timeZone) )
    return jade

#--------------------------------------------------------------------------------

def calcRuby(time):
    ruby = 15 * math.sin( ((2*math.pi)/12) * (time - timeZone) )
    return ruby

#--------------------------------------------------------------------------------

def nextGood(hour, type):
    while True:
        if(type == 0):
            bonus = calcJade(hour)
        else:
            bonus = calcRuby(hour)
            
        if bonus >= 0:
            return hour-1
    
        hour = hour + 1

#--------------------------------------------------------------------------------
    
def nextBad(hour, type):    
    while True:
        if(type == 0):
            bonus = calcJade(hour)
        else:
            bonus = calcRuby(hour)
        
        if bonus <= 0:
            return hour-1
               
        hour = hour + 1

#--------------------------------------------------------------------------------

def fixTime(hour):
    if hour > 23:
        return hour - 24
    else:
        return hour

#--------------------------------------------------------------------------------

print("Temple thingy\n")

hour = int(datetime.datetime.now().strftime("%H")) 
minute = int(datetime.datetime.now().strftime("%M"))

time = hour + round((minute/60), 2)

jade = round(calcJade(time), 2)
ruby = round(calcRuby(time), 2)
    
print("Time = "+str(hour)+":"+str(minute)+" ("+str(hour - timeZone)+" UTC)\n   Jade bonus = "+str(jade)+"%\n   Ruby bonus = "+str(ruby)+"%\n")
    
if jade >= ruby and jade > 0:
    nextJadeB = nextBad(hour+1, 0)
    h = hour
        
    while h < nextJadeB:
        h = h + 1
        jade = round(calcJade(h), 2)
        ruby = round(calcRuby(h), 2)

        if jade < ruby:
            break
          
    if h < nextJadeB:
        h = fixTime(h)
        print("Keep the thing in the Jade slot\nRuby is better after "+str(h-1)+" ("+str((h-1) - timeZone)+" UTC)\n")
        
    else:
        nextJadeB = fixTime(nextJadeB)
        print("Keep the thing in the Jade slot until "+str(nextJadeB)+" ("+str(nextJadeB - timeZone)+" UTC)\n")

                
elif ruby >= jade and ruby > 0:
    nextRubyB = nextBad(hour+1, 1)
    h = hour
        
    while h < nextRubyB:
        h = h + 1
        jade = round(calcJade(h), 2)
        ruby = round(calcRuby(h), 2)      

        if ruby < jade:
            break
          
    if h < nextRubyB:
        h = fixTime(h)
        print("Keep the thing in the Ruby slot\nJade is better after "+str(h-1)+" ("+str((h-1) - timeZone)+" UTC)\n")
        
    else:
        nextRubyB = fixTime(nextRubyB)
        print("Keep the thing in the Ruby slot until "+str(nextRubyB)+" ("+str(nextRubyB - timeZone)+" UTC)\n")
        
else:
    print("No bonus for now\n")
    
    nextJadeG = nextGood(hour+1, 0)
    nextRubyG = nextGood(hour+1, 1)
    
    if nextJadeG < nextRubyG:
        nextJadeG = fixTime(nextJadeG)
        print("Next Jade bonus at "+str(nextJadeG)+" ("+str(nextJadeG - timeZone)+" UTC)\n")
    else:
        nextRubyG = fixTime(nextRubyG)
        print("Next Ruby bonus at "+str(nextRubyG)+" ("+str(nextRubyG - timeZone)+" UTC)\n")

print("byebye :(\n")
