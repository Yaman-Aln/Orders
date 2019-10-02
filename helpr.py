import pandas as pd
input_url = '/Users/yaman/Downloads/Yaman_Gits/Orders/input/'
output_url = '/Users/yaman/Downloads/Yaman_Gits/Orders/'

#Reads text files and saves into a dataframe
def read_file(input_file):
    list_df = []
    df = pd.read_csv(input_url+input_file)
    
#    for file in input_files:
#        df = pd.read_csv(drive_url+file)
#        list_df.append(df)
        
    return df

#Outputs dataframes into text file, make sure file has .txt extension
def write_new_file(filename):
    f= open(output_url+filename,"w+")    
#    f.write()
    f.close()
    
def write_end_file(file,line):
    f=open(output_url+file, 'a')
    f.write(line)
    f.close()
    

