import React, { Component } from 'react'
import { Titulo } from './title';

class Card extends Component {
    state = {  }
    
    static defaultProps = {
        nome: "Sem Nome",
    }
    
    render() { 
        return (
            <>
                <div className='card'>
                    {this.props.nome}
                </div>
            </>
        );
    }
}
 
export default Card