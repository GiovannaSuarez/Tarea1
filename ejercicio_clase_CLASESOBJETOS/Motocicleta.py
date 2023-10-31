class Motocicleta:
    #atributo de clase
    estado="nueva"
    motor=False
    
    #metodos
    def __init__(self,color,matricula,combustible_litros,num_ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso):
        self.color=color
        self.matricula=matricula
        self.combustible_litros=combustible_litros
        self.numero_ruedas=num_ruedas
        self.marca=marca
        self.modelo=modelo
        self.fecha_fabricacion=fecha_fabricacion
        self.velocidad_punta=velocidad_punta
        self.peso=peso

#metodos arrancar y detener 
        
    def arrancar(self):
        if self.motor==False:
            print("El motor ahora está encendido"  )
            self.motor=True
        else:
            print("El motor ya estaba encendido")  
    
    def detener(self):
        if self.motor==True:
            print("El motor se ha detenido")
            self.motor=False    
        else:
            print("El motor ya estaba detenido")     

# forma de consultar el precio desde la clase con un método                    
    
    def precio_desde_metodo (self):
        self.precio=("$ 5.000.000")
        print(f"El precio de la moto es : {self.precio}")  