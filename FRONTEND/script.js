function mostrarUsuarios() {
    fetch('http://127.0.0.1:5000/api/getUsuarios')
    .then(response => response.json())
    .then(data => {
        const cuerpoTabla = document.getElementById('cuerpo-tabla-usuarios');
        cuerpoTabla.innerHTML = ''; // Limpiar la tabla antes de agregar nuevos datos

        data.forEach(usuario => {
            const fila = document.createElement('tr');
            
            // Crear celdas para número de socio y nombre
            const numeroSocio = document.createElement('td');
            numeroSocio.textContent = usuario[0];
            const nombre = document.createElement('td');
            nombre.textContent = usuario[1];

            // Agregar las celdas a la fila
            fila.appendChild(numeroSocio);
            fila.appendChild(nombre);

            // Agregar la fila a la tabla
            cuerpoTabla.appendChild(fila);
        });
    })
    .catch(error => console.error('Error al obtener usuarios:', error));
}
