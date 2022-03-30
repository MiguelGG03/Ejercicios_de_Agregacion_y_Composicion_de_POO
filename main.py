from clases.ejercicioa import *
from clases.ejerciciob import *
from clases.ejercicioc import *

def main():
    acabar=False
    while(acabar==False):
        seguir=str(input('Quieres seguir viendo ejercicios(S/N)?:'))    
        if(seguir=='s' or seguir=='S'):
            cual=str(input('Que ejercicio quieres ver (A,B,C)?:'))
            if(cual=='a' or cual=='A'):
                print('Ejercicio A:\n\n')
                
                ny=NuevaYork()
                del ny
                
            elif(cual=='b' or cual=='B'):
                print('Ejercicio B:\n\n')
               
                yin = Yin() 
                yang = Yang() 
                yin.yang = yang 
                print(yang)
                print(yang is yin.yang) 
                yang.__delete__()
                print("?")
                
            elif(cual=='c' or cual=='C'):
                print('Ejercicio C:\n\n')
                
                ventanas =[]
                # Instanciación de las paredes 
                pared_norte = Pared("NORTE") 
                pared_oeste = Pared("OESTE") 
                pared_sur = Pared("SUR") 
                pared_este = Pared("ESTE") 
                # Instanciación de las ventanas 
                ventana_norte = Ventana(pared_norte, 0.5) 
                ventana_oeste = Ventana(pared_oeste, 1) 
                ventana_sur = Ventana(pared_sur, 2) 
                ventana_este = Ventana(pared_este, 1) 
                # Instanciación de la casa con las 4 paredes 
                casa = Casa([ventana_norte, ventana_oeste, ventana_sur, ventana_este]) 
                print(casa.superficie_acristalada()) 

            else:
                print('Eso no es una A,B o C.')
        if(seguir=='n' or seguir=='N'):
            acabar=True
        else:
            print('Eso no es una S o una N')

if __name__ == '__main__':
    main()