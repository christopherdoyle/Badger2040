@ECHO OFF

pushd "%~dp0"
CALL ampy --port "COM8" put app/ /
CALL ampy --port "COM8" run .\app\main.py -n
