#!/usr/bin/python

import json
import math
import os

import yaml
from lxml import etree

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import wavedrompy as wavedrom

# ---------------------------------------------
# noinspection PyUnboundLocalVariable,PyDefaultArgument,PyAttributeOutsideInit
class TimingDiagram(inkBase.inkscapeMadeEasy):
    def __init__(self):
        inkBase.inkscapeMadeEasy.__init__(self)

        self.arg_parser.add_argument("--tab", type=str, dest="tab", default="signals")

        self.arg_parser.add_argument("--signalString", type=str, dest="signalString", default='{ "assign":[  ["out", ["~", "a"]  ]]}')
        self.arg_parser.add_argument("--filePath", type=str, dest="filePath", default='')

    def effect(self):

        so = self.options
        so.tab = so.tab.replace('"', '')  # removes de exceding double quotes from the string

        root_layer = self.document.getroot()

        # sets the position to the viewport center, round to next 10.
        position = [self.svg.namedview.center[0], self.svg.namedview.center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10

        # load data
        if os.path.isfile(so.filePath):
            with open(so.filePath, 'r') as file:
                inputString = file.read()
        else:
            inputString = so.signalString

        # fix quotes, necessary for wavedrompy (Json)
        cleanedWaveString = self.fixQuotes(inputString)

        #self.displayMsg(cleanedWaveString)

        # craete diagram svg
        svgObj = wavedrom.render(source=cleanedWaveString, output=[])
        # svgObj.saveas('/home/fernando/temporary.svg')

        # converts to lxml etree for cleanup
        svg = etree.fromstring(svgObj.tostring())

        # removes unitary squares at the origin that seems useless and cause problems
        if True:
            for elem in svg.iter():
                # removes namespace
                elemTag = etree.QName(elem).localname
                if elemTag == 'rect':
                    if elem.attrib['x'] == '0' and elem.attrib['y'] == '0' and elem.attrib['height'] == '1' and elem.attrib['width'] == '1':
                        elem.getparent().remove(elem)

        # remove title elements
        if True:
            for elem in svg.iter():
                # removes namespace
                elemTag = etree.QName(elem).localname
                if elemTag == 'title':
                    elem.getparent().remove(elem)

        #add to inkscape document
        diagramGroup = self.createGroup(root_layer, label='importedSVG')
        for elem in svg:
            diagramGroup.append(elem)

        center = self.getCenter(diagramGroup)
        self.moveElement(diagramGroup, position - center)

        self.addAttribute(diagramGroup, 'WavedromString', cleanedWaveString, forceWrite=True)

    def fixQuotes(self, inputString):
        # fix double quotes in the input file. opening with yaml and dumping with json fix the issues.
        yamlCode = yaml.load(inputString, Loader=yaml.FullLoader)
        string = json.dumps(yamlCode, indent=4)
        return string

if __name__ == '__main__':

    debugMode = False
    sp = TimingDiagram()

    if debugMode:
        tempFile='/home/fernando/temp_debugA.svg'
        sp.createEmptySVG(tempFile)

        # sp.run([r'--signalString={ "assign":[  ["out", ["~", "a"]  ]]}',r'/home/fernando/lixo.svg'], output=os.devnull)
        sp.run([r'--filePath=/home/fernando/diagram_01.txt', tempFile], output=os.devnull)
        sp.document.write('/home/fernando/temp_debug_out.svg')

    else:
        sp.run()
