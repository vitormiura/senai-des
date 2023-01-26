import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import styles from './styles'


export default function Home({navigation}){
    return(
        <View style={styles.container}>
            <Text style={styles.texto1}>
                Home
            </Text>
        </View>
    )
}