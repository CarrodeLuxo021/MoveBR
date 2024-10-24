document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById('menu-icon');
    const menu = document.getElementById('menu');

    menuIcon.addEventListener('click', function () {
        // Adiciona ou remove a classe 'show' para mostrar/esconder o menu
        if (menu.classList.contains('show')) {
            menu.classList.remove('show'); // Esconde o menu (desliza para fora)
        } else {
            menu.classList.add('show'); // Mostra o menu (desliza para dentro)
        }
    });
});

// Função para abrir e fechar o menu
document.getElementById('toggleBtn').addEventListener('click', function () {
    var menu = document.getElementById('menu1');
    menu.style.display = menu.style.display === 'grid' ? 'none' : 'grid';
    this.innerHTML = menu.style.display === 'grid' ? '&#9660;' : '&#9650;';
});

// Selecionar todos os botões de meses
const monthButtons = document.querySelectorAll('.month');
const details = document.getElementById('details');
const selectedMonth = document.getElementById('selectedMonth');

// Adicionar evento de clique para cada botão
monthButtons.forEach(button => {
    button.addEventListener('click', function () {
        // Obter o mês atual a partir do botão clicado
        const currentMonth = this.getAttribute('data-month');

        // Verificar se o mês já está selecionado
        if (selectedMonth.textContent === currentMonth) {
            // Se o mês atual já estiver selecionado, ocultar os detalhes
            details.style.display = 'none';
            selectedMonth.textContent = ''; // Limpar o texto do mês selecionado
        } else {
            // Caso contrário, exibir os detalhes
            details.style.display = 'block';
            selectedMonth.textContent = currentMonth; // Atualizar o nome do mês nos detalhes
        }
    });
});


