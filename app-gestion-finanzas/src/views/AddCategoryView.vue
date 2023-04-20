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
          <h1>Add Category</h1>
    </div>
    <div class="row mt-5">
    <div class=" mt-4 text-center">
      <h2>Category Name</h2>
    </div>
    <div class="row text-start justify-content-center">
      <div class="col-6">
      
      <input type="text"  class= "form-control-plaintext border-0 border-bottom border-warning" id="floatingInputGrid">
    </div>  
      
    </div>
    <div class="row text-start justify-content-center mt-5">
    <div class=" mt-4 text-center">
      <h2>Icons</h2>
    </div>
    
      <div class="col-6 border-bottom border-warning dropdown">
        <div class="input-group mb-3">
  <div class="input-group-prepend">
    <span class="input-group-text" id="inputGroup-sizing-default"><i class="bi bi-chat-square-dots-fill"></i></span>
  </div>
  <select class="form-control" >
    <option value="" disabled selected>Select an icon</option>
    <option value="bi bi-emoji-laughing-fill"><i class="bi bi-emoji-laughing-fill"></i> Emoji laughing</option>
    <option value="bi bi-people-fill"><i class="bi bi-people-fill"></i> People</option>
    <option value="bi bi-heart-fill"><i class="bi bi-heart-fill"></i> Heart</option>
  </select>
</div>
      
    

        <!-- <select class="form-select bg-body-tertiary border-0 border-bottom border-warning" id="inputGroupSelect01">
          <option selected class="bi bi-house-fill">hola</option>
          <option value="1" class="bi bi-house-fill">Casa</option>
          <option value="2"><i class="bi bi-fuel-pump-fill"></i></option>
          <option value="3"><i class="bi bi-fuel-pump-fill"></i></option>
          <option value="3"><i class="bi bi-airplane-fill"></i></option>
        </select> -->
      </div>
    </div>

    <div class="row mt-5">
    <div class="mt-4 text-center d-grid gap-2 col-7 mx-auto">
      <button type="submit" class="btn btn-success btn-lg fs-4">Add</button>
    </div>
    </div>
    
  </div>
    </div>
  </div>
  </div>


<footer>
    
  <FooterNavBar class="d-md-none d-block fixed-bottom"/> 
</footer>

</template>