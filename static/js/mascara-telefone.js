// Máscara de telefone
const handlePhone = (event) => {
    // Obtém o elemento de entrada e aplica a máscara ao valor atual
    let input = event.target;
    input.value = phoneMask(input.value);
};

// Função que formata o valor como um número de telefone
const phoneMask = (value) => {
    if (!value) return ""; // Retorna vazio se não houver valor
    value = value.replace(/\D/g, ''); // Remove caracteres que não são números
    value = value.replace(/(\d{2})(\d)/, "($1) $2"); // Formata o código de área
    value = value.replace(/(\d)(\d{4})$/, "$1-$2"); // Formata o número com hífen
    return value;
};

// Máscara de CPF
const cpf = (v) => {
    v = v.replace(/\D/g, ""); // Remove caracteres que não são números
    v = v.replace(/^(\d{3})(\d)/, "$1.$2"); // Adiciona o primeiro ponto
    v = v.replace(/^(\d{3})\.(\d{3})(\d)/, "$1.$2.$3"); // Adiciona o segundo ponto
    v = v.replace(/\.(\d{3})(\d{2})$/, ".$1-$2"); // Adiciona o hífen
    return v;
};

// Função para formatar CPF a partir de um valor e atualizar o campo correspondente
function formatarCPF(valor) {
    const input = document.getElementById('cpf'); // Obtém o campo de CPF pelo ID
    input.value = cpf(valor); // Aplica a máscara ao valor
}

// Máscara de CNPJ
const cnpj = (v) => {
    v = v.replace(/\D/g, ""); // Remove caracteres que não são números
    v = v.replace(/^(\d{2})(\d)/, "$1.$2"); // Adiciona o primeiro ponto
    v = v.replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3"); // Adiciona o segundo ponto
    v = v.replace(/^(\d{2})\.(\d{3})\.(\d{3})(\d)/, "$1.$2.$3/$4"); // Adiciona a barra
    v = v.replace(/(\d{2})\.(\d{3})\.(\d{3})\/(\d{4})(\d{1})/, "$1.$2.$3/$4-$5"); // Adiciona o hífen
    return v;
};

// Função para formatar CNPJ a partir de um valor e atualizar o campo correspondente
function formatarCNPJ(valor) {
    const input = document.getElementById('cnpj'); // Obtém o campo de CNPJ pelo ID
    input.value = cnpj(valor); // Aplica a máscara ao valor
}
