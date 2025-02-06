from classes_command.emprestimo_command import EmprestimoCommand
from classes_command.reserva_command import ReservaCommand
from classes_command.devolucao_command import DevolucaoCommand
from classes_command.consulta_command import ConsultaCommand

class Console:
    def __init__(self):
        self.comandos = {
            "emp": EmprestimoCommand(),
            "res": ReservaCommand(),
            "dev": DevolucaoCommand(),
            "usu": ConsultaCommand(),
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