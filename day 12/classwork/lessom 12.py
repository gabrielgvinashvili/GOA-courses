user_score = int(input("რამდენი მიიღე ტესტში:    "))
score1 = (90 or 100) 
score2 = (70 or 80)
score3 = (40 or 70)
score4 = (40)

if user_score > score1:
    print("თქვენ დაგიფინანსდებათ სრულიად")

elif user_score < score2:
    print("თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით")

elif user_score < score3:
    print("თქვენ დაგიფინანსდებათ სწავლა 500 ლარით")