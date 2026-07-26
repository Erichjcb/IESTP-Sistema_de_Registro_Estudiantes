class Cita:
    def __init__(self,paciente,medico):
        self.paciente=paciente
        self.medico=medico
        
    def mostrar(self):
        print("====CITA MÉDICA====")
        print("Paciente: ", self.paciente.nombre)
        print("Médico: ",self.medico.nombre)
        print("Especialidad: ",self.medico.especialidad)
        