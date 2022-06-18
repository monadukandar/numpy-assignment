#!/usr/bin/env python
# coding: utf-8

# In[42]:


#1. create a null vector of size 10 but the fifth value which is 1.
import numpy as np
list_array = np.zeros(10)
list_array[4]=1
print(list_array)


# In[43]:


#2.create a vector with values ranging from 10 to 49.
import numpy as np
Range_of_vectors = np.arange(10,49+1)
print("Range_of_vectors:")
print(Range_of_vectors)


# In[44]:


#3. create a 3x3 matrix with values ranging from 0 to 8.
import numpy as np
values = np.arange(0,9).reshape((3,3))
print("3x3 matrix with values ranging from 0 to 8:" , values)


# In[49]:


#4. Find indices of non-zero elements from [1,2,0,0,4,0]
import numpy as np
Array_1 = np.array([1,2,0,0,4,0])

print("Inputing an array : \n", Array_1)

Array_2 = np.nonzero(Array_1)
print("Indicing of non zero elements :", Array_2)


# In[48]:


#5. create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np
random_array = np.random.random((10,10))
print("Original Array:")
print(random_array)
print()
print()
array_min_value = random_array.min()
array_max_value = random_array.max()

print("Minimum Value:",array_min_value)
print("Maximum Value:",array_max_value)


# In[47]:


#6. create a random vector of size 30 and find the mean value.
import numpy as np
size = np.random.random(30)
mean_value = size.mean()
print(mean_value)
    


# In[ ]:




