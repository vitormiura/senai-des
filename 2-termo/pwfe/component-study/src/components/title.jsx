import React, { Component } from 'react'

export const Titulo = (props) => (
    <>
    <b>Bololo <span style={{color: props.color}}>{props.nome}</span> 
    <ul>
        <li>{props.nota}</li>
        <li>{props.turma}</li>
        <li>{props.presente}</li>
        <li>{props.disciplinas}</li>
    </ul>
    </b>
    </>
)

Titulo.defaultProps = {
    nome: "",
    nota: 'sem nota',
    turma: "",
    presente: false,    
    disciplinas: ['oi','oii'],
    color: '#f00',
}

export const Titulo2 = () => (
    <b>chimpanze</b>
)

// export Titulo;
