from AutomataTheory import *

def main():
    inp = "(01*1)*1"
    print inp
    nfaObj = NFAfromRegex(inp)
    nfa = nfaObj.getNFA()
    dfaObj = DFAfromNFA(nfa)
    dfa = dfaObj.getDFA()
    minDFA = dfaObj.getMinimisedDFA()
    drawGraph(dfa, "dfa")
    drawGraph(nfa, "nfa")
    drawGraph(minDFA, "mdfa")
    nfaObj.displayNFA()
    dfaObj.displayDFA()
    dfaObj.displayMinimisedDFA()
    # print nfa.language
    # print dfa.language
    # print minDFA.language
    # x = BuildAutomata.basicstruct("0")
    # # x.addtransition(1,2,'1')
    # y = BuildAutomata.basicstruct("1")
    # u3 = BuildAutomata.plusstruct(x,y)      # 0+1
    # u4 = BuildAutomata.starstruct(u3)     # (0+1)*
    # u5 = BuildAutomata.dotstruct(u4,y)    # (0+1)*1
    # u6 = BuildAutomata.dotstruct(u5,u3)   # (0+1)*1(0+1)
    # u7 = BuildAutomata.dotstruct(u6,u3)   # (0+1)*1(0+1)(0+1)
    # u8 = BuildAutomata.plusstruct(u6,u7)  # (0+1)*1(0+1)+(0+1)*1(0+1)(0+1)
    # u3.printautomata()
    # # print u4.automata()
    # # print u5.automata()
    # # print u6.automata()
    # # u7.automata()
    # dfa = buildDFA(u8)
    # # dfa.printautomata()
    # for s in ['01000', '110', '011', '111', '0100', '0101', '0110', '0111']:
    #     print s, acceptsstring(dfa, s)
    # # u8 = BuildAutomata.plusstruct(u6,u7)
    # d = Automata()
    # d.addtransition(1,2,"0")
    # d.addtransition(1,3,"1")
    # d.addtransition(2,4,"0")
    # d.addtransition(2,5,"1")
    # d.addtransition(3,7,"1")
    # d.addtransition(3,6,"0")
    # d.addtransition(4,4,"0")
    # d.addtransition(4,5,"1")
    # d.addtransition(5,6,"0")
    # d.addtransition(5,7,"1")
    # d.addtransition(6,4,"0")
    # d.addtransition(6,5,"1")
    # d.addtransition(7,7,"1")
    # d.addtransition(7,6,"0")
    # d.setstartstate(1)
    # d.addfinalstates([4, 6,7])
    # d.printautomata()
    # drawGraph(d,"dfa")
    # x = TransformNFA(d)
    # x.dfa = d
    # m = x.minimiseDFA()
    # m.printautomata()
    # drawGraph(m,"mdfa")
    # # print d.automata()
    # # print buildDFA(d).automata()
    # # p = BuildAutomata.dotstruct(x,y)
    # # q = BuildAutomata.plusstruct(x,y)
    # # r = BuildAutomata.starstruct(x)
    # # s = BuildAutomata.plusstruct(p,q)
    # # print q.automata()
    # # allstates = {1:[1,2,3],2:[2,3]}
    # # print [k for k, v in allstates.iteritems() if v  ==  [1,2,3]]
    # # print s.automata()
    # # print buildDFA(u5).automata()
    # # print y.automata()
    # # print p.automata()
    # # print q.automata()
    # # print r.automata()

if __name__  ==  '__main__':
    t = time.time()
    try:
        main()
    except BaseException as e:
        print "Failure:", e
    print time.time() - t, "seconds"