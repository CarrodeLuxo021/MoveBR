const fotoAlunoInput = document.getElementById('fotoAluno');
const fotoAlunoPreview = document.getElementById('foto-aluno-preview');

fotoAlunoInput.addEventListener('change', (e) => {
  const file = e.target.files[0];
  const reader = new FileReader();

  reader.onload = (e) => {
    fotoAlunoPreview.src = e.target.result;
  };

  reader.readAsDataURL(file);
});