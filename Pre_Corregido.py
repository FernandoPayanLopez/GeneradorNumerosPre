from rich.table import Table
from rich.console import Console
import statistics

def NI(Semilla_Cuadrada_String, Numero_Interno):
    if(len(Semilla_Cuadrada_String)%2 == 0):
        Numero_Aux = "0" + Semilla_Cuadrada_String
        mid_p = int(len(Numero_Aux)/2)
        mid_nAnterior = Numero_Aux[mid_p-1]
        mid_nMedio = Numero_Aux[mid_p]
        mid_nSiguiente = Numero_Aux[mid_p+1]
        Semilla_Cuadrada_String = mid_nAnterior + mid_nMedio + mid_nSiguiente
        return int(Semilla_Cuadrada_String)
    else:
        Numero_Aux = Semilla_Cuadrada_String
        mid_p = int(len(Numero_Aux)/2)
        mid_nAnterior = Numero_Aux[mid_p-1]
        mid_nMedio = Numero_Aux[mid_p]
        mid_nSiguiente = Numero_Aux[mid_p+1]
        Semilla_Cuadrada_String = mid_nAnterior + mid_nMedio + mid_nSiguiente
        return int(Semilla_Cuadrada_String)
        

def main():
    #Inserción de Datos y Verificación
    Semilla = 000
    Semilla_Cuadrada = 000
    Semilla_Cuadrada_String = 000
    Numero_Interno = 000
    Siguiente_Numero = 000
    NumerosGenerados = []
    Media = 0
    N = 0
    Varianza = 0
    Semilla = input("Ingrese un número de no más de 3 digitos: ")
    if(len(Semilla) > 3):
        print("El numero ingresado es invalido.")
        Semilla = input("Ingrese un número de no más de 3 digitos: ")
    
    
    #Tabla a Generar
    table = Table()
    table.add_column("N", justify="center")
    table.add_column("Semilla")
    table.add_column("Semilla al Cuadro")
    table.add_column("Numero Interno")
    table.add_column("Siguiente numero")

    Siguiente_Numero = Semilla
    x = True
    
    while x:
        Semilla_Int = int(Siguiente_Numero)
        if(N == 0):
            NumerosGenerados.append(Semilla_Int)
            Media = (Media + Semilla_Int)
        Semilla_Cuadrada = Semilla_Int**2
        Semilla_Cuadrada_String = str(Semilla_Cuadrada)
        if(len(Semilla_Cuadrada_String)<3):
            x = False
        else:
            Numero_Interno = NI(Semilla_Cuadrada_String, Numero_Interno)
            Siguiente_Numero = Numero_Interno
            if(Siguiente_Numero in NumerosGenerados or Numero_Interno == 0):
                x = False
            NumerosGenerados.append(Numero_Interno)
            N = N + 1
            Media = (Media + Numero_Interno)
            table.add_row(f"{N}", str(Semilla_Int), str(Semilla_Cuadrada), str(Numero_Interno), str(Siguiente_Numero))
        
        
    N = N + 1
    console = Console()
    console.print(table)
    print("La media de es: " , "{:.2f}".format(Media/N))
    for k in range(N):
        Varianza = (Varianza + ((NumerosGenerados[k] - (Media)/N)**2))  
    print("La varianza poblacional es igual a: ", "{:.2f}".format(Varianza/N))
    if(len(NumerosGenerados)>2): 
        print("La varianza muestral es igual a: ", "{:.2f}".format(statistics.variance(NumerosGenerados)))
        
if __name__ == "__main__":
    main()