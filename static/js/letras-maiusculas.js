// Seleciona todos os campos de entrada do tipo texto e email
const inputs = document.querySelectorAll('input[type="text"]');

// Adiciona eventos aos campos de entrada para monitorar mudanças e pressionamento de teclas
inputs.forEach(input => {
  // Adiciona um evento 'input' para capturar alterações no valor do campo em tempo real
  input.addEventListener('input', () => {
    capitalizeFirstLetter(input); // Chama a função para capitalizar a primeira letra de cada palavra
  });

  // Adiciona um evento 'keydown' para monitorar a tecla pressionada
  input.addEventListener('keydown', (event) => {
    // Verifica se a tecla pressionada foi a barra de espaço
    if (event.key === ' ') {
      // Aguarda o valor ser atualizado antes de chamar a função de capitalização
      setTimeout(() => {
        capitalizeFirstLetter(input);
      }, 0); // O delay de 0ms assegura que o valor atualizado do campo é processado
    }
  });
});

// Função para capitalizar a primeira letra de cada palavra no valor do campo
function capitalizeFirstLetter(input) {
  // Divide o valor do campo em palavras, separadas por espaços
  const words = input.value.split(' ');
  for (let i = 0; i < words.length; i++) {
    // Verifica se a palavra não está vazia
    if (words[i]) {
      // Capitaliza a primeira letra e transforma o restante em minúsculas
      words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1).toLowerCase();
    }
  }
  // Junta as palavras novamente com espaços e atualiza o valor do campo
  input.value = words.join(' ');
}
