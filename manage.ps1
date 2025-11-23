<#
.SYNOPSIS
Script de orquestación para Docker y Alembic en Windows.
#>

param (
    [Parameter(Mandatory=$true)]
    [ValidateSet("start", "stop", "clean", "migration", "shell")]
    [string]$action,

    [string]$m = "cambio_sin_nombre"
)

$ErrorActionPreference = "Stop"

switch ($action) {
    "start" {
        Write-Host "[INICIO] Levantando servicios y construyendo si es necesario..." -ForegroundColor Green
        docker-compose up -d --build
        
        Write-Host "[MIGRACIONES] Ejecutando migraciones pendientes..." -ForegroundColor Cyan
        docker-compose exec web uv run alembic upgrade head
        
        Write-Host "[LISTO] Backend corriendo en http://localhost:8000" -ForegroundColor Green
    }

    "stop" {
        Write-Host "[PAUSA] Pausando servicios..." -ForegroundColor Yellow
        docker-compose stop
    }

    "clean" {
        Write-Host "[LIMPIEZA] Bajando servicios y limpiando redes (Datos persisten)..." -ForegroundColor Red
        docker-compose down
    }

    "migration" {
        Write-Host "[NUEVA MIGRACION] Generando archivo para: $m" -ForegroundColor Cyan
        # Usamos comillas dobles para interpolar la variable $m correctamente
        docker-compose exec web uv run alembic revision --autogenerate -m "$m"
        Write-Host "[EXITO] Archivo de migración creado en /alembic/versions/" -ForegroundColor Green
    }
    
    "shell" {
        Write-Host "[TERMINAL] Entrando al contenedor..." -ForegroundColor Cyan
        docker-compose exec web /bin/bash
    }
}