import React, { useState, useEffect } from 'react'
import { View, Text, TouchableOpacity, TextInput, Image } from 'react-native'
import styles from './styles'
import { ref, getDownloadURL, uploadBytesResumable } from 'firebase/storage'
import { storage, db } from '../login/firebaseConfig'
import { collection, addDoc } from 'firebase/firestore'

export default function Create ({ navigation }) {
  const [texto, setTexto] = useState()
  const [nome, setNome] = useState()
  const [email, setEmail] = useState()
  const [progressPercent, setProgressoPercent] = useState(0)
  const [imgUrl, setImgUrl] = useState()
  const [image, setImage] = useState()
  const [preview, setPreView] = useState()

  //######################## Imagem ############################
  useEffect(() => {
    if (!image) {
      setPreView(undefined)
      return
    }

    const objectUrl = URL.createObjectURL(image)
    setPreView(objectUrl)

    return () => URL.revokeObjectURL(objectUrl)
  }, [image])

  //######################## Fim Imagem ########################

  const upload = e => {
    e.preventDefault()

    const file = image

    if (!file) {
      console.log('Faltou imagem!')
      return
    }

    if (!nome) {
      console.log('Faltou nome!')
      return
    }

    if (!email) {
      console.log('Faltou e-mail!')
      return
    }

    if (image == null) return

    const storageRef = ref(
      storage,
      `images/${nome.replace(/ +/g, '') + '_' + image.name}`
    )
    const uploadTask = uploadBytesResumable(storageRef, file)

    uploadTask.on('state_changed', snapshot => {
      const progress = Math.round(
        (snapshot.bytesTransferred / snapshot.totalBytes) * 100
      )
      setTimeout(() => {
        setProgressoPercent(progress), 1000
      })
    })
    adicionar()
  }

  async function adicionar () {
    await addDoc(collection(db, 'alunos'), {
      name: nome,
      email: email,
      status: false,
      image: nome.replace(/ +/g, '') + '_' + image.name
    })

    setEmail('')
    setNome('')
    setTexto('Cadastrado com Sucesso!')
    setPreView(undefined)
  }

  return (
    <View style={styles.container}>
      <View style={styles.container1}>
        <Text style={styles.texto1}>Create</Text>
      </View>
      <View style={styles.container2}>
        <Text style={styles.texto2}>Cadastro</Text>

        <View style={styles.top}>
          <View style={styles.campo}>
            <TextInput
              style={styles.caixa1}
              placeholder='Nome'
              value={nome}
              onChangeText={e => {
                setNome(e)
              }}
            />
          </View>
          <View style={styles.campo}>
            <TextInput
              style={styles.caixa1}
              placeholder='Email'
              value={email}
              onChangeText={e => {
                setEmail(e)
              }}
            />
          </View>
        </View>

        <View style={styles.foto0}>
          <img src={preview} style={styles.foto1} />
        </View>

        <View style={styles.entrada}>
          <input
            type='file'
            onChange={e => {
              setImage(e.target.files[0])
            }}
          />
        </View>

        <View style={{ alignItems: 'center' }}>
          <TouchableOpacity style={styles.btn} onPress={upload}>
            <Text>Upload</Text>
          </TouchableOpacity>
        </View>

        <View>
          <Text style={styles.sucesso}>{texto}</Text>
        </View>
      </View>
    </View>
  )
}
