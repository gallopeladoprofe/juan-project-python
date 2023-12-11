$(async function() {
    // zona segura de ejecucion
    
    try {
        const personas = await axios.get('/get-personas');
        console.log(personas);
        lista_personas = personas.data;
        let cadena = '';
        for(const item of lista_personas) {
            cadena += `
            <tr>
                <th scope="row">${item.id}</th>
                <td>${item.nombres}</td>
                <td>${item.apellidos}</td>
                <td>${item.ci}</td>
                <td></td>
            </tr>
            `;
        }
        $('#tbl tbody').html(cadena);
    } catch (error) {
        console.error(error);
    }

    
    $('#btncrear').on('click', async function(){
        // recuperar los datos del formulario
        const nombres = $('#txtnombres').val();
        const apellidos = $('#txtapellidos').val();
        const ci = $('#txtci').val();
        const direccion = $('#txtdireccion').val();
        
        console.log('nombres = ' + nombres);
        console.log("apellidos = " + apellidos);
        console.log(`cedula ${ci}`);
        console.log(`direccion ${direccion}`);

        if(!nombres.trim()) {
            Swal.fire({
                title: "Error",
                text: "Nombre invalido",
                icon: "error"
            });
            return;
        }
        if(!apellidos.trim()) {
            Swal.fire({
                title: "Error",
                text: "Apellido invalido",
                icon: "error"
            });
            return;
        }
        if(!ci.trim()) {
            Swal.fire({
                title: "Error",
                text: "CI invalido",
                icon: "error"
            });
            return;
        }
        if(!direccion.trim()) {
            Swal.fire({
                title: "Error",
                text: "Direccion invalido",
                icon: "error"
            });
            return;
        }

        // JSON -- Javascript object notation
        const persona = {
            nombres: nombres,
            apellidos: apellidos,
            cedula: ci,
            direccion: direccion
        }
        console.log(persona);

        try {
            const guardado = await axios.post('/save-persona', persona);
            console.log(guardado);
        } catch (error) {
            console.error(error);
        }

        /*
        Swal.fire({
            title: "Exitoso",
            text: "Guardando Formulario",
            icon: "success"
        });
        */
    });
});