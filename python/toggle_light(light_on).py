def toggle_light(light_on):
    if light_on: 
        light_on = False
        print("LIGHT TURNED OFF.")

    else:
        light_on =  True
        print("LIGHT TURNED ON,")
    return light_on


toggle_light("")
