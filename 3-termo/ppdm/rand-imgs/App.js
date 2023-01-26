import React, {useEffect, useState} from 'react';
import {StyleSheet, Text, TouchableOpacity, View, Image} from 'react-native';

const App = () => {
  const [count, setCount] = useState(0);
  const onPress = () => setCount(prevCount => prevCount + 1);

  return (
    <View style={styles.container}>
      <View style={styles.img}>
        <Image source={{uri: `https://www.placemonkeys.com/500/350?random=${count}`, width: 300, height: 300}}/>
      </View>
      <TouchableOpacity style={styles.button} onPress={onPress}>
        <Text>Press Here</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    paddingHorizontal: 10,
  },
  button: {
    alignItems: 'center',
    backgroundColor: '#DDDDDD',
    padding: 10,
  },
  img: {
    alignItems: 'center',
  },
});

export default App;