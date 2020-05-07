
while True:
    try:
        time = input("givr me time [ex. 12:17]: ")
        in_hours = int(time.split(":")[0])
        in_minutes = int(time.split(":")[1])
        assert 0 <= in_hours <= 60, "Wrong hours plz give a valid one..!!!"
        assert 0 <= in_minutes <= 60, "Wrong hours plz give a valid one..!!!"
        break
    except AssertionError as assert_msg:
        print(assert_msg)
        
    

duration = int(input("for how long [ex. 59]in min: "))


#from math: 
#? t + n = f (mod 24) if time is in 24 {where t: current time, n: time in future with hours}
#TODO [12:17] , (59 min) we will get the time in hours in future after that add the minutes
#! but since we get duratin in min we need to change it to hours first 


#check if duration will be added to hour or min
if duration < 60:
   out_min = in_minutes + duration
   if out_min > 60:
      out_hours = int(out_min/60)
      out_min = out_min%60
      
      ans_h = in_hours + out_hours
      ans_min = out_min
else:
    d_hours = int(duration/60)
    d_min = duration%60
   
    ans_min = in_minutes + d_min
   
    extra_h = 0
    if ans_min >  60:
        extra_h = int(ans_min/60)
        ans_min = ans_min%60
    else:
        ans_min = in_minutes + d_min

    ans_h = in_hours + d_hours + extra_h
    if ans_h > 24:
        ans_h = ans_h - 24

   
   
#show ans_h/min in the appropriate way

print(f"{ans_h}:{ans_min}")








