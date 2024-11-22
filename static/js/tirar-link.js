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

$(document).ready(function() {
    $('#gerarCodigoBtn').click(function() {
        // Fazer a requisição AJAX para o backend Flask
        $.ajax({
            url: 'http://127.0.0.1:5000/gerar_codigo',  // URL do backend Flask
            method: 'GET',
            success: function(data) {
                // Exibir o link retornado pelo backend
                const link = data.link;
                $('#link').text(link);

                // Copiar o link para a área de transferência
                navigator.clipboard.writeText(link)
                    .then(function() {
                        alert('Link copiado para a área de transferência!');
                    })
                    .catch(function(err) {
                        console.error('Erro ao copiar para a área de transferência:', err);
                    });
            },
            error: function(error) {
                console.log('Erro ao fazer a requisição AJAX:', error);
            }
        });
    });
});