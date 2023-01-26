import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#0c0',
        alignItems: 'center',
        justifyContent: 'center',
    },
    texto1: {
        fontSize: 50,
    },
    botao: {
        width: '60%',
        height: 50,
        backgroundColor: '#555',
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 8,
    },
    btn: {
        width: '100%',
        height: 60,
        padding: 10,
        justifyContent: 'center',
        alignItems: 'center',
    },
    txtButton: {
        fontFamily: 'Verdana',
        fontSize: 20,
        color: '#DDD',
    },
    txt: {
        color: '#f00',
        fontSize: 40,
    },
    botoes: {
        width: '50%',
        padding: 10,
        justifyContent: 'center',

    },
    txtInput1: {
        width: '60%',
        height: 40,
        backgroundColor: '#bbb',
        padding: 10,
        marginBottom: 10,
        marginTop: 10,
        borderColor: '#777',
        borderRadius: 5,
    },
    botaoLogin: {
        height: 40,
        backgroundColor: '#555',
        borderRadius: 8,
        color: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: 20,
        fontFamily: 'Verdana'
    }
})

export default styles