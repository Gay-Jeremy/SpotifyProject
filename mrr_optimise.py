from spotify import dataset

nbUser = {}

PRICES = {"Free": 0.0, "Premium": 9.99, "Family": 14.99, 
"Student": 4.99}

for record in dataset :

    country = record['country']                                                         #création de variable qui prend la valeur du record[country]
    typeAccount = record['subscription_type']                                           #création de variable qui prend la valeur du record[country]

    if country not in nbUser :  
        nbUser[country] = {}                                                            #initialisation du sous dictionnaire country dans le dictionnaire nbUser                     

    user = 0
    if country in nbUser :

        if typeAccount not in nbUser[country] and record["is_churned"] :                      
            nbUser[country][typeAccount] = 1                                            #initialisation du nombre d'utilisateur dans le sous dictionnaire country 

        elif typeAccount in nbUser[country] :
            nbUser[country][typeAccount] = nbUser[country][typeAccount] + 1             # incrémentation de 1 du nombre d'utilisateur du sous dictionnaire country
print(nbUser)

for country, subscription in nbUser.items() :
        for count in PRICES :
            totalMRR = int(subscription[count]) * float(PRICES[count])
            print(f'Pays: {country} Compte: {count} MRR: {round(totalMRR, 2)}€  ')



    


