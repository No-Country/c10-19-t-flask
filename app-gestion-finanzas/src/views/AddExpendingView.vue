<script setup>
import NavBar from '../components/NavBar.vue'
import FooterNavBar from '../components/FooterNavBar.vue'
import {RouterLink} from 'vue-router'
</script>

<template>
<header>
    
    <NavBar class="sticky-top bg-body-tertiary d-none d-md-block"/>
               
  </header>
<div class="container">
<div class="row">
    <div class="col">
        <h1>soy add expending</h1>
    </div>
</div>
</div>
<footer>
    
  <FooterNavBar class="d-md-none d-block fixed-bottom"/> 
</footer>

</template>