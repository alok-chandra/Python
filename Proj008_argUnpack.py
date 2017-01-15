def HealthMtr(age=30,apple=25,drinks=5):
    answer = (age*10) + (apple *5) - (drinks*10)
    print(answer)

cuck_data= [11,11,5]
HealthMtr(*cuck_data)
HealthMtr(cuck_data[0],cuck_data[1],cuck_data[2])