from spotify import dataset

power_user = 0
lstPowerUser =[]

for record in dataset : 
    
    if float(record["listening_time"]) > 200 and float(record["songs_played_per_day"]) > 50 :
        power_user = power_user + 1
        lstPowerUser.append(record["user_id"])
        
print(f"Le nombre de power user est de : {power_user}")
print(f"Voici la liste des power user {lstPowerUser}")