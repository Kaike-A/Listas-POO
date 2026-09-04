sensor1 = float(input("Digite a temperatura do sensor 1: "))
sensor2 = float(input("Digite a temperatura do sensor 2: "))
sensor3 = float(input("Digite a temperatura do sensor 3: "))

media_temperatura = (sensor1 + sensor2 + sensor3) / 3

print(f"Temperatura média registrada: {media_temperatura:.2f}")