<script setup>
import NavBar from '../components/NavBar.vue'
import FooterNavBar from '../components/FooterNavBar.vue'
import {RouterLink} from 'vue-router'
</script>

<template>
<header>
    
    <NavBar class="sticky-top bg-body-tertiary d-none d-md-block"/>
               
  </header>
  
    <aside class="p-1 float-start d-none vh-100 d-md-block bg-light shadow border border-start-0 d-inline-block " style="width: 20%;" >
    <section class="">
      <ul>
      <li class=""><RouterLink to="/addexpending" class="nav-link active" aria-current="page">Add expending
            <i class="bi bi-plus-circle-fill text-success position-absolute top-0 start-100 translate-middle pe-3 pb-3" style="font-size: 2.5rem;"></i></RouterLink>
          </li>
        </ul>
    </section>
  </aside>
 
  
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