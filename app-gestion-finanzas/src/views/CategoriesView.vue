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
            <p class="text-wrap">House<br><i class="bi bi-house-fill p-1"></i>$ 20000</p>
          </div>

          <div class="col p-3">
            <p class="text-wrap">Pet<br><i class="bi bi-house-fill p-1"></i><br>$ 50</p>
          </div>
    
          <div class="col p-3 ">
            <p class="text-wrap">Gifts<br><i class="bi bi-house-fill p-1"></i><br>$ 300</p>
          </div>

          <div class="col p-3 ">
            <p class="text-wrap">Bills<br><i class="bi bi-house-fill p-1"></i><br>$ 250</p>
          </div>

          <div class="col p-3 ">
            <p class="text-wrap">Grosseries<br><i class="bi bi-house-fill p-1"></i><br>$ 1000</p>
          </div>

          <div class="col p-3">
            <RouterLink to="/addcategory"><p class="text-center mt-4 text-secondary" style="font-size: 2.1rem;"><i class="bi bi-plus-circle-fill"></i></p></RouterLink>
          </div>

        </div>
    
       </div>

    </div>

  </div>


<footer>
    
  <FooterNavBar class="d-md-none d-block fixed-bottom"/> 
</footer>

</template>