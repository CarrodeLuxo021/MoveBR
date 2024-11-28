// Adiciona um evento de clique ao botão com o ID 'generateRoute'
document.getElementById('generateRoute').addEventListener('click', function() {
    const selectedSchools = []; // Array para armazenar os endereços das escolas selecionadas
    const selectedStudents = []; // Array para armazenar os endereços dos alunos selecionados
    
    // Coleta os endereços das escolas selecionadas (checkboxes com a classe 'school-checkbox' e que estão marcadas)
    const schoolCheckboxes = document.querySelectorAll('.school-checkbox:checked');
    schoolCheckboxes.forEach(checkbox => {
        selectedSchools.push(checkbox.getAttribute('data-address')); // Adiciona o endereço ao array de escolas
    });

    // Coleta os endereços dos alunos selecionados (checkboxes com a classe 'student-checkbox' e que estão marcadas)
    const studentCheckboxes = document.querySelectorAll('.student-checkbox:checked');
    studentCheckboxes.forEach(checkbox => {
        selectedStudents.push(checkbox.getAttribute('data-address')); // Adiciona o endereço ao array de alunos
    });

    // Obtém o valor do campo de origem (ponto de partida) e remove espaços em branco extras
    const originInput = document.getElementById('origin');
    const origin = originInput.value.trim();

    // Verifica se há escolas ou alunos selecionados e se o campo de origem não está vazio
    if ((selectedSchools.length > 0 || selectedStudents.length > 0) && origin !== '') {
        // Combina os endereços de escolas e alunos em um único array
        const allSelectedAddresses = [...selectedSchools, ...selectedStudents];
        
        // Define o destino como o último endereço selecionado (último elemento do array)
        const destination = allSelectedAddresses[allSelectedAddresses.length - 1];
        
        // Define os waypoints como todos os endereços, exceto o último (que é o destino)
        const waypoints = allSelectedAddresses.slice(0, -1).join('|');

        // Gera a URL do Google Maps com origem, destino e waypoints
        const routeUrl = `https://www.google.com/maps/dir/?api=1&origin=${encodeURIComponent(origin)}&destination=${encodeURIComponent(destination)}&waypoints=${encodeURIComponent(waypoints)}`;

        // Abre a URL gerada em uma nova aba do navegador
        window.open(routeUrl, '_blank');
    } else {
        // Se não houver escolas ou alunos selecionados, ou o campo de origem estiver vazio, exibe um alerta
        alert('Por favor, selecione pelo menos uma escola ou um aluno, e insira o ponto de partida.');
    }
});
