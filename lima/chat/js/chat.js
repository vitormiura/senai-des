var input = document.getElementById("msg");
        input.addEventListener("keypress", function (event) {
            if (event.key === "Enter") {
                enviarMSG();
            }
        });
        
        //CDN
        import { initializeApp } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-app.js";
        import { getDatabase, ref, set, push, remove, onValue } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-database.js";

        var firebaseConfig = {
            apiKey: "AIzaSyDuqNXOwbDuqmyVNoDLsYtFRh3Et1tcBiM",
            authDomain: "chatmiura.firebaseapp.com",
            projectId: "chatmiura",
            storageBucket: "chatmiura.appspot.com",
            messagingSenderId: "598470159541",
            appId: "1:598470159541:web:5fa44a7ccc30bd17d562fc",
            measurementId: "G-6MYMR5XSCQ"
        };

        const app = initializeApp(firebaseConfig);

        var db = getDatabase(app);
        const dbRef = ref(db, 'exemplo');

        var meuhtml = "";

        var nomeUsuario = prompt("Digite seu nome");

        onValue(dbRef, (snapshot) => {
            const data = snapshot.val();
            console.log(data);
            meuhtml = "";
            snapshot.forEach(function (childSnapshot) {
                var key = childSnapshot.key;
                console.log(key);
                console.log(childSnapshot.val().nome);
                console.log(childSnapshot.val().mensagem);

                meuhtml += '<div class="msg"><b>' + childSnapshot.val().nome +  '</i></b><span>' + childSnapshot.val().mensagem + '</span></div>';

            });
            atualizarHTML();
        });

        function enviarMSG() {

            var datahj = new Date();
            var hora = datahj.getHours() + ":" + datahj.getMinutes() + ":" + datahj.getSeconds()

            push(ref(db, 'exemplo'), {
                nome: nomeUsuario,
                horario: hora,
                data: datahj,
                mensagem: document.getElementById("msg").value
            });

            document.getElementById("msg").value = "";
        }

        function atualizarHTML() {
            document.getElementById("conteudo").innerHTML = meuhtml
            ajustarScroll();
        }

        function ajustarScroll() {
            console.log("corrirgir scroll");
            var divConteudo = document.getElementById("conteudo");
            divConteudo.scrollTop = divConteudo.scrollHeight;
        }