function calcular_viagem() {
    // Pegar os valores do formulário e convertê-los para números
    const etanol = Number(document.getElementById("etanol").value);
    const gasolina = Number(document.getElementById("gasolina").value);
    const combusivel_usado = document.getElementById("combustivel_usado").value;
    const gasto_medio = Number(document.getElementById("gasto_medio").value);
    const distancia = Number(document.getElementById("distancia").value);
    const velo_media = Number(document.getElementById("velo_media").value);
    const volta = document.getElementById("volta").checked;

    // Verificação para garantir que os valores necessários estão preenchidos
    if (!etanol || !gasolina || !gasto_medio || !distancia || !velo_media) {
        document.getElementById('resultado').innerHTML = '<h2>Por favor, preencha todos os campos obrigatórios!</h2>';
        return;
    }

    // Cálculos
    let valorTotal_etanol = (distancia / gasto_medio) * etanol;
    let valorTotal_gasolina = (distancia / gasto_medio) * gasolina;
    let combustivel_quant_usada = distancia / gasto_medio;

    const pedagio_quant = Number(document.getElementById("pedagio_quant").value || 0);
    const pedagio_valor = Number(document.getElementById("pedagio_valor").value || 0);

    let custo_c_pedagio = pedagio_quant * pedagio_valor;

    let custo_total_etanol = valorTotal_etanol + custo_c_pedagio;
    let custo_total_gasolina = valorTotal_gasolina + custo_c_pedagio;

    let tempo_de_viagem = distancia / velo_media;

    // Ajuste para ida e volta
    if (volta) {
        combustivel_quant_usada *= 2;
        valorTotal_etanol *= 2;
        valorTotal_gasolina *= 2;
        custo_c_pedagio *= 2;
        custo_total_etanol *= 2;
        custo_total_gasolina *= 2;
        tempo_de_viagem *= 2;
    }

    // Exibir resultados de acordo com o combustível usado
    if (combusivel_usado === "etanol") {
        document.getElementById('resultado').innerHTML = `
            <h2>Resumo de Viagem</h2>
            <ul>
                <li>Combustível: <span>${combusivel_usado}</span></li>
                <li>Litros de combustível consumidos: <span>${combustivel_quant_usada.toFixed(2)} L</span></li>
                <li>Gasto médio de combustível: <span>${gasto_medio.toFixed(2)} KM/L</span></li>
                <li>Valor gasto com combustível: <span>${valorTotal_etanol.toFixed(2)} R$</span></li>
                <li>Tempo de viagem: <span>${tempo_de_viagem.toFixed(2)} horas</span></li>
                <li>Custo com pedágios: <span>${custo_c_pedagio.toFixed(2)} R$</span></li>
                <li>Custo total: <span>${custo_total_etanol.toFixed(2)} R$</span></li>
            </ul>
        `;
    } else if (combusivel_usado === "gasolina") {
        document.getElementById('resultado').innerHTML = `
            <h2>Resumo de Viagem</h2>
            <ul>
                <li>Combustível: <span>${combusivel_usado}</span></li>
                <li>Litros de combustível consumidos: <span>${combustivel_quant_usada.toFixed(2)} L</span></li>
                <li>Gasto médio de combustível: <span>${gasto_medio.toFixed(2)} KM/L</span></li>
                <li>Valor gasto com combustível: <span>${valorTotal_gasolina.toFixed(2)} R$</span></li>
                <li>Tempo de viagem: <span>${tempo_de_viagem.toFixed(2)} horas</span></li>
                <li>Custo com pedágios: <span>${custo_c_pedagio.toFixed(2)} R$</span></li>
                <li>Custo total: <span>${custo_total_gasolina.toFixed(2)} R$</span></li>
            </ul>
        `;
    }
}

function limpar() {
    document.getElementById('resultado').innerHTML = '<h1>Insira os dados para Ver os resultados aqui:</h1>';
}