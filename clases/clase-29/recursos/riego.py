def riego_total(turnos, caudal):
    total = 0
    for minutos in turnos:
        total += minutos * caudal
    return total


turnos = [30, 45, 20]
print(riego_total(turnos, 12))
