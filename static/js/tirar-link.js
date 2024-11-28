function verificarURL(event) {
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

function gerarCodigo() {
    // Envia a requisição GET para a rota '/gerar-codigo'
    fetch('/gerar-codigo')
        .then(response => response.json())
        .then(data => {
            // Copia o link gerado para a área de transferência
            navigator.clipboard.writeText(data.link)
                .then(() => {
                    // Exibe um alerta notificando o sucesso
                    alert("Código copiado para a área de transferência!");
                })
                .catch(error => {
                    console.error("Erro ao copiar para a área de transferência:", error);
                    alert("Erro ao copiar o código!");
                });
        })
        .catch(error => {
            console.error("Erro ao gerar código:", error);
            alert("Erro ao gerar o código!");
        });
}