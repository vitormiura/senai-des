import { StatusBar } from 'expo-status-bar';
import React, { useState } from "react";
import { StyleSheet, Text, View, Image, Switch, ImageBackground, TouchableOpacity } from 'react-native';

const smokmonk = { uri: "https://extra.globo.com/incoming/25266652-278-514/w448h673-PROP/blog_monkey.jpg" };
const brunodiff = { uri: "https://c.tenor.com/N7eo74QudhYAAAAd/aaaaaaa-macaco.gif" };

export default function App() {
  const [isEnabled, setIsEnabled] = useState(false);
  const toggleSwitch = () => setIsEnabled(previousState => !previousState);

  return (
    // <View style={styles.container}>
    //   <ImageBackground source={smokmonk} resizeMode="cover" style={styles.image}>
    //     <Text>esquizo!</Text>
    //     <Image source={brunodiff} style={{ width: 400, height: 400 }} />
    //     <StatusBar style="auto" />
    //     <Switch ios_backgroundColor="red" trackColor={{ true: 'blue', false: 'red' }} />
    //   </ImageBackground>
    // </View>

    // <View style={{flex:1}}>
    //   <View style={{flex:0.5, backgroundColor:"#ccc"}}>
    //     <Text style={{color:"#fff"}}>Oi</Text>
    //   </View>

    //   <View style={{flex:0.5, backgroundColor:"#ccc"}}>
    //     <Text style={{color:"#fff"}}>Oi</Text>
    //   </View>
    // </View>

    <View style={styles.container}>
      <TouchableOpacity onPress={() => alert("vc fuma charuto de carne")}>
        <ImageBackground source={brunodiff} style={styles.title}>
          <Text style={styles.text}>Clique-me</Text>
        </ImageBackground>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  image: {
    flex: 1,
    justifyContent: "center"
  },
  text: {
    color: "white",
    fontSize: 42,
    lineHeight: 84,
    fontWeight: "bold",
    backgroundColor: "#ccc",
  },
  title: {
    color: "white",
    fontSize: 30,
    textAlign: "center",
    padding: 100,
    paddingTop: 300,
    paddingBottom: 300,
  }
});
