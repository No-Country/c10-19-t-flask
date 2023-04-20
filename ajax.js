
const URL = 'https://clownstech.com/app-finanzas/api/v1'

async function signup(){
    const data = {
        'email': 'email', // input email
        'password': 'password', // input password
        'fullname': 'nombre completo' //input nombre completo
    }

    const requestOptions = {
    method: 'POST',
    body: JSON.stringify(data),
    };

    let response = await fetch(URL+"/signup", requestOptions)
    if (response.status == 401){
        return 'error'
    }

    response = await response.json()
    console.log(response['message'])
    return response.data
}

async function login(){
    const data = {
        'email': 'email', // input email
        'password': 'password', // input password
    }

    const requestOptions = {
    method: 'POST',
    body: JSON.stringify(data),
    };

    let response = await fetch(URL+"/login", requestOptions)
    if (response.status == 401){
        return 'error'
    }

    response = await response.json()
    console.log(response['access_token'])
    localStorage.setItem('token', response['access_token'])
    return response.data
}

import { ref } from 'vue';

const listItems = ref([]);

const data = JSON.parse(sessionStorage.getItem('user'))
const user = data.user

async function getData() {
  const res = await fetch(`https://clownstech.com/app-finanzas/api/v1/${user.id}/transaction?group_id=${user.groups[0].id}`);
  const finalRes = await res.json();
  listItems.value = finalRes;
}

getData()