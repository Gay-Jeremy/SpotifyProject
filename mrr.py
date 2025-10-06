from spotify import dataset

country = []

typeAccount = []

PRICES = {"Free": 0.0, "Premium": 9.99, "Family": 14.99, 
"Student": 4.99}


for record in dataset:
    if record['country'] not in country :
        country.append(record['country'])


for record in dataset:
    if record['subscription_type'] not in typeAccount :
        typeAccount.append(record['subscription_type'])


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


