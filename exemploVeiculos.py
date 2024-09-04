class Veiculos:
    def locomocao():
        print("o veiculo se move")

class VeiculoMotor(Veiculos):
    def motor():
        print("o veiculo possui motor")

class VeiculoPedal(Veiculos):
    def pedal():
          print("o veiculo possui pedais")
    

veiculo = VeiculoPedal
veiculo.locomocao()
print(veiculo)


