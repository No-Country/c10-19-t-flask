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
      <div class="col-12 col-lg-9 py-5 shadow-lg bg-light mb-5">
      <div class="col-12 text-center p-2 shadow">
          <h1>Add New Group</h1>
    </div>
    <div class="row mt-5 justify-content-center">
    <div class=" mt-4 text-center">
      <h2>Group Name</h2>
    </div>
    
      <div class="col-8 col-lg-6">
      <input type="text" class= "form-control-plaintext border-0 border-bottom border-warning" id="floatingInputGrid">
    </div>
    </div>  
      
    </div>


    <div class="row mt-5">
    <div class="mt-4 text-center d-grid gap-2 col-7 mx-auto">
      <button type="submit" class="btn btn-success btn-lg fs-4">Add</button>
    </div>
    </div>
    
  </div>
    </div>
  


<footer>
    
  <FooterNavBar class="d-md-none d-block fixed-bottom"/> 
</footer>

</template>