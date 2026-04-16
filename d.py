from escpos.printer import Usb

# Ajustar IDs USB da DPP-250
p = Usb(0x04b8, 0x0202)  # pode mudar dependendo do driver

p.set(align='center', text_type='B', width=2, height=2)
p.text("GUARDA MUNICIPAL\n")

p.set(align='center', width=1, height=1)
p.text("GUIA DE REMOCAO\n\n")

p.set(align='left')
p.text("Data: 16/04/2026\n")
p.text("Hora: 10:30\n\n")

p.text("Veiculo: ABC-1234\n")
p.text("Modelo: Gol\n")
p.text("Cor: Branco\n\n")

p.text("Local: Centro\n")
p.text("Motivo: Estacionamento irregular\n\n")

p.text("Agente: Joao Henrique\n\n")

p.text("------------------------------\n")
p.text("Assinatura\n\n")

p.cut()