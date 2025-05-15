#Funksjon "is_crosswind" som lager et crosswind-område på angitt rullebane med hensyn til hvilken vinkel rullebanen har. 

def is_crosswind(runway_angle, wind_direction, wind_speed):
    
    #Denne funksjonen returnerer vinkelen mellom to retninger(0-180°).
    def angle_diff(a, b):
        return min((a - b) % 360, (b - a) % 360)
    # Vindhastighetsgrense i knop lik 35 i denne analysen. 
    wind_threshold = 34
    if wind_speed <= wind_threshold:
        return False

    x = runway_angle
    x_compl = (x + 180) % 360  # motsatt bane av x er lik x komplement 

    # Sjekk hvis banen eller motsatt bane er i det "kritiske intervallet" 45–135° i forhold til x og x komplement
    if (45 <= x <= 135) or (45 <= x_compl <= 135):
        return angle_diff(x, wind_direction) > 45 and angle_diff(x_compl, wind_direction) > 45
    else:
        # Velg den som er nærmest 180° og lengst fra 180°
        x_ok = min([x, x_compl], key=lambda x: abs(x - 180))
        x_prob = max([x, x_compl], key=lambda x: abs(x - 180))

        return (
            angle_diff(x_prob, wind_direction) > 45 and
            angle_diff(x_ok, wind_direction) > 45
        )
