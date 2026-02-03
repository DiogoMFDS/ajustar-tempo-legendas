import logging
import os


from libs.config_log import ConfigLog


config_log = ConfigLog()
log = config_log.configurar()
def clear_cmd():
    os.system('cls' if os.name == 'nt' else 'clear')