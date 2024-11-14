function verificarURL() {
    const urlAtual = window.location.href; // Obtém a URL atual
    const padrao = /http:\/\/127\.0\.0\.1:8080\/cadastrar-aluno\/.+/; // Regex para verificar se a URL contém /cadastrar-aluno/{codigo}

    if (padrao.test(urlAtual)) {
        // Se a URL corresponder ao padrão, oculta o botão
        document.getElementById('gerarLinkBtn').style.display = 'none';
        document.getElementById('visibleButton').style.display = 'none';
    } else {
        // Caso contrário, mostra o botão
        document.getElementById('gerarLinkBtn').style.display = 'block';
        document.getElementById('visibleButton').style.display = 'block';
    }
   
}

function redirecionar() {
    // Redireciona para a URL gerada
    window.location.href = "{{ url_for('cadastrar_aluno', codigo=codigo) }}";
}

// Chama a função ao carregar a página
verificarURL();