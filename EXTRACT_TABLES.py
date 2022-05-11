#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tabula

pdf_path="ast_sci_data_tables_sample.pdf"

dfs=tabula.read_pdf(pdf_path,pages='all')

for i in range(len(dfs)):
    dfs[i].to_csv(f"all_pages_table{i}.csv")


# In[ ]:





# In[ ]:




