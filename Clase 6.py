#!/usr/bin/env python
# coding: utf-8

# In[31]:


x=["Hola", "Buenas tardes", "Shalom"]

def funcion(lista):
    j_0= x[0]
    x[0]=x[len(x)-1]
    x[len(x)-1]= j_0
    print(x)
funcion(x)


# In[40]:


x=["Hola", "Buenas tardes", "Shalom"]
def newborn(x,juan,marcelo):
    j_1=x[marcelo-1]
    x[marcelo-1]=x[juan-1]
    x[juan-1]=j_1
    return(x)
newborn(x,3,1)

