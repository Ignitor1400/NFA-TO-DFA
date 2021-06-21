import pandas as pd

# Taking NFA input from User 

nfa = {}                                 
n = int(input("No. of states : "))            
t = int(input("No. of transitions : "))       
for i in range(n):  
    state = input("state name : ")            
    nfa[state] = {}                           #Creating a nested dictionary
    for j in range(t):
        path = input("path : ")               #Enter path eg : a or b in {a,b} 0 or 1 in {0,1}
        print("Enter end state from state {} travelling through path {} : ".format(state,path))
        reaching_state = [x for x in input().split()]  
        nfa[state][path] = reaching_state     

print("\nNFA :- \n")
print(nfa)                                    #Printing NFA
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter final state of NFA : ")
nfa_final_state = [x for x in input().split()]      # Enter final state/states of NFA
###################################################                 
    
new_states_list = []                         
dfa = {}                                      
keys_list = list(list(nfa.keys())[0])                  
path_list = list(nfa[keys_list[0]].keys())    #list of all the paths eg: [a,b] or [0,1]

###################################################

# Computing first row of DFA transition table

dfa[keys_list[0]] = {}                         
for y in range(t):
    var = "".join(nfa[keys_list[0]][path_list[y]])  
    dfa[keys_list[0]][path_list[y]] = var            
    if var not in keys_list:                        
        new_states_list.append(var)                  
        keys_list.append(var)                        
        
###################################################
 
# Computing the other rows of DFA transition table

while len(new_states_list) != 0:                    
    dfa[new_states_list[0]] = {}                     
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []                               
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]] 
            s = ""
            s = s.join(temp)                         
            if s not in keys_list:                   
                new_states_list.append(s)           
                keys_list.append(s)                  
            dfa[new_states_list[0]][path_list[i]] = s   
        
    new_states_list.remove(new_states_list[0])      

print("\nDFA :- \n")    
print(dfa)                                          
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break
        
print("\nFinal states of the DFA are : ",dfa_final_states)       #Printing Final states of DFA
