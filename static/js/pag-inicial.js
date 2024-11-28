// Aguarda o carregamento completo do DOM antes de executar o código
document.addEventListener("DOMContentLoaded", function () {
    // Seleciona o ícone do menu pelo ID 'menu-icon'
    const menuIcon = document.getElementById('menu-icon');
    // Seleciona o menu pelo ID 'menu'
    const menu = document.getElementById('menu');

    // Adiciona um evento de clique ao ícone do menu
    menuIcon.addEventListener('click', function () {
        // Verifica se o menu já possui a classe 'show'
        if (menu.classList.contains('show')) {
            // Remove a classe 'show' para esconder o menu
            menu.classList.remove('show');
        } else {
            // Adiciona a classe 'show' para exibir o menu
            menu.classList.add('show');
        }
    });
});
