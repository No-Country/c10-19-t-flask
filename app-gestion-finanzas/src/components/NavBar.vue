<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>

<template>
  
  <nav class="navbar navbar-expand-lg bg-body-tertiary d-flex justify-content-center">
    <div class="container-fluid ">
      <div class="row">
        <div class="">
          <div class="navbar navbar-expand d-flex p-2 " id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item p-2">
                <RouterLink to="/" class="nav-link active " aria-current="page">temporary home</RouterLink>
              </li>
              <li class="nav-item p-2">
                <RouterLink to="/transactions" class="nav-link active " aria-current="page"><i class="bi bi-journal-text"></i>Transactions</RouterLink>
              </li>
              <li class="nav-item p-2">
                <RouterLink to="/categories" class="nav-link active " aria-current="page"><i class="bi bi-inboxes p-1"></i>Categories</RouterLink>
              </li>
              <li class="nav-item p-2">
                <RouterLink to="/login" class="nav-link active " aria-current="page"><i class="bi bi-three-dots-vertical p-1"></i>Menu</RouterLink>
              </li>
          
            </ul>
          </div>
        </div>
    </div>
  </div> 
</nav>



      <!--<ul class="nav justify-content-center">
        <li class="nav-item ">
          <RouterLink to="/" class="nav-link active" aria-current="page" href="#"><i class="bi bi-0-circle"></i>Home</RouterLink>
           <a class="nav-link active" aria-current="page" href="#">Active</a> 
        </li>
        <li class="nav-item">
          <RouterLink to="/about" class="nav-link active" aria-current="page" href="#">About</RouterLink>
           <a class="nav-link" href="#">Link</a> 
        </li>
        <li class="nav-item">
          <RouterLink to="/singin" class="nav-link active" aria-current="page" href="#">Sing in</RouterLink>
           <a class="nav-link" href="#">Link</a> 
        </li>    
      </ul>-->
  

</template>

<!-- <RouterLink to="/">Home</RouterLink>
<RouterLink to="/about">About</RouterLink>
<RouterLink to="/singin">Sing in</RouterLink> -->