#! /usr/bin/python3
from os import system, name
import sys

_B = "[1m"
_N = "[22m"
_D = "[2m"
_RSTALL = "[0m"
_f_w = "[37m"
_f_y = "[33m"
_f_b = "[34m"
_f_bl = "[30m"
_f_r = "[31m"
_f_c = "[36m"
_f_g = "[32m"
_f_m = "[35m"


_f_ex_w = "[97m"
_f_ex_y = "[93m"
_f_ex_b = "[94m"
_f_ex_bl = "[90m"
_f_ex_r = "[91m"
_f_ex_c = "[96m"
_f_ex_g = "[92m"
_f_ex_m = "[95m"


def logo():
    _m_cl = _f_ex_b
    _b_cl = _f_y
    print("")
    print(f"{_m_cl}╔═══╗╔╗╔╗{_b_cl}───────{_m_cl}╔═══╗{_b_cl}───{_m_cl}╔═╦╗{_b_cl}───{_m_cl}╔══╗  {_RSTALL}")
    print(f"{_m_cl}║╔═╗╠╝╚╣║{_b_cl}───────{_m_cl}║╔═╗║{_b_cl}───{_m_cl}║╔╝╚╗{_b_cl}──{_m_cl}╚╣╠╝  {_RSTALL}")
    print(f"{_m_cl}║║{_b_cl}─{_m_cl}║╠╗╔╣║╔══╦══╗║╚══╦══╦╝╚╗╔╝{_b_cl}───{_m_cl}║║╔═╗{_RSTALL}")
    print(f"{_m_cl}║╚═╝║║║║║║╔╗║══╣╚══╗║╔╗╠╗╔╣║{_b_cl}────{_m_cl}║║║╔╝{_RSTALL}")
    print(f"{_m_cl}║╔═╗║║╚╣╚╣╔╗╠══║║╚═╝║╚╝║║║║╚╗╔╗╔╣╠╣║ {_RSTALL}")
    print(f"{_m_cl}╚╝{_b_cl}─{_m_cl}╚╝╚═╩═╩╝╚╩══╝╚═══╩══╝╚╝╚═╝╚╝╚══╩╝ {_RSTALL}")


def Fncls():
    if name == 'nt':
        _ = system('cls')
        print("ted")    
    else:
        _ = system('clear')



if __name__ == '__main__':            
    
    if len(sys.argv) == 1:
        Fncls()
        print("")
        logo()