@echo off

if "%~1" == "" (
	echo usage harpie [-FLAGS] <filename>.a
	exit /b
)

if "%~1" == "-v" (
	echo harpie virtual machine version 0x01
	exit /b
)

py ./src/main.py %*