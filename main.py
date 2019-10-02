#import libraries and modules
import pandas as pd 
import helpr
import tree_analysis 

#Assumptions: 
#1) workorders can only be dependent on later workorders (helps when making new trees))
#2) Can be dependent on no more than 2 workorders (binary trees)

#Requires Attention:
#The secondary binary tree "new_tree" is currently poorly integrated for one time use of id/dep use.

#Requires improvement:
#Currently there is a redundant use of the find method in the tree_analysis module.
#Inefficient, would slightly play with structure of code if I went back to this.
 
def init_orders():
    
    id_depend = []
    helpr.write_new_file("output.txt")
    merged_file = helpr.read_file('dependencies.txt')
    #Sorting to keep assumption that workorders can only be dependent on later workorders, pragmatism > inefficiency of having to use sort here for now.
    #Python's sorted() uses timsort, so unnecessary to write an alternate algorithm ie merge_sort.
    #Note: It is a stable sort, so any items that have the same sort 'value', are kept in the order they were in before sorting.
    ordered_file= merged_file.sort_values(by=['id'])

    for row in merged_file.itertuples():
        id_depend.append([row.id, row.dependency_id])

    #Instantiate tree
    binary_orders = tree_analysis.Tree()
    
    #Populate tree
    for pair in id_depend:
        id, depend = pair[0], pair[1]
        binary_orders.insert(id,depend)
        #In case *a* secondary tree is required for *one* time use
        if binary_orders.insert(id,depend) is not None:
            new_tree = binary_orders.insert(id,depend)
 
    binary_orders.depth_tree_order()
    
    new_tree.depth_tree_order()
    
    
init_orders()