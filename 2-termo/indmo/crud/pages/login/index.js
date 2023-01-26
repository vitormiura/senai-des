import React, { useState, useEffect } from "react"
import { auth, logInWithEmailAndPassword, signInWithGoogle } from "./firebaseConfig";
import { useAuthState } from "react-firebase-hooks/auth";
import { View, TextInput, TouchableOpacity, Text } from 'react-native'
import { useNavigation } from '@react-navigation/native';

import Styles from './styles.js'
import Create from "../create";

export default function ({ navigation }) {
  const [email, setEmail] = useState()
  const [password, setPassword] = useState()
  const [user, loading, error] = useAuthState(auth);

  const navigate = useNavigation();


  useEffect(() => {
    if (loading) {
      return;
    }
    if (user) navigate.navigate(Create);
  }, [user, loading]);

  const loginFirebase = () => {
    console.log(email)
    console.log(password)
    console.log("chamou")
    logInWithEmailAndPassword(email, password);
  }

  return (
    <View style={Styles.container}>
      <TextInput
        style={Styles.txtInput1}
        placeholder='email'
        keyboardType='text'
        value={email}
        onChangeText={(e) => { setEmail(e) }}
      />
      <TextInput
        style={Styles.txtInput1}
        placeholder='password'
        keyboardType='password'
        value={password}
        onChangeText={(e) => { setPassword(e) }}
      />
      <View style={Styles.botoes}>
        <TouchableOpacity
          style={Styles.botaoLogin}
          onPress={() => loginFirebase()}
        >
          <Text style={Styles.txtButton}>Login</Text>
        </TouchableOpacity>
      </View>

    </View>
  )
}

