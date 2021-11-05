#!/usr/bin/env python
# coding: utf-8

# In[20]:


def funcion():
    nombre_persona = input("nombre: ")
    if(nombre_persona == "Maxi"):
        print("Shalom")
    else:
        print("hola")
funcion()


# In[5]:


def funcion():
    edad = int(input("edad: "))
    if(edad >= 18):
        print("Hola, sos muy viejo")
    else:
        print("This ain't a family friendly channel")
funcion()


# In[ ]:


def funcion():
    edad = int(input("edad:"))
    nombre = input("nombre: ").capitalize()
    if(edad<18):
        print("Tienes que ser mayor")
    elif (nombre == "Carlos"):
        print("Shalom")
    else:
        print("Buenos días")
funcion()
        
    

