#!/usr/bin/env python

import sys
import os
import moviepy
import weedeo.widgets as widgets
from weedeo.nodes import *

from random import random

os.environ['QT_API'] = 'pyside2'  # tells qtpy to use PyQt5
import ryvencore_qt as rc
from qtpy.QtWidgets import QMainWindow, QApplication

        
def main():

    app = QApplication()
    mw = QMainWindow()

    session = rc.Session()
    session.design.set_flow_theme(name='pure light')
    session.register_nodes([PrintNode, RandNode, WeedeoClipNode, WeedeoFileNode, CustomUINode])
    script = session.create_script('hello world', flow_view_size=[800, 500])

    mw.setCentralWidget(session.flow_views[script])

    mw.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
