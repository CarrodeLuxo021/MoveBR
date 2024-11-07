//MASCARA DO TELEFONE

const handlePhone = (event) => {
    let input = event.target
    input.value = phoneMask(input.value)
}

const phoneMask = (value) => {
    if (!value) return ""
    value = value.replace(/\D/g, '')
    value = value.replace(/(\d{2})(\d)/, "($1) $2")
    value = value.replace(/(\d)(\d{4})$/, "$1-$2")
    return value
}

//MASCARA DO CPF

const cpf = v => {
    v = v.replace(/\D/g, "")                    //Remove tudo o que não é dígito
    v = v.replace(/^(\d{3})(\d)/, "$1.$2")       //Coloca um ponto entre o terceiro e o quarto dígitos
    v = v.replace(/^(\d{3})\.(\d{3})(\d)/, "$1.$2.$3") //Coloca um ponto entre o sexto e o sétimo dígitos
    v = v.replace(/\.(\d{3})(\d{2})$/, ".$1-$2") //Coloca um hífen entre o nono e o décimo dígitos
    return v
}

function formatarCPF(valor) {
    const input = document.getElementById('cpf');
    input.value = cpf(valor);
}


//MACARA CNPJ

const cnpj = v => {
    v = v.replace(/\D/g, "")                    //Remove tudo o que não é dígito
    v = v.replace(/^(\d{2})(\d)/, "$1.$2")       //Coloca um ponto entre o segundo e o terceiro dígitos
    v = v.replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3") //Coloca um ponto entre o quinto e o sexto dígitos
    v = v.replace(/^(\d{2})\.(\d{3})\.(\d{3})(\d)/, "$1.$2.$3/$4") //Coloca uma barra entre o oitavo e o nono dígitos
    v = v.replace(/(\d{2})\.(\d{3})\.(\d{3})\/(\d{4})(\d{1})/, "$1.$2.$3/$4-$5") //Coloca um hífen entre o décimo segundo e o décimo terceiro dígitos
    return v
}

function formatarCNPJ(valor) {
    const input = document.getElementById('cnpj');
    input.value = cnpj(valor);
}