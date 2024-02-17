import os

from exact_counter import main as ex_main
from aproximate_counter import main as ap_main
from space_saving import main as sp_main
from plot_comparison import main as plots


def main():
    if not os.path.exists("./results"):
        os.mkdir("./results")
        
    if not os.path.exists("./images"):
        os.mkdir("./images")
    
    ex_main()
    ap_main()
    sp_main()
    plots()

if "__main__" == __name__:
    main()