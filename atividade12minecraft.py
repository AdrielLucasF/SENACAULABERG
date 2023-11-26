#creeper
# velocidade - 2  explosão - 5  perseguição 20  spawn qualquer momento  dano - 20% a cada bloco  tempoExplosão - 2
# andar perseguir explodir

class Creepper:
    def __init__(self, vida, vel, spawn, perseguicao, explosao, dano, tempoExplosao):
        self.vida = vida
        self.velocidade = vel
        self.spawn = spawn
        self.perseguicao = perseguicao
        self.explosao = explosao
        self.dano = dano
        self.tempoEx = tempoExplosao

    def toString(self):
        return f"vida:{self.vida}\nvelocidade:{self.velocidade}\nspawn:{self.spawn}\nraio de perseguição:{self.perseguicao}\nraio da explosão:{self.explosao}\ndano por proximidade de bloco:{self.dano}%\ntempo pra explosão:{self.tempoEx} segundos."

# esqueleto
# vel 5  percepção 12  dano 20%  spawn à noite
# andar perseguir atirar

class Esqueleto:
    def __init__(self, vida, vel, spawn, perseguicao, dano):
        self.vida = vida
        self.velocidade = vel
        self.spawn = spawn
        self.perseguicao = perseguicao
        self.dano = dano

    def toString(self):
        return f"vida:{self.vida}\nvelocidade:{self.velocidade}\nspawn:{self.spawn}\nperseguição:{self.perseguicao}\ndano:{self.dano}% da vida máxima do player."

creepin = Creepper(50, 2, "Qualquer horário", 20, 5, 20, 2)
esqueletin = Esqueleto(70, 5, "à noite", 12, 20)

print("Esqueleto\n",esqueletin.toString())
print("Creeper\n",creepin.toString())

# Todos os atributos da classe Esqueleto têm semelhança com os da classe Creeper