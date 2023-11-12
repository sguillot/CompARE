
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import create_files_qLMXB_contours_A
from tk_compare import create_files_qLMXB_pdf
from tk_compare import create_files_qLMXB_contours_C

def main():
    #
    # create contours from author (A) files
    #
    create_files_qLMXB_contours_A( )
    #
    # create pdf from author files
    #
    create_files_qLMXB_pdf( )
    #
    # create contour from pdf
    #
    create_files_qLMXB_contours_C( )

    
if __name__ == "__main__":
    main()
