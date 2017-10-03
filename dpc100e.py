# DPC 100 [E]
# Sleep Cycle Estimator

def specific_cycle(hours,minutes):
  print """\nhow many cycles of sleep do you want
  1 cycle  = 1.5 hours
  2 cycles = 3   hours
  3 cycles = 4.5 hours
  4 cycles = 6   hours
  5 cycles = 7.5 hours
  6 cycles = 9   hours
  7 cycles = 10.5hours
  8 cycles = 12  hours"""
  
  cycles = int(raw_input("\ntype a number less than 9 >> "))
  duration = cycles*1.5
  dhour = int(duration)
  dmin = int((duration-dhour)*60)
  
  while (dmin > minutes):
    hours -= 1
    minutes += 60
  
  minutes -= dmin
  hours -= dhour
  
  if (hours < 0):
    hours += 24
  else:
    hours = hours
  
  if (hours > 12):
    mthing = "pm"
    hours -= 12
  elif (hours == 0):
    mthing = "am"
    hours += 12
  else:
    mthing = "am"
    
  if (minutes == 0):
    minutes = "00"
  else:
    minutes = str(minutes)
    
  print "\nsleep duration, get in bed time"
  print duration, "hr, %d:%s %s" %(hours,minutes,mthing)
  
def all_hours(hours,minutes):
  print "\nsleep duration, get in bed time"
  
  for cycles in range(1,7):
    duration = cycles*1.5
    dhour = int(duration)
    dmin = int((duration-dhour)*60)
    
    hours2 = hours - dhour
    minutes2 = minutes - dmin
    if (minutes2 < 0):
      hours2 -= 1
      minutes2 += 60
    else:
      minutes2 = minutes2
    if (hours2 < 0):
      hours2 += 24
    else:
      hours2 = hours2
    if (hours2 > 12):
      mthing = "pm"
      hours2 -= 12
    elif (hours2 == 0):
      mthing = "am"
      hours2 += 12
    else:
      mthing = "am"
      
    if (minutes2 == 0):
      minutes2 = "00"
    else:
      minutes2 = str(int(minutes2))
      
    print duration, "hr, %d:%s %s" %(hours2,minutes2,mthing)



print "Enter waking time (military style)"
print "ex. 6:15 pm = 1815"
wake = int(raw_input(">> "))

print "\nHow many minutes from in bed to asleep"
presleep = int(raw_input(">> "))

hours = wake/100
minutes = wake - hours*100
while (presleep > minutes):
  hours -= 1
  minutes += 60
minutes -= presleep

print "\ns - input sleep time"
print "otherkey - see all cycles possible <= 9 hr"
if (raw_input(">> ") == "s"):
  specific_cycle(hours,minutes)
else:
  all_hours(hours,minutes)  
