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
  <div class="row">
      <div class="col-12 text-center p-2 mt-1 shadow">
          <h1>Add Expenses</h1>
      </div>
  </div>

  <div class="row mt-4 text-center">
    <h2>Category</h2>
  </div>
  <div class="row text-start justify-content-center">
    <div class="col-6 border-bottom border-warning">
      <i class="bi bi-caret-down"></i>
    </div>
  </div>

  <div class="row mt-5 justify-content-center me-2">
    <div class="col-2 text-center">
      <text class="fs-3 fw-semibold">US$</text></div>
    <div class="col-4">
      <input type="number" class= "form-control-plaintext border-0 border-bottom border-warning" id="floatingInputGrid">
    </div>
  </div>
</div>
<footer>
    
  <FooterNavBar class="d-md-none d-block fixed-bottom"/> 
</footer>

</template>