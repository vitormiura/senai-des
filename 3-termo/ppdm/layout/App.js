import { useDeviceOrientation } from "@react-native-community/hooks";
import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View, Dimensions, Button } from "react-native";

export default function App() {
  console.log(Dimensions.get("screen"));
  const posicao = useDeviceOrientation();
  console.log(posicao);
  return (
    <>
      <View style={{ height: posicao == "landscape" ? "100%" : "100%" }}>
        <View
          style={{
            backgroundColor: "red",
            flex: posicao == "landscape" ? 1 : 0.87,
          }}
        />
        <View
          style={{
            backgroundColor: "green",
            flex: 1,
          }}
        />
        <Button title="butao" onPress={() => alert("jaja", 'haha')}/>
        <View
          style={{
            backgroundColor: "black",
            flex: 1,
          }}
        />
        {/* <Text>Open up App.js to start working on your app!</Text> */}
        <StatusBar style="auto" />
      </View>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
