
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import create_files_qLMXB_contours_A
from tk_compare import create_files_qLMXB_pdf
from tk_compare import create_files_qLMXB_contours_C
from tk_compare import create_files_Mass
from tk_compare import create_files_Spin

def main():
    #
    print(50*'-')
    #
    # create contours from author (A) files
    #
    create_files_qLMXB_contours_A( )
    #
    print(50*'-')
    #
    # create pdf from author files
    #
    create_files_qLMXB_pdf( )
    #
    print(50*'-')
    #
    # create contour from pdf
    #
    create_files_qLMXB_contours_C( )
    #
    print(50*'-')
    #
    # create Mass
    #
    create_files_Mass( )
    #
    print(50*'-')
    #
    # create Spin
    #
    create_files_Spin( )
    #
    print(50*'-')

    
if __name__ == "__main__":
    main()
