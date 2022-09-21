const form = document.querySelector('#formulario');
form.addEventListener('submit',(e)=>{
     e.preventDefault()
     const peso = Number(e.target.querySelector('#peso').value)
     const altura = Number(e.target.querySelector('#altura').value)
     if(!peso){
        setMsg("Peso inválido");
        return;
     }
     if(!altura){
        setMsg("Altura inválido");
        return;
     }
     const imc = peso / altura **2;
     x = nivelMassa(imc);
     setMsg(`Índice de massa corporal ${x}`)
})
function nivelMassa(imc){
    const nivel = ['abaixo do peso', 'peso normal', 'sobrepeso',
    'obesidade grau 1', 'obesidade grau 2', 'obesidade grau 3'];
  if (imc >= 39.9) return nivel[5];
  if (imc >= 34.9) return nivel[4];
  if (imc >= 29.9) return nivel[3];
  if (imc >= 24.9) return nivel[2];
  if (imc >= 18.5) return nivel[1];
  if (imc < 18.5) return nivel[0];
}

function setMsg(msg){
    const local = document.querySelector('#resultado');
    local.innerHTML = msg
}