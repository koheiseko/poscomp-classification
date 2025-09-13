def get_areas(especialidade, *areas):
    for valor, area in enumerate(areas):
        if especialidade in area:
            return valor