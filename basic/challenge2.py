ace_of_teams = ['JUV : Ronaldo', 'CHE : Hazard', 'LIV : Salah', 'MNU : Pogba', 'INT : Icardi', 'BCN : Suarez', 'RMD : Modric']
podium = []

for ace_of_team in ace_of_teams:
    # podium.append(ace_of_team[6:].upper())
    podium.append(ace_of_team[ace_of_team.index(':') + 2:].upper())
# 각 ace 소팅해서 출력
podium.sort()
print(podium)