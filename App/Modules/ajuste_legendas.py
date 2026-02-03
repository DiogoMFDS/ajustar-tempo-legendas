import re
import os
from libs.init import *
from config.cfg import Caminhos

class AjusteLegendas:
    def __init__(self, arquivo:str, diminuir_segundos=0, aumentar_segundos=0, aumentar_milisegundos=0, diminuir_milisegundos=0):
        
        self.diminuir_segundos = diminuir_segundos
        self.aumentar_segundos = aumentar_segundos
        self.aumentar_milisegundos = aumentar_milisegundos
        self.diminuir_milisegundos = diminuir_milisegundos
        self.arquivo = arquivo

        if arquivo:
            log.info(f"Ajustando legenda: {arquivo}")
            self._final()
        if not arquivo:
            arquivos_legendas = os.listdir(Caminhos.legendas_originais)
            for arquivo in arquivos_legendas:
                log.info(f"Ajustando legenda: {arquivo}")
                self.arquivo = arquivo
                self._final()

    def _final(self):
        legenda = self._ler_arquivo(self.arquivo)
        linhas = legenda.splitlines()

        resultado = []
        for linha in linhas:
            if "-->" in linha:
                linha = self._processar_intervalo(linha)
            resultado.append(linha)
        self._salvar_arquivo(self.arquivo, "\n".join(resultado))
        log.info(f"Legenda ajustada e salva: {self.arquivo}")

    def _ajustar_tempo(self,linha):
        """Ajusta o tempo de uma linha no formato HH:MM:SS,mmm."""
        horas, minutos, segundos, milissegundos = map(int, re.split('[:.,]', linha))
        tempo_total = (horas * 3600 + minutos * 60 + segundos - self.diminuir_segundos + self.aumentar_segundos) * 1000 + milissegundos + self.aumentar_milisegundos - self.diminuir_milisegundos
        if tempo_total < 0:
            tempo_total = 0
        horas = tempo_total // 3600000
        minutos = (tempo_total % 3600000) // 60000
        segundos = (tempo_total % 60000) // 1000
        milissegundos = tempo_total % 1000
        return f"{horas:02}:{minutos:02}:{segundos:02},{milissegundos:03}"

    def _processar_intervalo(self, intervalo):
        """Processa a linha de tempo do intervalo."""
        inicio, fim = intervalo.split(' --> ')
        inicio_ajustado = self._ajustar_tempo(inicio)
        fim_ajustado = self._ajustar_tempo(fim)
        return f"{inicio_ajustado} --> {fim_ajustado}"
    
    def _ler_arquivo(self, arquivo:str) -> str:
        """Lê o conteúdo de um arquivo de legenda."""

        caminho_arquivo = f'{Caminhos.legendas_originais}/{arquivo}'
        if not os.path.exists(caminho_arquivo):
            log.error(f"O arquivo {caminho_arquivo} não foi encontrado.")
            raise FileNotFoundError(f"O arquivo {caminho_arquivo} não foi encontrado.")
        
        with open(caminho_arquivo, "r") as arquivo:
            return arquivo.read()

    def _salvar_arquivo(self, arquivo:str, texto_ajustado:str):
        """Salva o conteúdo ajustado em um arquivo."""
        caminho_arquivo = f'{Caminhos.legendas_ajustadas}/{arquivo}'
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto_ajustado)
