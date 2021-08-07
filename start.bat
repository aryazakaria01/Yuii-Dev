@echo off
TITLE Yuii bot
:: Enables virtual env mode and then starts Yuii
env\scripts\activate.bat && py -m tg_bot
