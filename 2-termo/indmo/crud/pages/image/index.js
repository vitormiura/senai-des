import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import styles from './styles'

export default function Image({navigation}) {
    return (
        <View style={styles.container}>
            <Text style={styles.texto1}>
                Image
            </Text>
        </View>
    )
}