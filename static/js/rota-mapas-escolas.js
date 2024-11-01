// Script para gerar rota das escolas
    document.getElementById('generateRoute').addEventListener('click', function() {
        const selectedSchools = [];
        const checkboxes = document.querySelectorAll('.school-checkbox:checked');

        checkboxes.forEach(checkbox => {
            selectedSchools.push(checkbox.getAttribute('data-address'));
        });

        const originInput = document.getElementById('origin');
        const origin = originInput.value.trim();

        if (selectedSchools.length > 0 && origin !== '') {
            const destination = selectedSchools[selectedSchools.length - 1];
            const waypoints = selectedSchools.slice(0, -1).join('|');

            const routeUrl = `https://www.google.com/maps/dir/?api=1&origin=${encodeURIComponent(origin)}&destination=${encodeURIComponent(destination)}&waypoints=${encodeURIComponent(waypoints)}`;

            document.getElementById('routeUrl').innerHTML = `<a href="${routeUrl}" target="_blank">Abrir Rota no Google Maps</a>`;
        } else {
            alert('Por favor, selecione pelo menos uma escola e insira o ponto de partida.');
        }
    });

// Script para gerar rota dos alunos
    document.getElementById('generateStudentRoute').addEventListener('click', function() {
        const selectedStudents = [];
        const checkboxes = document.querySelectorAll('.student-checkbox:checked');

        checkboxes.forEach(checkbox => {
            selectedStudents.push(checkbox.getAttribute('data-address'));
        });

        const originInput = document.getElementById('origin');
        const origin = originInput.value.trim();

        if (selectedStudents.length > 0 && origin !== '') {
            const destination = selectedStudents[selectedStudents.length - 1];
            const waypoints = selectedStudents.slice(0, -1).join('|');

            const studentRouteUrl = `https://www.google.com/maps/dir/?api=1&origin=${encodeURIComponent(origin)}&destination=${encodeURIComponent(destination)}&waypoints=${encodeURIComponent(waypoints)}`;

            document.getElementById('studentRouteUrl').innerHTML = `<a href="${studentRouteUrl}" target="_blank">Abrir Rota dos Alunos no Google Maps</a>`;
        } else {
            alert('Por favor, selecione pelo menos um aluno e insira o ponto de partida.');
        }
    });