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
    <div class="row d-flex aling-items-center justify-content-center mt-4">
      <div class="col-12 col-lg-9 py-5 shadow-lg bg-light mb-5 h-50">
      <div class="col-12 text-center p-2 shadow">
          <h1>Categories</h1>
    </div>

   <div class="row row-cols-lg-4 row-cols-3 p-3 justify-content-around text-center fs-4 fw-semibold">
    <div class="col p-3 ">
      <p class="text-wrap">House<br><i class="bi bi-house-fill p-1"></i>$20</p>
      
    </div>
    
    <div class="col p-3">Column</div>
    <div class="col p-3">Column</div>
    <div class="col p-3">Column</div>
    <div class="col p-3">Column</div>
   </div>
    
    
    </div>
  </div>
  </div>


<footer>
    
  <FooterNavBar class="d-md-none d-block fixed-bottom"/> 
</footer>

</template>