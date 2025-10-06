from spotify import dataset

nbUser = {}

PRICES = {"Free": 0.0, "Premium": 9.99, "Family": 14.99, 
"Student": 4.99}

for record in dataset :

    country = record['country']
    typeAccount = record['subscription_type']

    if country not in nbUser :
        nbUser[country] = {}

    user = 0
    if country in nbUser :
       
        if typeAccount not in nbUser[country] :
            nbUser[country][typeAccount] = 1

        elif typeAccount in nbUser[country] :
            nbUser[country][typeAccount] = nbUser[country][typeAccount] + 1
print(nbUser)


