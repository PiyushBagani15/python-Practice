def switch(day:int) -> str:
   week_dict={
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
   }
   return week_dict.get(day,"Day is Invalid")
print(switch(7))