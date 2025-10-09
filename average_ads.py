from spotify import dataset

# Initialisation dictionnaire 
nbUserAccount = {}                                                     
nbAdsAccount = {}

# Boucle sur les record du dataset
for record in dataset :

# Initialisation de varaiable 
    subscription_type = record['subscription_type']         
    adsAccount = int(record['ads_listened_per_week'])

# Condition
    if subscription_type not in nbUserAccount :
        nbUserAccount[subscription_type] = 0

    if subscription_type in nbUserAccount :
        nbUserAccount[subscription_type] += 1

    if subscription_type not in nbAdsAccount :
        nbAdsAccount[subscription_type] = adsAccount
    else : 
        nbAdsAccount[subscription_type] += adsAccount

print (nbUserAccount)
print (nbAdsAccount)

# Boucle dans le dictionnaire nbUserAccount
for key in nbUserAccount :

    if nbAdsAccount.get(key) != 0 :
        average_ads =  nbAdsAccount.get(key) / nbUserAccount.get(key)
print (round(average_ads , 2))
    




    



    


        




        

  


