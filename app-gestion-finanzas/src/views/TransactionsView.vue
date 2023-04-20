<script setup>

import NavBar from '../components/NavBar.vue'
import FooterNavBar from '../components/FooterNavBar.vue'
import AsideNavBar from '../components/AsideBar.vue'
import {RouterLink} from 'vue-router'
import ChildComps from '../views/AddExpendingView.vue'
import { ref } from 'vue'


const transactions = ref([])

console.log()
const user = JSON.parse(sessionStorage.getItem("user"))
console.log(user)
const group_id = user.user.groups[0].id
console.log(group_id)
const user_id = user.user.id
console.log(user_id)

async function getData(){
        const res = await fetch(`https://clownstech.com/app-finanzas/api/v1/${user_id}/transaction`+`?group_id=${group_id}`);
        let finalRes = await res.json();
        console.log(finalRes)
        finalRes = finalRes.data.sort(function(a, b) {
          let keyA = new Date(a.date);
          let keyB = new Date(b.date);
          // Compare the 2 dates
          if (keyA > keyB) return -1;
          if (keyA < keyB) return 1;
          return 0;
        });
        // finalRes = finalRes.map(element => element.user = element.user.fullname);
        transactions.value = finalRes;
      }

console.log(transactions)

getData()
</script>

<template>

<header>
    
    <NavBar class="sticky-top bg-body-tertiary d-none d-md-block"/>
               
  </header>
  
   
      <AsideNavBar />
    
 
  
<div class="container">
<div class="row row-cols-2 g-3 justify-content-evenly">
    <div class="col-12 text-center rounded-4 bg-primary p-3 shadow-color border border-3 border-light">
      <h1>Total</h1>
      <h2>$12000</h2>
    </div>

    <div class="col-5 col-lg-5 text-center rounded-4 bg-danger border border-3 border-light pt-3 pb-3  shadow-color  ">
        <Text class="fs-3">persona-1</text><br/>
        <text class="fs-3 fw-medium">$100000000</text>
    </div>
    <div class="col-5 col-lg-5 text-center rounded-4 bg-warning border border-3 border-light pt-3 pb-3 shadow-color">
      <text class="fs-3">persona 2</text><br/>
      <h2 class="fs-3 fw-medium">$2000</h2>
    </div>
  
    
</div>

<div class="row justify-content-center mt-4 g-5">
  <div class="col text-center">
    <p class="h1">Transactions</p>
  </div>
  <div class="row justify-content-center mt-5" v-for="transaction in transactions" :key="transaction.id">
  <div class="col-3">
    <p class="h3">{{ transaction.date }}</p>
  </div>
  <div class="col-3 text-center">
    <p class="h3">{{ transaction.user.fullname }}</p>
  </div>
  <div class="col-3 text-center">
    <p class="h3">{{ transaction.category_id }}</p>
  </div>
  <div class="col-3 text-end">
    <p class="text-end h3">{{ transaction.value }}</p>
  </div>
</div>
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