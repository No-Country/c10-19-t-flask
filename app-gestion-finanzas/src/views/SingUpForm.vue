<script setup>
import {RouterLink} from 'vue-router'

const form = {
  email: undefined,
  fullname: undefined,
  password: undefined,
};
console.log(form)

const submitForm = () => {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(form), 
    redirect: 'follow'
  };
  
  fetch("https://clownstech.com/app-finanzas/api/v1/signup", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
};


</script>

<template>
  
  
    <div class="container bg-body-tertiary">
      
      <form class="row d-flex align-items-center justify-content-center wv-100 vh-100">
        <div class="col-12 col-md-7 col-lg-6 col-xl-4 py-5" style="--bs-bg-opacity: .5; background-color: #DDDDDD;">
        
      <div class="mb-3">
        <div class="row justify-content-center">
          <div class="col-10">
            <label for="exampleInputEmail1" class="form-label">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="form.email">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
          </div>    
        </div>
      </div>

      <div class="mb-3">
        <div class="row justify-content-center">
          <div class="col-10">
            <label for="exampleInputPassword1" class="form-label">Full Name</label>
            <input type="text" class="form-control" id="exampleInputText1" v-model="form.fullname">
          </div>
        </div>  
      </div>

      <div class="mb-3">
        <div class="row justify-content-center">
          <div class="col-10">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1" v-model="form.password">
          </div>
        </div>  
      </div>
      <div class="d-grid gap-2 text-center">
        <RouterLink to="/" class="btn btn-success shadow my-3" aria-current="page" @click="submitForm">Sing Up</RouterLink>  
        <h5>Sing up with</h5>
        <button type="button" class="btn btn-primary shadow border border-secondary" ><i class="bi bi-facebook"></i> Facebook</button>
        <button type="button" class="btn btn-danger shadow border border-secondary"  ><i class="bi bi-google"></i> Google</button>
        <div class="m-2"></div>
        <RouterLink to="/" class="btn btn-light shadow rounded border border-secondary " aria-current="page">Go Back Login</RouterLink>
      </div>

      
      </div>
    </form>
    </div>
     
  
</template>