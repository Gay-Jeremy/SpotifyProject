from spotify import dataset

total =0 # Nombre Total d'utilisateur
churned = 0 # Nombre d'utilisateur ayant quitté le service
churnedFree = 0  # Nombre d'utilisateur ayant quitté le service avec un abonnement Free 
churnedFamily = 0 # Nombre d'utilisateur ayant quitté le service avec un abonnement Family 
churnedPremium = 0 # Nombre d'utilisateur ayant quitté le service avec un abonnement Premium 
churnedStudent = 0 # Nombre d'utilisateur ayant quitté le service avec un abonnement Student
at_risk_user = 0 # Nombre d'utilisateur à risque
noChurned = 0 # Nombre d'utilisateur non churned
mrrFree = 0 # MRR abonnement Free
mrrFamily = 0 # MRR abonnement Family
mrrStudent = 0 # MRR abonnement Student
mrrPremium = 0 # MRR abonnement Premium
country = []

#EXERCICE 1

for record in dataset:
    total = total + 1
    if record['is_churned'] =='1':
        churned = churned + 1

print(f"Total user: {total}")
print(f"Churn users: {churned}")

percentage= round((churned / total) * 100, 2)
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

# EXERCICE 2

for record in dataset:
    if record['subscription_type'] != 'Free'and record['skip_rate'] > '0.3' and record['listening_time'] < '100' or record['subscription_type'] == 'Free'and record['offline_listening'] == '0' and record['ads_listened_per_week'] > '20'  :
        at_risk_user = at_risk_user + 1

print(f"le nombre d'utilisateur à risque est {at_risk_user}")

percentage_at_risk_user= round((at_risk_user / total) * 100, 2)

print(f"Le taux d'utilisateur à risque est {percentage_at_risk_user}%")

for record in dataset:
    if record['is_churned'] =='0':
        noChurned = noChurned + 1
print (f"Nombre d'utilisateur non churned est de {noChurned}")

for record in dataset:
    if record['is_churned'] =='0' and record['country'] not in country :
        country.append(record['country'])
print (country)

for i in range(len(country)) :
    mrrFree = 0
    userNoChurnCountry = 0
    for record in dataset:
        if record['subscription_type'] == 'Free' and record['country'] == country[i]:
            userNoChurnCountry = userNoChurnCountry + 1
        if record['is_churned'] =='0' and record['subscription_type'] == 'Free' and record['country'] == country[i]:
            mrrFree = mrrFree + 1
    print (f"Total d'utilisateur du pays {country[i]} est de {userNoChurnCountry} ")
    print(f"Utilisateur no churned avec abonnement Free du pays {country[i]} est de {mrrFree} ")