def imprimir_guia(dados):
    from escpos.printer import Serial

    p = Serial(devfile='COM5', baudrate=9600)

    p.text("GUARDA MUNICIPAL\n")
    p.text("GUIA DE REMOCAO\n\n")

    p.text(f"Veiculo: {dados['placa']}\n")
    p.text(f"Modelo: {dados['modelo']}\n")
    p.text(f"Cor: {dados['cor']}\n\n")

    p.text(f"Local: {dados['local']}\n")
    p.text(f"Motivo: {dados['motivo']}\n\n")

    p.text(f"Agente: {dados['agente']}\n")

    p.cut()