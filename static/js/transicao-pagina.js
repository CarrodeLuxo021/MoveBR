document.getElementById('transitionButton').addEventListener('click', function() {
    const transitionDiv = document.getElementById('transition');
    const dustDiv = document.getElementById('dust');

    // Iniciar a animação do veículo
    const vehicle = document.querySelector('.vehicle');
    vehicle.style.animation = 'moveVehicle 1s forwards';
    
    
    
    setTimeout(() => {
        transitionDiv.style.display = 'flex'; // Mostrar a animação de transição
        dustDiv.style.animation = 'dustEffect 1s forwards'; // Iniciar a animação de poeira
    }, 2000);

    // Esperar a animação terminar antes de mudar de página
    setTimeout(() => {
        window.location.href = 'pag-inicial-motorista.html'; // Substitua pelo URL da próxima página
    }, 1000); // O tempo deve ser igual à duração da animação
});