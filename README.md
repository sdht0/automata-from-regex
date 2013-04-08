Automata From Regular Expressions
=================================

Overview and Usage
------------------
This is a python program to contruct [e-NFA][1], [DFA][2], and [minimised DFA][3] from a given [regular expression][4], built as a class project for Formal Language and Automata Theory.

It requires the python programming language: Python 2.7 (http://python.org/download/)

The program can be run by passing the regex as a command line argument: `python cli.py "(0+1)*+01*0"`

Alternately, you can use the GUI built using the Tkinter Library: `python gui.py`

You may get a 'command not found' error in Windows, which means python is not in your PATH. Check out how to add python to your path here: http://superuser.com/questions/143119/how-to-add-python-to-the-windows-path

The program also has the ability to create graphs from the built automata. For that, it requires:
* The GraphViz software to actually create the graphs. Get it from http://www.graphviz.org/Download.php. (This is a ~50MB download, but worth it!)
* The Python Imaging Library (PIL) to read the png images into Tkinter. Get it from http://www.pythonware.com/products/pil/index.htm.

Ubuntu users can install them by running `sudo apt-get install python-imaging-tk graphviz`

Checkout the included screenshots. The GUI is not the best in the world, but it gets the work done :)

Acknowledgements
----------------
* Prof S.K. Saha, for the project idea and concepts of Automata Theory
* https://github.com/max99x/automata-editor, for general ideas and esp. for showing how to use GraphViz
* The wonderful community over at http://stackoverflow.com, for helping get past all bottlenecks
* The very helpful documentation of Tkinter at http://effbot.org/tkinterbook/

[1]: http://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
[2]: http://en.wikipedia.org/wiki/Deterministic_finite_automaton
[3]: http://en.wikipedia.org/wiki/DFA_minimization
[4]: http://en.wikipedia.org/wiki/Regular_expression

License
-------
GNU GPLv3
