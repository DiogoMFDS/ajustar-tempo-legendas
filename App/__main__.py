from Modules.init import *
from libs.init import *

log = logging.getLogger(__name__)

def main():
    while True:
        log.info("Iniciando o ajuste de legendas...")
        clear_cmd()
        nome_arquivo = str(input("Informe o nome do arquivo ou click enter para ajustar todos os arquivos: "))
        opcao = input("Deseja aumentar ou diminuir o tempo? (A/D): ").strip().upper()
        opcao_tempo = str(input("Deseja ajustar em segundos ou milissegundos? (S/M): ")).strip().upper()
        valor_ajuste = int(input("Informe o valor do ajuste (número inteiro): "))
        
        AjusteLegendas(
            arquivo=nome_arquivo,
            aumentar_segundos=valor_ajuste if opcao == 'A' and opcao_tempo == 'S' else 0,
            diminuir_segundos=valor_ajuste if opcao == 'D' and opcao_tempo == 'S' else 0,
            aumentar_milisegundos=valor_ajuste if opcao == 'A' and opcao_tempo == 'M' else 0,
            diminuir_milisegundos=valor_ajuste if opcao == 'D' and opcao_tempo == 'M' else 0
        )
        sair = input("Deseja sair do programa? (S/N): ").strip().upper()
        if sair == 'S':
            log.info("Encerrando o programa de ajuste de legendas.")
            break


if __name__ == "__main__":
    main()