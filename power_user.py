from spotify import dataset

power_user = 0

for record in dataset : 
    
    if float(record['listening_time']) > 200 and float(record['songs_played_per_day']) > 50 :
     power_user = power_user + 1

print(power_user)