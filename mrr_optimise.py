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

revenu = {} 
for country, subscriptions in nbUser.items(): 
    
    for subType, count in subscriptions.items(): 
        total = 0 
        price = PRICES[subType] 
        total += price * count 
        revenu[subType] = round(total, 2) 
        print(f"{country} le revenu de {subType} est de {round(total,2)}€")



    


