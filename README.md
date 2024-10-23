**Stage Manager - tool to auto-generate running-orders for dance shows**

Work in progress; early stages.

As a dancer, I regularly organise productions with my university dance team. For every production, it takes us weeks to work out the optimal running order for the dances. Each team member is in a different subset of the dances, and there are ~3x10^28 possible orders; we need the one which minimises the number of quick costume changes, maximises the contrast in consecutive dance styles, and takes account for other miscellaneous constraints. 

This project aims to automate a solution to this problem, and ultimately integrate the tool into a web-app for dance club management which can be used in my own club once I have left.

So far, the program reduces the problem to a variant of the Travelling Salesman problem, and is looking at was to break down the search space to optimise a solution.
