from spotify import dataset

total =0 # Nombre Total d'utilisateur
churned = 0 # Nombre d'utilisateur ayant quitté le service
churnedFree = 0  # Nombre d'utilisateur ayant quitté le service avec un abonnement Free 
churnedFamily = 0 # Nombre d'utilisateur ayant quitté le service avec un abonnement Family 
churnedPremium = 0 # Nombre d'utilisateur ayant quitté le service avec un abonnement Premium 
churnedStudent = 0 # Nombre d'utilisateur ayant quitté le service avec un abonnement Student
noChurned = 0 # Nombre d'utilisateur non churned



#EXERCICE 1

for record in dataset:
    total = total + 1
    if record['is_churned'] =='1':
        churned = churned + 1

print(f"Total user: {total}")
print(f"Churn users: {churned}")

percentage = round((churned / total) * 100, 2)
print(f"Churn rate : {percentage}%")

for record in dataset:
    total = total + 1
    if record['is_churned'] =='1'and record['subscription_type'] == 'Free':
        churnedFree = churnedFree + 1
    elif record['is_churned'] =='1'and record['subscription_type'] == 'Family':
        churnedFamily = churnedFamily + 1
    elif record['is_churned'] =='1'and record['subscription_type'] == 'Premium':
        churnedPremium = churnedPremium + 1
    elif record['is_churned'] =='1'and record['subscription_type'] == 'Student':
        churnedStudent = churnedStudent + 1

print(f"Total churned Free: {churnedFree}")
print(f"Total churned Family: {churnedFamily}")
print(f"Total churned Premium: {churnedPremium}")
print(f"Total churned Student: {churnedStudent}")

percentageFree= round((churnedFree / total) * 100, 2)
print(f"Churn rate Free: {percentageFree}%")

percentageFamily= round((churnedFamily / total) * 100, 2)
print(f"Churn rate Family: {percentageFamily}%")

percentageStudent= round((churnedStudent / total) * 100, 2)
print(f"Churn rate Premium : {percentageStudent}%")

percentagePremium= round((churnedPremium / total) * 100, 2)
print(f"Churn rate Student: {percentagePremium}%")



for record in dataset:
    if record['is_churned'] =='0':
        noChurned = noChurned + 1
print (f"Nombre d'utilisateur non churned est de {noChurned}")




