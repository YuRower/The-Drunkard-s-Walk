# Stochastic Processes, Random Walks, & Markov Chains
The program that simulates state-transitions and displays the number of stays in non-absorbing states
## Execution Details
Start of transition modeling - 2000 times
Absorbing states - P,K.
Non-absorbing states 1, 2, 3 and their probability of transitions i,j,k , respectively.
If a drunkard is in an absorbing state, then the completion of the transitions and printing the results of execution.
```Python
while ((not (self.field[position].NameState==("P"))) and (not (self.field[position].NameState==("K")))):
                 self.walk()
                 moves+=1
return moves
}
#...
#...
#...
print("Time of total number of state in non-absorbing state from position " + str(num) + " = " + str(distance /numTrials) )
```
