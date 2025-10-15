label proximo_caminho:

    menu:
        "O que você quer fazer agora?"

        "Ir com Cherry" if not cena_cherry:
            $ cena_cherry = True
            jump CaminhoCherry

        "Ir com Blueberry" if not cena_blueberry:
            $ cena_blueberry = True
            jump CaminhoBlueberry

        "Ir com Citrus" if not cena_citrus:
            $ cena_citrus = True
            jump CaminhoCitrus

        "Seguir a história principal":
            jump VerdadeConsequencia
