<script setup>
import { RouterLink, RouterView } from 'vue-router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary col-md-12">
    <div class="container-fluid">
      
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <RouterLink to="/" class="nav-link active" aria-current="page">Home</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink to="/about" class="nav-link active" aria-current="page">About</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink to="/singin" class="nav-link active" aria-current="page">Sing in</RouterLink>
        </li>
      </ul>
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