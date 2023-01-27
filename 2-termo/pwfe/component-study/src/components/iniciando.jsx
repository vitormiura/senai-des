import React, { Component } from 'react';
import { Titulo, Titulo2 } from './title';
import Card from './card';

class Iniciando extends Component {
    state = { 
        contador: 0,
        alunos: [],
        alunosHoje: [{id:1, nome:"carlo", presente:true},{id:2, nome:"antonio", presente:true},{id:3, nome:"marco", presente:false}],
        diaSemana: 5,
        //dados: [{id:1, nome:"carlo", id:2, nome:"antonio"}]
    }

    constructor(){
        super();
        this.decrementar = this.decrementar.bind(this);
    }

    // retornar alunos presentes
    chamada = (id) => {
        return this.state.alunosHoje.find((aluno)=> (
            aluno.id === id
        ))
    }

    incrementar = (id) => {
        var teste = this.chamada(id)
        console.log(teste);
        //recebe id = 1
        // console.log(id);
        // var nome = this.state.dados.find(function(dado){
            
        // })


        // if (this.state.contador == 10) return;
        this.state.contador++;
        this.setState({ contador: this.state.contador })
        console.log(this.state.contador);
    }


    decrementar = () => {
        //SUBTRAIR 1
        // if (this.state.contador > 0){
        //     this.state.contador--;
        //     this.setState({ contador: this.state.contador })
        //     console.log(this.state.contador);
        // }

        if (this.state.contador === 0) return;
        this.state.contador--;
        this.setState({ contador: this.state.contador })
        console.log(this.state.contador);
    }

    definirCorNumero(){
        // IF TERNÁRIO
        var corNumero = this.state.contador % 2 === 0 ? 'vermelho' : 'verde' ;

        return corNumero;
    }

    renderizarAlunos() {
        return (
            <ul>
                {this.state.alunos.map((aluno) => (
                    <li key={aluno.id} >{aluno.nome }</li>
                )) }
            </ul>
        )
    }

    render() { 
        return (
            <>
            <Titulo nome = "haha" nota = '10' turma = 'mat'/>
            <Titulo2/>
            <br />
            <Card nome = 'awdawd'/>
            

            {this.state.alunosHoje.map((aluno) =>(
                <li><Card nome = {aluno.nome}/></li>
            ))}

            <p>Seja bem vindo</p>
            <span className={this.definirCorNumero()}> {this.state.contador} </span>
            
            <button onClick={() => this.incrementar(2)} >incrementar</button>
            {/* Subtrair 1 no contador */}
            <button onClick={this.decrementar} >decrementar</button>
            
             {/* Criar uma função para mapear e retornar os alunos dentro da tag ul li - remover as linhas 51 a 55  */}

            {  this.state.alunos.length === 0 ? 'Não há alunos cadastrados' : 'Os alunos são:' }
                { this.renderizarAlunos()}
                {/* Utilizar o Math random para gerar um index aleatório e carregar um aluno */}
            <h3>{this.state.alunos[Math.floor(Math.random() * (3 - 0) + 0 )]}</h3>
            </>
        );
    }
}
 
export default Iniciando;