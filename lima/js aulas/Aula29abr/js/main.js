nome = prompt("Digite seu nome: ");

if(nome == ''){
    alert("Você não digitou o nome")
}else{
    //alert(nome);
    var msg = document.getElementById("msgbemvindo");
    msg.innerHTML = "Entrou no site " + nome;
    msg.classList.add("bemvindo");

    // setTimeout(() => {
    //     //msg.classList.remove("bemvindo");
    // if(confirm("Deseja ralar do site:")){
    //         window.location = "https://google.com"
    //     }
    // }, 2000);
}

// document.getElementById("kkk").innerHTML = "Pinto"

console.log(document.getElementsByTagName("p"));
 
var teste = document.getElementsByTagName("p");
for(i = 0; i < teste.length; i++){
    teste[i].innerHTML = "Bololo Haha";
}

// function  desFt(){
//     div = document.getElementById("containerImg");
//     div.style.display = "none";
//     div.removeChild(foto);
 
// }

// function ft(){
//     div = document.getElementById("containerImg");
//     div.style.display = "block";
//     foto = document.createElement("img");
//     foto.src = "https://www.senairs.org.br/sites/default/files/styles/scale_sm/public/logos/logos_senai_preto.png?itok=7T8jnVVt";
//     div.appendChild(foto);
// }

function  desFt(){
    div = document.getElementById("containerImg");
    div.style.display = "none";
    div.removeChild(foto);
 
}

setInterval(()=>{
        fetch('https://zoo-animal-api.herokuapp.com/animals/rand',
            {mode: 'cors'}
        ).then(response => {
            return response.json();
        }).then(function (json){
            console.log(json);
            document.getElementById("foto").innerHTML = '<img src="' + json.image_link + '" alt=""/>';
        })
},5000);

// function api(){
//     fetch('https://zoo-animal-api.herokuapp.com/animals/rand',
//         {mode: 'cors'}
//     ).then(response => {
//         return response.json();
//     }).then(function (json){
//         console.log(json);
//         document.getElementById("foto").innerHTML = '<img src="' + json.image_link + '" alt=""/>';
//     })
// }