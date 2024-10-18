

document.addEventListener("DOMContentLoaded", function() {
    // Obtém todos os botões de escolas usando a classe 'escola-btn'
    const escolaButtons = document.querySelectorAll("button[id^='btn-']");

    // Adiciona um event listener para cada botão individualmente
    escolaButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            // Evita comportamento padrão para que possamos controlar o evento
            event.preventDefault();

            // Verifica se o botão clicado é o "Todos" (sem filtro)
            if (this.id === "btn-todos") {
                // Redireciona para listar todos os alunos
                window.location.href = `/listar-alunos`;
            } else {
                // Para botões de escola, extrai o nome da escola a partir do ID do botão
                const escola = this.id.replace("btn-", "");

                // Redireciona para a URL com o filtro da escola, usando o parâmetro GET
                window.location.href = `/listar-alunos?escola=${encodeURIComponent(escola)}`;
            }
        });
    });
});