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

<style scoped>

.shadow-color {
  box-shadow: 2px 2px 2px #323232;

}

.person{
  font-size: rfs(100px)
}


</style>