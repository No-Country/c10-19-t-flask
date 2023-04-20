<script setup>

import NavBar from '../components/NavBar.vue'
import FooterNavBar from '../components/FooterNavBar.vue'
import AsideNavBar from '../components/AsideBar.vue'
import { ref } from 'vue'
import moment from 'moment'


const transactions = ref([])
const persons = ref([])

const user = JSON.parse(sessionStorage.getItem("user"))
const group_id = user.user.groups[0].id
const user_id = user.user.id
const user_fullname = user.user.fullname
const user_totals = ref("***")

const total_transactions = ref("***")

async function getData(){
  const res = await fetch(`https://clownstech.com/app-finanzas/api/v1/${user_id}/transaction`+`?group_id=${group_id}`);
  let finalRes = await res.json();
  finalRes = finalRes.data.sort(function(a, b) {
    let keyA = new Date(a.date);
    let keyB = new Date(b.date);
    // Compare the 2 dates
    if (keyA > keyB) return -1;
    if (keyA < keyB) return 1;
    return 0;
  });
  finalRes = finalRes.map(objeto => ({
  ...objeto, // copiamos el objeto completo
  date: moment(objeto.date, 'YYYY-MM-DDTHH:mm:ss').format('DD/MM') // formateamos la fecha y la asignamos al atributo date del nuevo objeto
}));
  user_totals.value = finalRes.filter(transaction => transaction.user.id == user_id).reduce((sum, tr) => {
          sum = sum + tr.value
          return sum
        }, 0)
  total_transactions.value = finalRes.reduce((sum, tr) => sum + tr.value, 0)
  transactions.value = finalRes;
}

async function checkPersonInGroups(){
  const res = await fetch(`https://clownstech.com/app-finanzas/api/v1/${user_id}/group/${group_id}/members`);
  let finalRes = await res.json();
  finalRes = finalRes.data.reduce((users, user_group) => {
    const fullname = user_group.user.fullname
    const id = user_group.user.id
    if (id != user_id){
      users.push({fullname: fullname, id: id})
    }
    return users
  }, [])
  persons.value = finalRes
}

checkPersonInGroups()
getData()
</script>

<template>

<header>
    
    <NavBar class="sticky-top bg-body-tertiary d-none d-md-block"/>
    <AsideNavBar />         
</header>
  
<div class="container-fluid">

  <div class="row align-items-center justify-content-center">
      <div class="col m-2 g-2 p-2 text-center rounded-4 bg-primary p-3 shadow-color border border-3 border-light">
        <h1>Total</h1>
        <h2>$ {{ total_transactions }}</h2>
      </div>
  </div>
  <div class="row">
    <div class="col m-2 text-center rounded-4 bg-danger border border-3 border-light pt-3 pb-3  shadow-color  ">
        <Text class="fs-3">{{ user_fullname }}</text><br/>
        <text class="fs-3 fw-medium">$ {{ user_totals }}</text>
    </div>
    <template v-for="person in persons" :key="person.id">
      <div class="col m-2 text-center rounded-4 bg-warning border border-3 border-light pt-3 pb-3 shadow-color">
        <text class="fs-3">{{ person.fullname }}</text><br/>
        <h2 class="fs-3 fw-medium">$ {{ transactions.filter(transaction => transaction.user.id == person.id).reduce((sum, tr) => {
          sum = sum + tr.value
          return sum
        }, 0) }}</h2>
      </div>
    </template>
    <template v-if="persons.length == 0">
      <div class="col m-2 d-flex align-items-center justify-content-center text-center rounded-4 border border-3 border-light pt-3 pb-3 shadow-color">
        <RouterLink to="/addmember" class="nav-link active" aria-current="page"><i class="bi bi-plus-circle-fill text-success" style="font-size: 2rem;"></i><p class="m-0">Add Person</p></RouterLink>
      </div>
    </template>  
  </div>
  <div class="row m-md-3 me-1">
  <h2 class="text-center">Transactions</h2>
  <ul class="list-group ms-3">
    <li class="list-group-item shadow d-flex justify-content-center align-items-center" v-for="transaction in transactions" :key="transaction.id">
      <div class="fs-4 fw-bold me-3">{{ transaction.date }}</div>
      <div class="ms-2 me-auto">
        <div class="fw-bold">{{ transaction.category.name}}</div>
        {{ transaction.user.fullname }}
      </div>
      <div class="fs-4 fw-bold">$ {{ transaction.value }}</div>
    </li>
  </ul>
  </div>
</div>

<footer>
  
  <FooterNavBar class="d-md-none d-block fixed-bottom"/>

</footer>

</template>

<style scoped>

.shadow-color {
  box-shadow: 2px 2px 2px #323232;

}

.person{
  font-size: rfs(100px)
}


</style>