from clases.ejercicioa import *

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
                print('Ejercicio B:\n')
                
            elif(cual=='c' or cual=='C'):
                print('Ejercicio C:\n')
            else:
                print('Eso no es una A,B o C.')
        if(seguir=='n' or seguir=='N'):
            acabar=True
        else:
            print('Eso no es una S o una N')

if __name__ == '__main__':
    main()