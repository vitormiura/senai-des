import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Entypo, FontAwesome, AntDesign, Feather } from '@expo/vector-icons'
import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from './pages/home';
import Create from './pages/create'
import Read from './pages/read';
import Update from './pages/update';
import Delete from './pages/delete';
import Login from './pages/login';
import Image from './pages/image';
import User from './pages/user';

const Pilha = createStackNavigator()
const Nav = createBottomTabNavigator()

function NavBar() {
    return (
        <Nav.Navigator
            screenOptions={{
                tabBarStyle: {
                    backgroundColor: '#000',
                    borderTopColor: 'transparent',
                    paddingBottom: 1,
                    paddingTop: 1,
                },
                tabBarActiveTintColor: '#f0f',
                tabBarInactiveTintColor: '#555'
            }}
        >
            <Nav.Screen name='Login' component={Login}
                options={{
                    headerShown: false,
                    tabBarIcon: ({ size, color }) => (
                        <Feather name='user' size={size} color={color} />
                    )
                }}
            />
            <Nav.Screen name='Home' component={Home}
                options={{
                    headerShown: false,
                    tabBarIcon: ({ size, color }) => (
                        <Entypo name='home' size={size} color={color} />
                    )
                }}
            />
            <Nav.Screen name='Create' component={Create}
                options={{
                    headerShown: false,
                    tabBarIcon: ({ size, color }) => (
                        <Entypo name='squared-plus' size={size} color={color} />
                    )
                }}
            />
            <Nav.Screen name='Read' component={Read}
                options={{
                    headerShown: false,
                    tabBarIcon: ({ size, color }) => (
                        <FontAwesome name='search-plus' size={size} color={color} />
                    )
                }}
            />
            <Nav.Screen name='Update' component={Update}
                options={{
                    headerShown: false,
                    tabBarIcon: ({ size, color }) => (
                        <Entypo name='upload-to-cloud' size={size} color={color} />
                    )
                }}
            />
            <Nav.Screen name='Delete' component={Delete}
                options={{
                    headerShown: false,
                    tabBarIcon: ({ size, color }) => (
                        <AntDesign name='delete' size={size} color={color} />
                    )
                }}
            />
            <Nav.Screen name='Image' component={Image}
                options={{
                    headerShown: false,
                    tabBarIcon: ({ size, color }) => (
                        <Feather name='image' size={size} color={color} />
                    )
                }}
            />
            <Nav.Screen name='User' component={User}
                options={{
                    headerShown: false,
                    tabBarIcon: ({ size, color }) => (
                        <FontAwesome name='user' size={size} color={color} />
                    )
                }}
            />
        </Nav.Navigator>
    )
}

export default function Routers() {
    return (
        <NavigationContainer>
            <Pilha.Navigator>
                <Pilha.Screen
                    name='NavBar'
                    component={NavBar}
                    options={{ headerShown: false }}
                />
                <Pilha.Screen
                    name="Home"
                    component={Home}
                    options={{ headerShown: false }}
                />
                <Pilha.Screen
                    name="Create"
                    component={Create}
                    options={{ headerShown: false }}
                />
                <Pilha.Screen
                    name="Read"
                    component={Read}
                    options={{ headerShown: false }}
                />
                <Pilha.Screen
                    name="Update"
                    component={Update}
                    options={{ headerShown: false }}
                />
                <Pilha.Screen
                    name="Delete"
                    component={Delete}
                    options={{ headerShown: false }}
                />
                <Pilha.Screen
                    name="Login"
                    component={Login}
                    options={{ headerShown: false }}
                />
                <Pilha.Screen
                    name="Image"
                    component={Image}
                    options={{ headerShown: false }}
                />
                <Pilha.Screen
                    name="User"
                    component={User}
                    options={{ headerShown: false }}
                />
            </Pilha.Navigator>

        </NavigationContainer>
    )
}