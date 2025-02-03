from classes_command.emprestimo_command import EmprestimoCommand
from classes_command.reserva_command import ReservaCommand

class Console:
    def __init__(self):
        self.comandos = {
            "emp": EmprestimoCommand(),
            "res": ReservaCommand()
        }
    
    def iniciar(self):
            while True:
                entrada = input("Digite um comando válido ou 'sai' para sair\n").split()
                
                if entrada[0] == "sai":
                    print("Encerrando o sistema...")
                    break
                
                elif entrada[0] not in self.comandos:
                    print("Comando inválido!")
                
                else:
                    cur = entrada[0]

                    self.comandos[cur].executar(*entrada[1:]) # o * é pra desempacotar os argumentos recebidos na entrada



if __name__ == "__main__":
     
    console = Console()
    
    console.iniciar()