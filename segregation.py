
# print("hello world !!")

# def segregate(volt):

def identify_device(power: float) -> dict:

    device = None
    # fridge, press, washing_machine, tv ,grinder, frother, roti maker, bulb, fan, geyser, charger,
    #  kettle, induction, air freshner, heater, hair dryer, oven, AC, messager, motor, cooler
    if 5 <= power < 15:
        device = "Bulb"
    elif 18<= power <40:
        device = "Charger"
    elif 40 <= power < 90:
        device = "Fan or upto 55 inches TV"
    elif 90 <= power<160:
        device = "upto 65 inches TV"
    elif 100 <= power < 300:
        device = "Fridge"
    elif 300 <= power < 700:
        device = "Roti Maker, Kettle, Cooler"
    elif 700 <= power < 1500:
        device = "Washing Machine, Geyser, Motor"
    elif 1500 <= power < 2500:
        device = "Fridge, Press, Heater, Oven"
    elif power >= 2500:
        device = "AC, Hair Dryer"
    else:
        device = "Unknown Device"
    return {
        "Input Power (W)": power,
        "Possible Device(s)": device
    }


# dict = identify_device(1200)
# print(dict)
