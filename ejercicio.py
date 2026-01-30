# Crear un programa que calcule cuánto debe pagar un cliente. El precio base es de $5 por hora.

# Reglas:
# Tiempo máximo: Si el cliente se queda más de 24 horas (1440 minutos), se le cobra una tarifa fija de $150 y no se aplican más descuentos.

# Tipo de Vehículo:

# Si es "Moto": Tiene un 15% de descuento sobre el total.

# Si es "Auto": No tiene descuento por tipo.

# Día de la semana:

# Si es "Domingo": Se aplica un descuento adicional del 10% sobre el monto que lleve acumulado.

# Restricción:
# Usa condicionales anidados para separar primero el caso de "Larga Estancia" (> 24h) de los casos de estancia normal.

minutos = int(input("Minutos de parqueo: "))
tipo_vehiculo = input("auto o moto): ")
dia_semana = input("Día de la semana: ")

# 1. Verificamos si supera las 24 horas
if minutos > 1440:
    total = 150.0
    print(f"Tarifa plana por larga estancia aplicada: ${total}") 
else:
    # Calculamos precio base ($5 por hora o fracción)
    horas = minutos / 60
    total = horas * 5
    
    # 2. Anidamos los descuentos según el vehículo
    if tipo_vehiculo == "moto":
        total = total * 0.85  # Aplica 15% de descuento
        
        # 3. Anidamos el descuento por día dentro del tipo de vehículo
        if dia_semana == "domingo":
            total = total * 0.90  # Aplica 10% adicional
    else:
        # Es un auto, solo revisamos el día
        if dia_semana == "domingo":
            total = total * 0.90
            
    print(f"Total a pagar por {horas:.2f} horas: ${total:.2f}")