import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#00c',
        alignItems: 'center',
        justifyContent: 'center',
    },
    container1: {
        flex: 0.2,
        width: '100%',
        alignItems: 'center',
    },
    container2: {
        flex: 1.5,
        padding: 20,
        width: '100%',
        backgroundColor: '#ddd',
        alignItems: 'center',
    },
    texto1: {
        fontSize: 50,
        color: '#fff',
    },
    texto2: {
        fontSize: 30,
    },
    top: {
        flexDirection: 'column',
    },
    campo: {
        paddingBottom: 10,
        paddingTop: 10,
    },
    caixa1: {
        borderColor: '#222',
        borderWidth: 1,
        borderRadius: 8,
        color: '#555',
        height: 30,
        width: '100%',
        padding: 10,
    },
    foto0: {
        padding: 10,
        alignItems: 'center',
    },
    foto1: {
        width: 150,
        height: 150,
        backgroundColor: '#eee',
        alignItems: 'center',
        justifyContent: 'center',
        borderRadius: 10,
    },
    entrada: {
        paddingBottom: 10,
        paddingTop: 2,
        alignItems: 'center',
    },
    botao: {
        width: '30%',
        height: 50,
        backgroundColor: '#555',
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 8,
    },
    btn: {
        width: 150,
        height: 40,
        padding: 10,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'yellow',
        borderRadius: 10,
    },
    sucesso: {
        fontSize: 20,
        color: '#0f0',
    },
    txtButton: {
        fontFamily: 'Verdana',
        fontSize: 30,
        color: '#DDD',
    },
})

export default styles