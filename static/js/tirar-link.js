// Função para verificar a URL atual e exibir/ocultar botões com base no padrão da URL
function verificarURL() {
    const urlAtual = window.location.href; // Obtém a URL atual da página
    // Regex para verificar se a URL contém '/cadastrar-aluno/{codigo}', onde {codigo} é uma string dinâmica
    const padrao = /http:\/\/127\.0\.0\.1:5000\/cadastrar-aluno\/.+/;

    // Testa se a URL atual corresponde ao padrão da expressão regular
    if (padrao.test(urlAtual)) {
        // Se a URL corresponder, oculta os botões 'gerarLinkBtn' e 'visibleButton'
        document.getElementById('gerarLinkBtn').style.display = 'none';
        document.getElementById('visibleButton').style.display = 'none';
    } else {
        // Caso contrário, mostra os botões
        document.getElementById('gerarLinkBtn').style.display = 'block';
        document.getElementById('visibleButton').style.display = 'block';
    }
}

// Função para redirecionar para uma URL específica de cadastro de aluno, com um código dinâmico
function redirecionar() {
    // Redireciona para a URL gerada pelo 'url_for' (no backend, essa URL é substituída pelo código correto)
    window.location.href = "{{ url_for('cadastrar_aluno', codigo=codigo) }}";
}

// Chama a função para verificar a URL quando a página é carregada
verificarURL();

// Função para gerar um código e copiar o link para a área de transferência
function gerarCodigo() {
    // Envia uma requisição GET para a rota '/gerar-codigo'
    fetch('/gerar-codigo')
        .then(response => response.json()) // Converte a resposta para JSON
        .then(data => {
            // Copia o link gerado para a área de transferência
            navigator.clipboard.writeText(data.link)
                .then(() => {
                    // Exibe um alerta notificando que o código foi copiado com sucesso
                    alert("Código copiado para a área de transferência!");
                })
                .catch(error => {
                    // Caso haja erro ao copiar o link para a área de transferência
                    console.error("Erro ao copiar para a área de transferência:", error);
                    alert("Erro ao copiar o código!");
                });
        })
        .catch(error => {
            // Caso haja erro ao gerar o código
            console.error("Erro ao gerar código:", error);
            alert("Erro ao gerar o código!");
        });
}
