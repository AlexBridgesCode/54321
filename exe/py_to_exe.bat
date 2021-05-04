cd "C:\Users\alexb\Documents\Programming\Python\54321\scripts\"
pyinstaller --onefile --icon="C:\Users\alexb\Documents\Programming\Python\54321\icon\icon.ico" 54321.py
move "C:\Users\alexb\Documents\Programming\Python\54321\scripts\dist\54321.exe" "C:\Users\alexb\Documents\Programming\Python\54321\exe\"
cd "C:\Users\alexb\Documents\Programming\Python\54321\scripts"
rmdir /s /q "__pycache__"
rmdir /s /q "build"
rmdir /s /q "dist"
del /s "54321.spec"