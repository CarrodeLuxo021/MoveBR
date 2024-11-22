function verificarURL() {
    const urlAtual = window.location.href; // Obtém a URL atual
    const padrao = /http:\/\/127\.0\.0\.1:5000\/cadastrar-aluno\/.+/; // Regex para verificar se a URL contém /cadastrar-aluno/{codigo}

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

verificarURL();


// Função para gerar o link e copiar
function gerarECopiarLink() {
    const link = "{{ linkAt }}"; // Obtém o link diretamente da variável do template
    copiarLink(link);
}

 // Função para copiar o link
 function copiarLink(linkAt) {
    navigator.clipboard.writeText(linkAt).then(() => {
        alert("Link copiado para a área de transferência: " + linkAt);
    }).catch(err => {
        console.error("Erro ao copiar o link: ", err);
    });
}
