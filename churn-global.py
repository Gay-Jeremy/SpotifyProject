from spotify import dataset

total =0 # Nombre Total d'utilisateur
churned = 0 # Nombre d'utilisateur ayant quité le service

for record in dataset:
    total = total + 1
    if record['is_churned'] =='1':
        churned = churned + 1

print(f"Total user: {total}")
print(f"Churn users: {churned}")

percentage= round((churned / total) * 100, 2)
print(f"Churn rate : {percentage}%")
