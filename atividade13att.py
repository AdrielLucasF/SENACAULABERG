import random
#creeper
# velocidade - 2  explosão - 5  perseguição 20  spawn qualquer momento  dano - 20% a cada bloco  tempoExplosão - 2
# andar perseguir explodir

class Creepper:
    def __init__(self, vida, vel, spawn, rangePerseguicao, posicao, explosao, dano, tempoExplosao):
        self.vida = vida
        self.velocidade = vel
        self.spawn = spawn
        self.perseguicao = rangePerseguicao
        self.posicao = posicao
        self.explosao = explosao
        self.dano = dano
        self.tempoEx = tempoExplosao

    def toString(self):
        return f"vida:{self.vida}\nvelocidade:{self.velocidade}\nspawn:{self.spawn}\ncoordenadas: x-{self.posicao[0]}  y-{self.posicao[1]}\nraio de perseguição:{self.perseguicao}\nraio da explosão:{self.explosao}\ndano por proximidade de bloco:{self.dano}%\ntempo pra explosão:{self.tempoEx} segundos.\n"
    
    def explodir(self, player):
        posicaoPlayer = player.posicao
        ranPeserseguir = []
        ranExplodir = []

        for i in range(-self.perseguicao,self.perseguicao+1):
            ranPeserseguir.append(i)
        for i in range(-self.explosao,self.explosao+1):
            ranExplodir.append(i)
        #se o x e y do player estiver dentro do range de visão do creeper, de acordo com a posição de ambos
        if posicaoPlayer[0]-self.posicao[0] in ranPeserseguir:
            if posicaoPlayer[1]-self.posicao[1] in ranPeserseguir:
                #creeper andará até chegar numa distância mais perto do Player
                self.posicao[0] = random.randrange(0,posicaoPlayer[0])
                self.posicao[1] = random.randrange(0,posicaoPlayer[1])
                if posicaoPlayer[0]-self.posicao[0] in ranExplodir:
                    if posicaoPlayer[1]-self.posicao[1] in ranExplodir:
                        print((posicaoPlayer[1]-self.posicao[1]))
                        print(f"O creeper explodiu! você recebeu {self.dano*(posicaoPlayer[1]-self.posicao[1])} de dano")
                    else:
                        print("Ufa, o creeper não está perto o suficiente")
                else:
                    print("Ufa, o creeper não está perto o suficiente")
            else:
                print("Ufa, você não está no range do creeper")
        else:
            print("Ufa, você não está no range do creeper")

# esqueleto
# vel 5  percepção 12  dano 20%  spawn à noite
# andar perseguir atirar

class Esqueleto:
    def __init__(self, vida, vel, spawn, rangePerseguicao, posicao, dano):
        self.vida = vida
        self.velocidade = vel
        self.spawn = spawn
        self.perseguicao = rangePerseguicao
        self.posicao = posicao
        self.dano = dano

    def toString(self):
        return f"vida:{self.vida}\nvelocidade:{self.velocidade}\nspawn:{self.spawn}\ncoordenadas: x-{self.posicao[0]}  y-{self.posicao[1]}\nraio de perseguição:{self.perseguicao}\ndano:{self.dano}% da vida máxima do player.\n"
    
    #metodo de atira casso o range de perseguição seja válido
    def atirar(self, player):
        posicaoPlayer = player.posicao
        ranPeserseguir = []
        for i in range(-self.perseguicao,self.perseguicao+1):
            ranPeserseguir.append(i)

        #se o x e y do player estiver dentro do range de visão do esqueleto, de acordo com a posição de ambos
        if posicaoPlayer[0]-self.posicao[0] in ranPeserseguir:
            if posicaoPlayer[1]-self.posicao[1] in ranPeserseguir:
                print(f"O esqueleto atirou! você recebeu {self.dano} de dano")
            else:
                print("Ufa, você não está no range do esqueleto")
        else:
            print("Ufa, você não está no range do esqueleto")

# player
# vida 100  vel 8  
class Player:
    def __init__(self, vida, vel, posicao):
        self.vida = vida
        self.velocidade = vel
        self.posicao = posicao
    
    def toString(self):
        return f"vida:{self.vida}\nvelocidade:{self.velocidade}\ncoordenadas: x-{self.posicao[0]}  y-{self.posicao[1]}\n"

creepin = Creepper(50, 2, "Qualquer horário", 20, [random.randrange(0, 30), random.randrange(0,30)], 5, 20, 2)
esqueletin = Esqueleto(70, 5, "à noite", 12,[random.randrange(0, 30), random.randrange(0,30)], 20)
stevin = Player(100, 8, [random.randrange(0, 30), random.randrange(0,30)])

print("Esqueleto\n",esqueletin.toString())
print("Creeper\n",creepin.toString())
print("Player\n",stevin.toString())

esqueletin.atirar(stevin)
creepin.explodir(stevin)
# Todos os atributos da classe Esqueleto têm semelhança com os da classe Creeper, mas o Creeper é mais complexo