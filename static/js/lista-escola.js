// Aguarda o carregamento completo do DOM antes de executar o código
document.addEventListener("DOMContentLoaded", function() {
    // Obtém todos os botões de escolas que têm um ID começando com 'btn-'
    const escolaButtons = document.querySelectorAll("button[id^='btn-']");

    // Adiciona um event listener para cada botão encontrado
    escolaButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            // Evita o comportamento padrão do clique (ex.: envio de formulário ou navegação)
            event.preventDefault();

            // Verifica se o botão clicado é o botão "Todos"
            if (this.id === "btn-todos") {
                // Redireciona para a página que lista todos os alunos
                window.location.href = `/listar-alunos`;
            } else {
                // Para os botões de escolas específicas, obtém o nome da escola do ID
                const escola = this.id.replace("btn-", ""); // Remove o prefixo "btn-"

                // Redireciona para a URL que lista os alunos da escola específica com um filtro GET
                window.location.href = `/listar-alunos?escola=${encodeURIComponent(escola)}`;
            }
        });
    });
});
