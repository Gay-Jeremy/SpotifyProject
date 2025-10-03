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
typeAccount = []
PRICES = {"Free": 0.0, "Premium": 9.99, "Family": 14.99, 
"Student": 4.99}

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
    if record['country'] not in country :
        country.append(record['country'])
print (country)

for record in dataset:
    if record['subscription_type'] not in typeAccount :
        typeAccount.append(record['subscription_type'])
print (typeAccount)
print("")


for i in range(len(country)) :

    for j in range(len(typeAccount)) :

        nbUser = 0
        userCountry = 0


        for record in dataset:


            if record['subscription_type'] == typeAccount[j] and record['country'] == country[i]:
            
                userCountry = userCountry + 1
            
            
            if record['is_churned'] =='0' and record['subscription_type'] == typeAccount[j] and record['country'] == country[i]:
                
                nbUser = nbUser + 1

        print (f"Nombre d'utilisateur du pays {country[i]} ayant une compte {typeAccount[j]} est de {userCountry} ")
        print(f"Utilisateur no churned avec abonnement {typeAccount[j]} du pays {country[i]} est de {nbUser} ")
        print (f"Le MRR des abonnement {typeAccount[j]} du pays {country[i]} est de : {round(nbUser *PRICES[typeAccount[j]])}€")
        print(" ")



