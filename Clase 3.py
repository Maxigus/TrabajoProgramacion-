{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "d2a8f375",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Santiago tiene 17 anos\n"
     ]
    }
   ],
   "source": [
    "def function(nombre,edad):\n",
    "    nombre_edad= (nombre+ \"tiene \"+ edad+ \"anos\")\n",
    "    print(nombre_edad)\n",
    "function(\"Santiago \", \"17 \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "14f625cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "textojUANCHI\n",
      "juanchi\n"
     ]
    }
   ],
   "source": [
    "def function():\n",
    "    texto= input(\"texto\")\n",
    "    print(texto.lower())\n",
    "function()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "6fdf241b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nombreeifojn\n",
      "¿Cual es tu nombre? eifojn.hola ¿conoces a Juanchi?\n"
     ]
    }
   ],
   "source": [
    "def function(nombre):\n",
    "    quien= input(\"nombre\")\n",
    "    Hola=(\"¿Cual es tu nombre? \" + quien + \".\"+ \"hola \"+ \"¿conoces a \"+ nombre + \"?\")\n",
    "    print(Hola)\n",
    "function(\"Juanchi\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
