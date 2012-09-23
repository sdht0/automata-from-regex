Automata From Regular Expressions
================================
Version: 0.5.1
--------------
License: GPLv3
--------------

This is a python program to contruct [e-NFA][1], [DFA][2], and [minimised DFA][3] from a given [regular expression][4], built as a class project for Formal Language and Automata Theory.

It requires the python programming language: Python 2.7 (http://python.org/download/)

To run the programming, simply execute in a command window / terminal:
`python cli.py "(0+1)*+01*0"`

If you get a 'command not found' error in Windows, then probably python is not in your PATH. Check out how to add python to your path here: http://superuser.com/questions/143119/how-to-add-python-to-the-windows-path

Alternately, you can use the GUI built using the Tkinter Library :
`python gui.py`

The program also has the ability to create graphs from the built automata. For that, it requires:
* The GraphViz software to actually create the graphs. Get it from http://www.graphviz.org/Download.php. (This is a ~50MB download, but worth it!)
* The Python Imaging Library (PIL) to read the png images into Tkinter. Get it from http://www.pythonware.com/products/pil/index.htm.

Ubuntu users can install the above two directly by running `sudo apt-get install python-imaging-tk graphviz`

Checkout the included screenshots. The GUI is not the best in the world, but it gets the work done :)

[1]: http://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
[2]: http://en.wikipedia.org/wiki/Deterministic_finite_automaton
[3]: http://en.wikipedia.org/wiki/DFA_minimization
[4]: http://en.wikipedia.org/wiki/Regular_expression
