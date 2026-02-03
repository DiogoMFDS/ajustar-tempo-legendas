@echo off
cd /d "%~dp0"

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao esta instalado ou nao esta no PATH.
    pause
    exit /b 1
)

if not exist "venv\Scripts\activate.bat" (
    echo Criando ambiente virtual...
    python -m venv venv
    if errorlevel 1 (
        echo ERRO: Falha ao criar ambiente virtual.
        pause
        exit /b 1
    )
    echo Ativando ambiente virtual...
    call venv\Scripts\activate.bat
    echo Atualizando pip...
    pip install --upgrade pip
    if errorlevel 1 (
        echo AVISO: Falha ao atualizar pip. Continuando...
    )
    if exist "requirements.txt" (
        echo Instalando dependencias...
        pip install -r requirements.txt
        if errorlevel 1 (
            echo ERRO: Falha ao instalar dependencias.
            pause
            exit /b 1
        )
    ) else (
        echo AVISO: requirements.txt nao encontrado. Pulando instalacao de dependencias.
    )
) else (
    echo Ambiente virtual ja existe. Ativando...
    call venv\Scripts\activate.bat
)

REM Executando o script Python
echo Executando o aplicativo...
python App\__main__.py
if errorlevel 1 (
    echo ERRO: Falha ao executar o script Python.
    call venv\Scripts\deactivate.bat
    pause
    exit /b 1
)

REM Desativando o ambiente virtual
call venv\Scripts\deactivate.bat
echo Aplicativo executado com sucesso.
pause