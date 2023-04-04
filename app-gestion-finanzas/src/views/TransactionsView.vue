<script setup>
import NavBar from '../components/NavBar.vue'
import FooterNavBar from '../components/FooterNavBar.vue'
import AsideNavBar from '../components/AsideBar.vue'
import {RouterLink} from 'vue-router'
</script>

<template>
<header>
    
    <NavBar class="sticky-top bg-body-tertiary d-none d-md-block"/>
               
  </header>
  
   
      <AsideNavBar />
    
 
  
<div class="container-fluid ">
<div class="row d-flex justify-content-center p-2">
    <div class="col-12 text-center rounded-5 bg-primary p-3">
      <h1>Total</h1>
      <h2>$12000</h2>
    </div>
    <div class="col-6 text-center rounded-5 bg-danger border p-3">
        <Text class="fs-3">persona-1</text><br/>
        <text class="fs-3 fw-medium">$100000000</text>
    </div>
    <div class="col-6 text-center rounded-5 bg-warning border p-3">
      <text class="fs-3">persona 2</text><br/>
      <h2 class="fs-3 fw-medium">$2000</h2>
    </div>
</div>
<div class="row justify-content-center mt-4">
  <div class="col text-center">
    <h1>Today</h1>
  </div>
  <div class="row justify-content-center">
  <div class="col-3">
    <h1>holass</h1>
  </div>
  <div class="col-6 text-center">
    <h1 class="">com estas</h1>
  </div>
  <div class="col-3 text-end">
    <h1 class="text-end">chau</h1>
  </div>
</div>
</div>
</div>

<footer>
  
  <FooterNavBar class="d-md-none d-block fixed-bottom"/>

</footer>

</template>