import psycopg2
#pip install psycopg2
import datetime
import numpy as np

#campos Nome	CPF	Contato	Destino	Motivo	Observação	Data	Hora
class Acesso:
    def __init__(self, id, nome, cpf, contato, destino, motivo, observacao, data, hora):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.destino = destino
        self.motivo = motivo
        self.observacao = observacao
        self.data = data
        self.hora = hora

    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    
    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    
    def setCPF(self, cpf):
        self.cpf = cpf
    def getCPF(self):
        return self.cpf
    
    def setContato(self, contato):
        self.contato = contato
    def getContato(self):
        return self.contato
    
    def setDestino(self, destino):
        self.destino = destino
    def getDestino(self):
        return self.destino
    
    def setMotivo(self, motivo):
        self.motivo = motivo
    def getMotivo(self):
        return self.motivo
    
    def setObservacao(self, observacao):
        self.observacao = observacao
    def getObservacao(self):
        return self.observacao
    
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    
    def setHora(self, hora):
        self.hora = hora
    def getHora(self):
        return self.hora

    def to_string(self):
        print("ID: " + self.id + ", Nome: " + self.nome + ", CPF: " + self.cpf + ", Contato: " + self.contato + ", Destino: " + self.destino + ", Motivo: " + self.motivo + ", Observação: " + self.observacao + ", Data: " + self.data + ", Hora: " + self.hora + "\n")

#conecta ao BD
conn = psycopg2.connect(database="controle_acesso", user='######', password='#####', host='127.0.0.1', port='5432')
conn.autocommit = True
cursor = conn.cursor()

def inserir(acesso):
    #inserir informação
    cursor.execute("""INSERT INTO controle_acesso.acesso(id, nome, cpf, contato, destino, motivo, obs, data, hora) VALUES (nextval('hibernate_sequence'), %s, %s,%s, %s, %s, %s, %s, %s);""",(acesso.getNome(),acesso.getCPF(),acesso.getContato(), acesso.getDestino(),acesso.getMotivo(), acesso.getObservacao(), acesso.getData(), acesso.getHora()))

def listar_tudo():
    #consultar informação
    cursor.execute("SELECT * FROM controle_acesso.acesso;")

    #transforma o resultado da consulta em uma lista com os objetos Acesso
    lista = []
    for i in cursor.fetchall():
        arr = np.asarray(i)
        acesso = Acesso(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8])
        lista.append(acesso)
    return lista

def remover(id):
    #remover informação pelo ID
    cursor.execute("""DELETE FROM controle_acesso.acesso WHERE id = %s;""",(id,))

def atualizar(acesso):
    #campos Nome	CPF	Contato	Destino	Motivo	Observação	Data	Hora
    cursor.execute("""UPDATE controle_acesso.acesso SET nome = %s, cpf = %s ,contato = %s, destino = %s, motivo = %s, obs = %s, data = %s, hora = %s WHERE id= %s""",(acesso.getNome(),acesso.getCPF(),acesso.getContato(), acesso.getDestino(),acesso.getMotivo(), acesso.getObservacao(), acesso.getData(), acesso.getHora(),acesso.getId()))

if __name__ == "__main__":
    lista = listar_tudo()

    ##exemplo de como fazer update
    #acesso_update = lista[1]
    #acesso_update.setNome("teste12345")
    #atualizar(acesso_update)

    ##exemplo de como remover
    #remover(1)

    ##exemplo de como inserir
    #acesso = Acesso(0, "teste", "123123123", "teste@mail", "LD", "audi", "", str(datetime.date.today().strftime("%m/%d/%Y")), str(datetime.datetime.now().strftime("%H:%M:%S")))
    #inserir(acesso)


    lista = listar_tudo()
    #percorrendo a lista e exibindo o resultado
    for acessos in lista:
        acessos.to_string()

conn.commit()
conn.close()
