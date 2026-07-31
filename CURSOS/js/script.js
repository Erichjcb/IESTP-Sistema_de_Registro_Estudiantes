// ==========================
// EJECUTAR CUANDO EL HTML ESTÉ LISTO
// ==========================
document.addEventListener("DOMContentLoaded", function(){

    // ==========================
    // CAPTURAR ELEMENTOS HTML
    // ==========================
    const formulario = document.getElementById("formulario");
    const nombres = document.getElementById("nombres");
    const apellidoPaterno = document.getElementById("apellidoPaterno");
    const apellidoMaterno = document.getElementById("apellidoMaterno");
    const edad = document.getElementById("edad");
    const carrera = document.getElementById("carrera");
    const tabla = document.querySelector("#tabla tbody");
    const buscar = document.getElementById("buscar");

    // ==========================
    // ARREGLO DE ESTUDIANTES
    // ==========================
    let estudiantes = [];

    // ==========================
    // EVENTO DEL FORMULARIO
    // ==========================
    formulario.addEventListener("submit", function(event){
        event.preventDefault();

        const estudiante = {
            id: Date.now(),
            nombres: nombres.value,
            apellidoPaterno: apellidoPaterno.value,
            apellidoMaterno: apellidoMaterno.value,
            edad: edad.value,
            carrera: carrera.value
        };

        // Validar campos
        if(
            estudiante.nombres === "" ||
            estudiante.apellidoPaterno === "" ||
            estudiante.apellidoMaterno === "" ||
            estudiante.edad === "" ||
            estudiante.carrera === ""
        ){
            alert("Complete todos los campos.");
            return;
        }

        // Guardar estudiante
        estudiantes.push(estudiante);

        // Guardar en LocalStorage
        guardarDatos();

        // Mostrar en la tabla
        mostrarEstudiantes();

        // Limpiar formulario
        formulario.reset();
    });

    // ==========================
    // MOSTRAR ESTUDIANTES EN LA TABLA
    // ==========================
    function mostrarEstudiantes(){
        tabla.innerHTML = "";

        estudiantes.forEach(function(estudiante){
            tabla.innerHTML += `
                <tr>
                    <td>${estudiante.nombres}</td>
                    <td>${estudiante.apellidoPaterno}</td>
                    <td>${estudiante.apellidoMaterno}</td>
                    <td>${estudiante.edad}</td>
                    <td>${estudiante.carrera}</td>
                    <td>
                        <button onclick="editarEstudiante(${estudiante.id})">Editar</button>
                        <button onclick="eliminarEstudiante(${estudiante.id})">Eliminar</button>
                    </td>
                </tr>
            `;
        });
    }

    // ==========================
    // ELIMINAR ESTUDIANTE
    // ==========================
    window.eliminarEstudiante = function(id){
        estudiantes = estudiantes.filter(function(estudiante){
            return estudiante.id !== id;
        });

        guardarDatos();
        mostrarEstudiantes();
    };

    // ==========================
    // EDITAR ESTUDIANTE
    // ==========================
    window.editarEstudiante = function(id){
        const estudiante = estudiantes.find(function(e){
            return e.id === id;
        });

        nombres.value = estudiante.nombres;
        apellidoPaterno.value = estudiante.apellidoPaterno;
        apellidoMaterno.value = estudiante.apellidoMaterno;
        edad.value = estudiante.edad;
        carrera.value = estudiante.carrera;

        eliminarEstudiante(id);
    };

    // ==========================
    // GUARDAR DATOS EN LOCALSTORAGE
    // ==========================
    function guardarDatos(){
        localStorage.setItem("estudiantes", JSON.stringify(estudiantes));
    }

    // ==========================
    // CARGAR DATOS AL INICIAR
    // ==========================
    const datosGuardados = localStorage.getItem("estudiantes");
    if(datosGuardados){
        estudiantes = JSON.parse(datosGuardados);
        mostrarEstudiantes();
    }

    // ==========================
    // BUSCAR ESTUDIANTES
    // ==========================
    buscar.addEventListener("keyup", function () {
        const texto = buscar.value.toLowerCase();
        const filas = tabla.getElementsByTagName("tr");

        for (let fila of filas) {
            const contenido = fila.textContent.toLowerCase();
            if (contenido.includes(texto)) {
                fila.style.display = "";
            } else {
                fila.style.display = "none";
            }
        }
    });

});
