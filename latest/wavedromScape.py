#!/usr/bin/python

import math
import os
import sys

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw

# pip install wavedrom
import wavedrom
import tempfile

# ---------------------------------------------
# noinspection PyUnboundLocalVariable,PyDefaultArgument,PyAttributeOutsideInit
class TimingDiagram(inkBase.inkscapeMadeEasy):
    def __init__(self):
        inkBase.inkscapeMadeEasy.__init__(self)

        self.arg_parser.add_argument("--tab", type=str, dest="tab", default="signals")

        self.arg_parser.add_argument("--signalString", type=str, dest="signalString", default='123')

    def effect(self):

        so = self.options
        so.tab = so.tab.replace('"', '')  # removes de exceding double quotes from the string

        root_layer = self.document.getroot()

        # sets the position to the viewport center, round to next 10.
        position = [self.svg.namedview.center[0], self.svg.namedview.center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10

        #removes \n \r characters
        cleanedWaveString = ' '.join(so.signalString.replace(r'\n','').replace(r'\r','').split())

        #craete diagram
        svgObj = wavedrom.render(source=cleanedWaveString,output=[])

        # create temp svg file and export diagram
        tmpf = tempfile.NamedTemporaryFile(mode='w', prefix='tempDiagram_', suffix='.svg', delete=False)
        tempFilePath = tmpf.name
        tmpf.close()
        svgObj.saveas(tempFilePath)

        print(tempFilePath)
        #import SVG
        diagramGroup = self.importSVG(root_layer,tempFilePath, createGroup=True, position=position, scaleFactor=1.0, unifyDefs=True)

        #add config
        self.addAttribute( diagramGroup, 'WavedromString', cleanedWaveString,forceWrite=True)

        #remove temp file
        os.remove(tempFilePath)

if __name__ == '__main__':

    debugMode = False
    sp = TimingDiagram()

    if debugMode:
        sp.run([r'--signalString={ "signal": [{ "name": "a1", "wave": "01.zx=ud.23.456789" }] }',r'/home/fernando/lixo.svg'], output=os.devnull)

        #save the result
        sp.document.write('/home/fernando/out.svg')

    else:
        sp.run()
