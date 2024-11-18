@echo off
cd C:\Projetos\api_python
call venv\Scripts\activate
uvicorn main:app --reload
