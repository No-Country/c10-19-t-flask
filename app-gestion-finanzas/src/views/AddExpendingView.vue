<script setup>
import NavBar from '../components/NavBar.vue'
import FooterNavBar from '../components/FooterNavBar.vue'
import AsideNavBar from '../components/AsideBar.vue'
import { useRouter } from "vue-router";
import { ref } from 'vue'

const router = useRouter();

const options = ref([])

const user = JSON.parse(sessionStorage.getItem("user"))
const group_id = localStorage.getItem('group_id')
const user_id = user.user.id

const expending = {
    type: "SPEND",
    value: undefined,
    category_id: undefined,
    group_id: group_id,
    date: undefined
}

const submitExpending = () => {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(expending), 
    redirect: 'follow'
  };
  
  fetch(`https://clownstech.com/app-finanzas/api/v1/${user_id}/transaction/`, requestOptions)
    .then(response => response.json())
    .then(() => {
            router.replace({ name: "transactions", path: "/transactions" });
        })
    .catch(error => console.log('error', error));
};

async function getCategories(){
  const res = await fetch(`https://clownstech.com/app-finanzas/api/v1/categories`);
  const finalRes = await res.json();
  localStorage.setItem('categories', finalRes.data)
  options.value = finalRes.data
}

getCategories()
</script>

<template>
<header>
    
    <NavBar class="sticky-top bg-body-tertiary d-none d-md-block"/> 
  </header>

  <AsideNavBar />

<div class="container">
    <div class="row d-flex aling-items-center justify-content-center mt-4">
      <div class="col-12 col-lg-9 py-5 shadow-lg bg-light mb-5">
      <div class="col-12 text-center p-2 shadow">
          <h1>Add Expenses</h1>
    </div>

    <div class=" mt-4 text-center">
      <h2>Category</h2>
    </div>
    <div class="row text-start justify-content-center">
      <div class="col-6 border-bottom border-warning">
        <select class="form-select bg-body-tertiary border-0 border-bottom border-warning" id="inputGroupSelect01" v-model="expending.category_id">
          <option value="" disabled selected>Choose a category</option>
          <option v-for="option in options" :key="option.id" :value="option.id">{{ option.name }}</option>
          
        </select>
      </div>
    </div>

    <div class="row mt-4 justify-content-center me-2">
      <div class="col-2 text-center">
        <text class="fs-3 fw-semibold">US$</text></div>
      <div class="col-4">
        <input type="number" class= "form-control-plaintext border-0 border-bottom border-warning" id="floatingInputGrid" v-model.number="expending.value">
      </div>
    </div>

    <div class="row mt-4 justify-content-center me-2">
      <div class="col-2 text-center">
        <text class="fs-3 fw-semibold">Date</text></div>
      <div class="col-4">
        <input type="date" class= "form-control-plaintext border-0 border-bottom border-warning" id="floatingInputGrid" v-model="expending.date">
      </div>
    </div>

    
    <!-- <div class="row mt-4 justify-content-center me-2 input-group">
      <div class="col-2 text-center">
        <text class="fs-3 fw-semibold">Paid</text>
      </div>
      <div class="col-4 ">
        <select class="form-select bg-body-tertiary border-0 border-bottom border-warning" id="inputGroupSelect01">
          <option selected></option>
          <option value="1">Persona1</option>
          <option value="2">persona2</option>
          <option value="3">Mitad y mitad</option>
        </select>
      </div>
    </div> -->
    
 

    <div class="row">
    <div class="mt-4 text-center d-grid gap-2 col-7 mx-auto">
      <button type="submit" class="btn btn-success btn-lg fs-4" @click="submitExpending">Add</button>
    </div>
    </div>
    
    
    </div>
  </div>
  </div>


<footer>
    
  <FooterNavBar class="d-md-none d-block fixed-bottom"/> 
</footer>

</template>