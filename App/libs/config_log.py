import logging
from datetime import datetime
import os

class ConfigLog:

    def __init__(self, LocalLog:str=r"./logs", level_log: int=logging.DEBUG, name_log : str="app_log"):


        os.makedirs(LocalLog, exist_ok=True)
        data_atual = datetime.now()
        self.nome_caminho = os.path.join(LocalLog, f'{name_log}_{data_atual.strftime("%d_%m_%Y")}.log')
        self.level_log = level_log

    def configurar(self):
        formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(self.nome_caminho, encoding='utf-8')
        file_handler.setFormatter(formato)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formato)

        logger = logging.getLogger()
        logger.setLevel(self.level_log)

        if not logger.handlers:
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
        
        logger.info("Iniciando Execução do Programa")

        return logger