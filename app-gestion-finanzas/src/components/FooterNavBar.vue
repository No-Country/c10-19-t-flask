<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AddExpending from '../views/AddExpendingView.vue'

</script>

<template>
<nav class="navbar bg-body-tertiary">
    <div class="container-fluid ">
      
        
      
      <div class="navbar navbar-expand vw-100 d-flex flex-row justify-content-center" id="navbarSupportedContent">
       
        <!-- <div class="col-3"> -->
        <ul class="navbar-nav ">
          <li class="nav-item text-center">
            <RouterLink to="/addexpending" class="nav-link active" aria-current="page"><i class="bi bi-plus-circle-fill text-success position-absolute top-0 start-100 translate-middle pe-3 pb-3" style="font-size: 2rem;"></i></RouterLink>
          </li>
          <li class="nav-item text-center">
            <RouterLink to="/transactions" class="nav-link active " aria-current="page"><i class="bi bi-journal-text fs-5"></i></RouterLink>
            <RouterLink to="/transactions" class="nav-link active " aria-current="page">Transactions</RouterLink>
          </li>
          <li class="nav-item text-center">
          <RouterLink to="/selectgroup" class="nav-link active" aria-current="page"><i class="bi bi-people-fill fs-5" ></i></RouterLink>
          <RouterLink to="/selectgroup" class="nav-link active " aria-current="page">Select Group</RouterLink>
          </li>

          
          <!-- <li class="nav-item text-center">
            <RouterLink to="/categories" class="nav-link active " aria-current="page"><i class="bi bi-inboxes p-1 fs-5"></i></RouterLink>
            <RouterLink to="/categories" class="nav-link active " aria-current="page">Categories</RouterLink>
          </li>
          <li class="nav-item text-center">
            <RouterLink to="/about" class="nav-link active " aria-current="page"><i class="bi bi-inboxes p-1 fs-5"></i></RouterLink>
            <RouterLink to="/about" class="nav-link active " aria-current="page">overview</RouterLink>
          </li> -->
          <!-- <li class="nav-item text-center">
            <RouterLink to="/about" class="nav-link active " aria-current="page"><i class="bi bi-three-dots-vertical p-1 fs-5"></i></RouterLink>
            <RouterLink to="/about" class="nav-link active " aria-current="page">menu</RouterLink>
          </li> -->
          
        </ul>
      <!-- </div> -->
      </div>
    </div>
   
</nav>
     
</template>