# wavedromScape

Wavedrom's digital timing diagram extension for [Inkscape](https://inkscape.org/).

**This is a work-in-progress project. The current state is BUGGY!  =)**


<img src="docs/images/Example_01.png" width="700px"/>

<img src="docs/images/Example_02.png" width="700px"/>

References:

[WaveDrom](https://wavedrom.com/)



<img src="docs/images/Examples.png" width="900px"/>

## main features

The main features of this extension are

 - You can create wavedrom digital timing diagram using Inkscape

## Current version

Compatibility table

|  Inkscape        |  wavedromScape  | inkscapeMadeEasy | Receive updates?|
|------------------|-----------------|------------------|-----------------|
|       1.0        |  1.0 (latest)   |   1.0 (latest)   | YES             |
| 0.48, 0.91, 0.92 |   NO SUPPORT    |  0.9x (obsolete) | NO              |


**Latest version:** The latest version of **wavedromScape** is **1.0**. This version is compatible with Inkscape 1.0 and up only. It is **incompatible** with older Inkscape versions! There is no goal to develop wavedromScape for Inkscape <1.0.

# Installation and requirements

## Requirements

- You will need [inkscapeMadeEasy](https://github.com/fsmMLK/inkscapeMadeEasy) plugin installed. Check the compatibility table above to know the version you need.
- You will need [wavedrom python module](https://github.com/wallento/wavedrompy). You can easily install it using pip: ``pip install wavedrom``

## Installation procedure

**wavedromScape** was developed using Inkscape 1.0 in Linux (Kubuntu 18.04). It should work in different OSs too as long as all requirements are met.

1. Install [inkscapeMadeEasy](https://github.com/fsmMLK/inkscapeMadeEasy), **version 1.0** (latest). Follow the instructions in the manual page. **Note:** No LaTeX text is used in **wavedromScape**, so there is no reason to install LaTeX support if you don't have any other extensions that employ inkscapeMadeEasy. However, you must follow the instructions and disable LaTeX support since it is enabled by default. See inkscapeMadeEasy's documetation pages.

2. **wavedromScape** installation

    1. Go to Inkscape's extension directory with a file browser. Your inkscape extension directory can be accessed by opening Inkscape and selecting ``Edit > Preferences > System``. Look for the item **User Extensions**  field. There is a button on the right of the field  that will open a file explorer window in that specific folder.

    2. Create a subfolder in the extension directory with the name ``wavedromScape``. **Important:**  Be careful with upper and lower case letters. You must write as presented above.

    3. Download **wavedromScape** files and place them inside the directory you just created.

       You don't have to copy all files from Github. The files you will need are inside the ``latest`` folder. In the end you must have the following files and directories in your Inkscape extension directory.

       **LaTeX users:** the file `wavedromScapePreamble.tex` contains the macros defined in this plugin. You can add your own macros to this file. You can also add macros to ``inkscapeMadeEasy/basicLatexPackages.tex``. In this case the same macros will be accessible by all plugins that employ inkscapeMadeEasy.

        ```
        inkscape
         ┣━━extensions
         ┋   ┣━━ inkscapeMadeEasy      <-- inkscapeMadeEasy folder
             ┃    ┣━━ inkscapeMadeEasy_Base.py
             ┃    ┣━━ inkscapeMadeEasy_Draw.py
             ┃    ┣━━ inkscapeMadeEasy_Plot.py
             ┃    ┗━━ basicLatexPackages.tex
             ┃
             ┣━━ textext               <-- texText folder (if you installed textText)
             ┃    ┋
             ┃
             ┣━━ wavedromScape        <-- wavedromScape folder
             ┋    ┣━━ wavedromScape.inx
                  ┗━━ wavedromScape.py
        
        NOTE: You might have other sub folders inside the extensions directory. They don't interfere with the plugin.
        ```

# Usage

The extension can be found under `extensions > fsmMLK > Circuit symbols` menu.

This extension is presented in one tab that allows you write the string that specifies the diagram

# Examples

Check tutorials [here](https://wavedrom.com/tutorial.html), [here](https://wavedrom.com/tutorial2.html), and 


```
{ "signal": [
 { "name": "CK",   "wave": "P.......",                                              "period": 2  },
 { "name": "CMD",  "wave": "x.3x=x4x=x=x=x=x", "data": "RAS NOP CAS NOP NOP NOP NOP", "phase": 0.5 },
 { "name": "ADDR", "wave": "x.=x..=x........", "data": "ROW COL",                     "phase": 0.5 },
 { "name": "DQS",  "wave": "z.......0.1010z." },
 { "name": "DQ",   "wave": "z.........5555z.", "data": "D0 D1 D2 D3" }
]}
```
<img src="docs/images/Example_01.png" width="700px"/>


```
{ "signal": [
  { "name": "pclk", "wave": "p......." },
  { "name": "Pclk", "wave": "P......." },
  { "name": "nclk", "wave": "n......." },
  { "name": "Nclk", "wave": "N......." },
  {},
  { "name": "clk0", "wave": "phnlPHNL" },
  { "name": "clk1", "wave": "xhlhLHl." },
  { "name": "clk2", "wave": "hpHplnLn" },
  { "name": "clk3", "wave": "nhNhplPl" },
  { "name": "clk4", "wave": "xlh.L.Hx" }
]}
```
<img src="docs/images/Example_02.png" width="700px"/>