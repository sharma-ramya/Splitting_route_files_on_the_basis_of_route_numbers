#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
This program takes an iput route file with the following data:
route_no, stop_seq, bus_stop_cd, bus_stop_nm, km, latitude, longitude
and converts it into multiple csv files, one for each route based on route number
"""


import pandas as pd


# In[8]:


#please specify input file here
input_file = '~/Documents/Miland_Sohni_transportation/Data/New_Shahpur_data/ETIM data/6dec/pgrouting_latlong_corrected_all_route_data_with_bus_stops_6dec1.csv.csv'

#output location
output_loc = "~/Documents/Miland_Sohni_transportation/Data/New_Shahpur_data/ETIM data/6dec/pgrouting_sample_routes/pgrouting_route"


# In[10]:


"""
read the route data containing all the route details, i.e.:
route_no, stop_seq, bus_stop_cd, bus_stop_nm, km, latitude, longitude
"""
read_data = pd.read_csv(input_file, delimiter = ',')


# In[11]:


read_data.iloc[[2]]


# In[5]:


#sample output file
sample_output_file = output_loc + str(read_data.iloc[0,0]) + ".csv"

print(sample_output_file)


# In[12]:


for i in read_data.index:
    
    #add the first stop to the data
    if (read_data.iloc[i,1] == 1):
        
        #To cover the first case, i.e. i is 0 and there is nodata before it to save in a file
        if (i > 0):            
            output_df.to_csv(output_file, encoding='utf-8', index=False)
            print ("Data written to ", output_file)
            
        output_file = output_loc + str(read_data.iloc[i,0]) + ".csv"
        output_df = pd.DataFrame()
    
    output_df = output_df.append(read_data.iloc[[i]])
    
#For the last file:
output_df.to_csv(output_file, encoding='utf-8', index=False)
print ("Data written to ", output_file)
        
    


# In[ ]:





# In[ ]:




