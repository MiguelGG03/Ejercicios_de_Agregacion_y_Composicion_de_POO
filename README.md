# Ejercicios_de_Agregacion_y_Composicion_de_POO

### Ejercicio a. El día siguiente


El UML de este ejercicio es el siguiente:

![EJERCICIO_A](https://user-images.githubusercontent.com/91721552/160427201-07086803-d3e8-44ad-881c-b65a3f916e94.png)    


### Ejercicio b. ¿Inmortal?


La variable "yang" se destruye al final del programa porque la clase "Yang" tiene el método 
__del__ que se llama a si mismo implicitamente si el "garbage collector" detecta que esta variable
no es usada mas (el garbage collector autoejecuta el método __del__ al final del 
bloque). Para que esto no suceda bastaria con cambiar el método __del__ por el método
 __delete__, el cual no se autoejecuta por el garbage collector.

 El código de el ejercicio que ejecuta antes el método que el signo de interrogación es el
 siguiente:
     
´´´

        class Yin: 
            pass 
        class Yang: 
            def __delete__(self): 
                print("Yang destruido") 


        yin = Yin() 
        yang = Yang() 
        yin.yang = yang 
        print(yang)
        print(yang is yin.yang) 
        yang.__delete__()
        print("?")
´´´


### Ejercicio c. Alternativa a la herencia múltiple
