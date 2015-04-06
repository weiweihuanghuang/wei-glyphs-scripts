# -*- coding: utf-8 -*-
# The function that creates the kerning text, change the Option="lc" to any of the options or, define your own
def kernMaker(kernPair, Option="lc"):
	# If small caps
	if ".sc" in kernPair:
		return u"""/h.sc /o.sc /h.sc {0} /h.sc /o.sc /h.sc  HOH{0} /h.sc /o.sc /h.sc \n/n.sc /o.sc /n.sc {0} /h.sc /h.sc /h.sc  HHH{0} /n.sc /n.sc /n.sc \n/o.sc /o.sc /o.sc {0} /o.sc /o.sc /o.sc  OOO{0} /o.sc /o.sc /o.sc \n/x.sc /h.sc /x.sc {0} /x.sc /h.sc /x.sc  XHX{0} /x.sc /h.sc /x.sc \n""".format(kernPair)
	elif Option == "full":
		return u"""HOH{0} non HOH{0} HOH non{0} npn\nHHH{0} nnn HHH{0} HHH nnn{0} nnn\nOOO{0} ooo OOO{0} OOO ooo{0} ooo\nXHX{0} xhx XHX{0} XHX xox{0} xox\n""".format(kernPair)
	elif Option == "CAPS":
		return u"""HOH{0} HOH\nHHH{0} HHH\nOOO{0} OOO\nXHX{0} XHX\n""".format(kernPair)
	elif Option == "CAPS-sc":
		return u"""HOH{0} /h.sc /o.sc /h.sc \nHHH{0} /h.sc /h.sc /h.sc \nOOO{0} /o.sc /o.sc /o.sc \nXHX{0} /x.sc /h.sc /x.sc \n""".format(kernPair)
	elif Option == "CAPS-lc":
		return u"""HOH{0} non\nHHH{0} nnn\nOOO{0} ooo\nXHX{0} xox\n""".format(kernPair)
	elif Option == "lc":
		return u"""non{0} non nnn{0} nnn ooo{0} ooo xox{0} xox\n""".format(kernPair)
	elif Option == "basic":
		return u"""nn{0} nono{0} oo\n""".format(kernPair)