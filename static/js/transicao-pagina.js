document.getElementById('transitionButton').addEventListener('click', function() {
    const vehicle = document.querySelector('.vehicle');
    const dust = document.querySelector('.dust');

    // Iniciar a animação do veículo
    vehicle.style.animation = 'moveVehicle 4s linear forwards';

    // Iniciar a animação da poeira
    dust.style.animation = 'moveDust 10s linear forwards';

    // Redirecionar após a conclusão da animação do veículo
    setTimeout(() => {
        window.location.href = 'pag-inicial-motorista.html'; // Altere para sua próxima página
    }, 4000); // Tempo sincronizado com a animação
});
