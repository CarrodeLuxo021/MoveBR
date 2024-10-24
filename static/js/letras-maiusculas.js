const inputs = document.querySelectorAll('input[type="text"], input[type="email"]');

inputs.forEach(input => {
  input.addEventListener('input', () => {
    capitalizeFirstLetter(input);
  });

  input.addEventListener('keydown', (event) => {
    if (event.key === ' ') {
      setTimeout(() => {
        capitalizeFirstLetter(input);
      }, 0); // Usar setTimeout para garantir que o valor foi atualizado após o espaço ser adicionado
    }
  });
});

function capitalizeFirstLetter(input) {
  const words = input.value.split(' ');
  for (let i = 0; i < words.length; i++) {
    if (words[i]) {
      words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1).toLowerCase();
    }
  }
  input.value = words.join(' ');
}