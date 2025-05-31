import pytest
import os
import sys
from pathlib import Path

sys.path.append(r'D:\ECE\multisim\NI Multisim Offline Installation\ceaser_cypher\ceaser_cypher')
from word import word_encrpyt
import unittest

def encyrpt_and_release():
        word_encrpyt()
        file_path="my_python_encrypt.docx"
        
        assert os.path.exists(file_path)==false
       



if __name__=="__main__":
    pytest.main()