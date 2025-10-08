# EXERCICE 2
from spotify import dataset

total = 0
at_risk_user = 0

for record in dataset :
    total = total + 1

    firstCondition = float(record['skip_rate']) > 0.3 and float(record['listening_time']) < 100
    secondCondition = (record['subscription_type'] == 'Free'and int(record['offline_listening']) == 0 and float(record['ads_listened_per_week']) > 20)

    if firstCondition or secondCondition :
        at_risk_user = at_risk_user + 1

print(f"le nombre d'utilisateur à risque est {at_risk_user}")

percentage_at_risk_user= round((at_risk_user / total) * 100, 2)

print(f"Le taux d'utilisateur à risque est {percentage_at_risk_user}%") 