import os
import subprocess
from time import sleep


class Axioma:

    cmd = 'WMIC PROCESS get Caption,Commandline,Processid'

    @staticmethod
    def start(name_app='AxiOMACtrlApplication.exe', name_opc='AxOpcServerWin.exe'):
        proc = subprocess.Popen(Axioma.cmd, shell=True, stdout=subprocess.PIPE)
        for proc_line in proc.stdout:
            if name_app in str(proc_line):
                app_run = True
            if name_opc in str(proc_line):
                opc_run = True
        if app_run:
            print(f"{name_app} already run")
        else:
            os.startfile(r'C:\NCSystems\АксиОМА Контрол x64\AxiOMACtrlApplication.exe')
            print(f"{name_opc} will be run")
        if opc_run:
            print(f"{name_opc} already run")
        else:
            if name_app:
                sleep(5)
                os.startfile(r'C:\NCSystems\АксиОМА Контрол x64\AxOpcServerWin.exe')
                print(f"{name_opc} will be run")
            else:
                print(f"Before need run {name_app}")

    @staticmethod
    def get_process():
        proc = subprocess.Popen(Axioma.cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            print(line)



