# NFA-TO-DFA

I/O Example

No. of states : 3
No. of transitions : 2
state name : 0
path : a
Enter end state from state 0 travelling through path a : 
1 2
path : b
Enter end state from state 0 travelling through path b : 

state name : 1
path : a
Enter end state from state 1 travelling through path a : 

path : b
Enter end state from state 1 travelling through path b : 

state name : 2
path : a
Enter end state from state 2 travelling through path a : 
1 2
path : b
Enter end state from state 2 travelling through path b : 
2

NFA :- 

{'0': {'a': ['1', '2'], 'b': []}, '1': {'a': [], 'b': []}, '2': {'a': ['1', '2'], 'b': ['2']}}

Printing NFA table :- 
        a    b
0  [1, 2]   []
1      []   []
2  [1, 2]  [2]
Enter final state of NFA : 
1

DFA :- 

{'0': {'a': '12', 'b': ''}, '12': {'a': '12', 'b': '2'}, '': {}, '2': {'a': '12', 'b': '2'}}

Printing DFA table :- 
      a    b
0    12     
12   12    2
    NaN  NaN
2    12    2

Final states of the DFA are :  ['12']
