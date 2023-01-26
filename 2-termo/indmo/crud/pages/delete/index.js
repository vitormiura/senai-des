import React from 'react';
import { View, Text, TouchableOpacity, FlatList } from 'react-native';
import styles from './styles'

export default function Delete({navigation}){
    return(
        <View style={styles.container}>
            <Text style={styles.texto1}>
                Delete
            </Text>
        </View>
    )
}