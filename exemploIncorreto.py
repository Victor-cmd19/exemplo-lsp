class Veiculos:
    def locomocao():
        print("o veiculo se move utilizando motor")

class VeiculoMotor(Veiculos):
    pass

class VeiculoPedal(Veiculos):
    def locomocao():
          print("o veiculo se move por causa dos pedais")
    

veiculo = VeiculoPedal
veiculo.locomocao()
print(veiculo)

