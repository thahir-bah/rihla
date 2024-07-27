import subprocess

with open('requirements.txt', 'r', encoding='utf-16') as file:
    for line in file:
        package = line.split('==')[0].strip()
        subprocess.run(['pip', 'uninstall', '-y', package], shell=True)