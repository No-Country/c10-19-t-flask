<script setup>
import NavBar from '../components/NavBar.vue'
import {RouterLink} from 'vue-router'

</script>

<template>
  
  
    <div class="container-fluid bg-body-tertiary">
      
      <form class="row d-flex align-items-center justify-content-center wv-100 vh-100">
        <div class="col-12 col-sm-10 col-md-6 col-lg-4 py-5 shadow-lg bg-warning mb-5" style="--bs-bg-opacity: .5;">
        
      <div class="mb-3">
        <div class="row justify-content-center">
          <div class="col-10">
            <label for="exampleInputEmail1" class="form-label">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
          </div>    
        </div>
      </div>

      <div class="mb-3">
        <div class="row justify-content-center">
          <div class="col-10">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1">
          </div>
        </div>  
      </div>

      <div class="mb-3">
        <div class="row justify-content-center">
          <div class="col-10">
            <label for="exampleInputPassword1" class="form-label">Confirm Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1">
          </div>
        </div>  
      </div>

      <div class="mb-3 form-check">
        <div class="row justify-content-center">
          <div class="col-10">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">Check me out</label>
          </div>
        </div>
      </div>

      <div class="row justify-content-center">
        <button type="submit" class="btn btn-success shadow col-10" ><RouterLink to="/" class="nav-link active" aria-current="page">Sing up</RouterLink></button>  
      </div>
    

    
      <div class="mb-3">
        <div class="row justify-content-center text-center p-4">
          <h3 class="col-6 ">Sing up with</h3>
        </div>
      </div>

      <div class="mb-3">
        <div class="row justify-content-center">
          <button type="submit" class="btn btn-primary col-10 shadow border border-secondary" ><i class="bi bi-facebook"></i> Facebook</button>
        </div>
      </div>

      <div class="mb-3">
        <div class="row justify-content-center">
          <button type="submit" class="btn btn-danger col-10 shadow border border-secondary"  ><i class="bi bi-google"></i> Google</button>
        </div>
      </div>
      
      </div>
    </form>
    </div>
     
  
</template>