ingreso_mensual = 5000

if ingreso_mensual > 10000:
    if gasto_mensual < 7000:
        print("tus gastos están controlados")
        print("estas bien en cualquier parte del mundo")
    else:
        print("estás gastando demasiado del ingreso")
    
elif ingreso_mensual > 1000:
    print("estas bien en Alemania")
    
elif ingreso_mensual > 800:
    print("estas bien en Colombia")
    
elif ingreso_mensual > 500:
    print("estas bien en Venezuela")
    
else:
    print("eres pobre")