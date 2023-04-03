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
    <div class="">
        <h1>soy transactions</h1>
    </div>
</div>
</div>
<footer>
  
  <FooterNavBar class="d-md-none d-block fixed-bottom"/>

</footer>

</template>