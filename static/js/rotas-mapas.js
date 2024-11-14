/* // -------------- ENDEREÇO DO ALUNO --------------------
document.getElementById('generateRoute').addEventListener('click', function() {
    // Captura os endereços selecionados
    const selectedAddresses = [];
    const checkboxes = document.querySelectorAll('.student-checkbox:checked');

    checkboxes.forEach(checkbox => {
        selectedAddresses.push(checkbox.getAttribute('data-address'));
    });

    // Obtém o ponto de partida do campo de entrada
    const originInput = document.getElementById('origin');
    const origin = originInput.value.trim();

    // Gera a URL da rota
    if (selectedAddresses.length > 0 && origin !== '') {
        const destination = selectedAddresses[selectedAddresses.length - 1]; // Último endereço selecionado como destino
        const waypoints = selectedAddresses.slice(0, -1).join('|'); // Todos os endereços exceto o último como waypoints

        const routeUrl = `https://www.google.com/maps/dir/?api=1&origin=${encodeURIComponent(origin)}&destination=${encodeURIComponent(destination)}&waypoints=${encodeURIComponent(waypoints)}`;

        // Exibe a URL gerada
        document.getElementById('routeUrl').innerHTML = `<a href="${routeUrl}" target="_blank">Abrir Rota no Google Maps</a>`;
    } else {
        alert('Por favor, selecione pelo menos um aluno e insira o ponto de partida.');
    }
});

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
}); */

document.getElementById('generateRoute').addEventListener('click', function() {
    const selectedSchools = [];
    const selectedStudents = [];
    
    // Coletar endereços das escolas selecionadas
    const schoolCheckboxes = document.querySelectorAll('.school-checkbox:checked');
    schoolCheckboxes.forEach(checkbox => {
        selectedSchools.push(checkbox.getAttribute('data-address'));
    });

    // Coletar endereços dos alunos selecionados
    const studentCheckboxes = document.querySelectorAll('.student-checkbox:checked');
    studentCheckboxes.forEach(checkbox => {
        selectedStudents.push(checkbox.getAttribute('data-address'));
    });

    const originInput = document.getElementById('origin');
    const origin = originInput.value.trim();

    // Verifica se há escolas ou alunos selecionados
    if ((selectedSchools.length > 0 || selectedStudents.length > 0) && origin !== '') {
        // Combina as escolas e alunos em um único array
        const allSelectedAddresses = [...selectedSchools, ...selectedStudents];
        
        // Define o destino como o último endereço selecionado
        const destination = allSelectedAddresses[allSelectedAddresses.length - 1];
        
        // Define os waypoints como todos os endereços, exceto o último
        const waypoints = allSelectedAddresses.slice(0, -1).join('|');

        // Gera a URL do Google Maps
        const routeUrl = `https://www.google.com/maps/dir/?api=1&origin=${encodeURIComponent(origin)}&destination=${encodeURIComponent(destination)}&waypoints=${encodeURIComponent(waypoints)}`;

        // Abre a URL diretamente no navegador
        window.open(routeUrl, '_blank');
    } else {
        alert('Por favor, selecione pelo menos uma escola ou um aluno, e insira o ponto de partida.');
    }
});
