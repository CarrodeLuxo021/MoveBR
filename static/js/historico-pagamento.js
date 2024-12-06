// Aguarda o carregamento completo do DOM antes de executar o código
document.addEventListener("DOMContentLoaded", function () {
    // Seleciona o ícone de menu pelo ID 'menu-icon'
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

// Adiciona um evento de clique ao botão com ID 'toggleBtn' para abrir/fechar outro menu
document.getElementById('toggleBtn').addEventListener('click', function () {
    // Seleciona o menu com ID 'menu1'
    var menu = document.getElementById('menu1');
    // Alterna a exibição entre 'grid' e 'none'
    menu.style.display = menu.style.display === 'grid' ? 'none' : 'grid';
    // Atualiza o ícone do botão baseado no estado do menu
    this.innerHTML = menu.style.display === 'grid' ? '&#9660;' : '&#9650;';
});

// Seleciona todos os botões com a classe 'month'
const monthButtons = document.querySelectorAll('.month');
// Seleciona o elemento de detalhes pelo ID 'details'
const details = document.getElementById('details');
// Seleciona o elemento que exibe o mês selecionado pelo ID 'selectedMonth'
const selectedMonth = document.getElementById('selectedMonth');

// Adiciona um evento de clique para cada botão de mês
monthButtons.forEach(button => {
    button.addEventListener('click', function () {
        // Obtém o valor do atributo 'data-month' do botão clicado
        const currentMonth = this.getAttribute('data-month');

        // Verifica se o mês clicado já está selecionado
        if (selectedMonth.textContent === currentMonth) {
            // Se sim, oculta os detalhes e limpa o texto do mês selecionado
            details.style.display = 'none';
            selectedMonth.textContent = '';
        } else {
            // Caso contrário, exibe os detalhes e atualiza o mês selecionado
            details.style.display = 'block';
            selectedMonth.textContent = currentMonth;
        }
    });
});
