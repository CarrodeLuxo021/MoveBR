// Seleciona o elemento de entrada de arquivo (input) com o ID 'fotoAluno'
const fotoAlunoInput = document.getElementById('fotoAluno');
// Seleciona o elemento de visualização de imagem (img) com o ID 'foto-aluno-preview'
const fotoAlunoPreview = document.getElementById('foto-aluno-preview');

// Adiciona um evento ao input para detectar mudanças no arquivo selecionado
fotoAlunoInput.addEventListener('change', (e) => {
  // Obtém o primeiro arquivo selecionado pelo usuário
  const file = e.target.files[0];
  // Cria uma nova instância de FileReader para ler o conteúdo do arquivo
  const reader = new FileReader();

  // Define uma função para ser executada quando a leitura do arquivo for concluída
  reader.onload = (e) => {
    // Atualiza o atributo 'src' do elemento de visualização com o resultado da leitura (base64)
    fotoAlunoPreview.src = e.target.result;
  };

  // Inicia a leitura do arquivo como uma URL codificada em base64
  reader.readAsDataURL(file);
});
