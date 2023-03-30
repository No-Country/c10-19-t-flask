<script setup>
import NavBar from '../components/NavBar.vue'
import {RouterLink} from 'vue-router'

</script>

<template>
  
  
  <form>
    <div class="container p-3">
      <div class="mb-3">
        <div class="row justify-content-center">
          <div class="col-10 col-lg-6">
            <label for="exampleInputEmail1" class="form-label">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
          </div>    
        </div>
      </div>

      <div class="mb-3">
        <div class="row justify-content-center">
          <div class="col-10 col-lg-6">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1">
          </div>
        </div>  
      </div>

      <div class="mb-3 form-check">
        <div class="row justify-content-center">
          <div class="col-10 col-lg-6">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">Check me out</label>
          </div>
        </div>
      </div>

      <div class="row justify-content-center">
        <button type="submit" class="btn btn-primary col-10 col-lg-6 shadow-md">Entrar</button>  
      </div>
    </div>

  <div class="container p-3">  
    <div class="mb-3">
      <div class="row justify-content-center text-center">
        <h3 class="col-6 ">Sing in with</h3>
      </div>
    </div>

    <div class="mb-3">
      <div class="row justify-content-center">
        <button type="submit" class="btn btn-primary col-10 col-lg-6 shadow-md border border-secondary" ><i class="bi bi-facebook"></i> Facebook</button>
      </div>
    </div>

    <div class="mb-3">
      <div class="row justify-content-center">
        <button type="submit" class="btn btn-light col-10 col-lg-6 shadow-md border border-secondary"  ><i class="bi bi-google"></i> Google</button>
      </div>
      </div>
    </div> 

  </form>
  
</template>