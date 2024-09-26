document.addEventListener("DOMContentLoaded", function() {
    const menuIcon = document.getElementById('menu-icon');
    const menu = document.getElementById('menu');

    menuIcon.addEventListener('click', function() {
        // Adiciona ou remove a classe 'show' para mostrar/esconder o menu
        if (menu.classList.contains('show')) {
            menu.classList.remove('show'); // Esconde o menu (desliza para fora)
        } else {
            menu.classList.add('show'); // Mostra o menu (desliza para dentro)
        }
    });
});
