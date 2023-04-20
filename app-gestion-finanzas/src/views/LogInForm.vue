<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const data = {
  email: undefined,
  password: undefined,
};
console.log(data)

const login = () => {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data), 
    redirect: 'follow'
  };
  JSON.stringify
  fetch("https://clownstech.com/app-finanzas/api/v1/login", requestOptions)
    .then(response => response.json())
    .then((response) => {
            sessionStorage.setItem("user", JSON.stringify(response))
            console.log(response)
            const groups = response.user.groups
            if (groups.length > 1){
              router.replace({ name: "selectgroup", path: "/selectgroup" });
            }
            router.replace({ name: "transactions", path: "/transactions" });
        })
    .catch(error => console.log('error', error));
   
};


</script>

<template>
  
  
    <div class="container-fluid bg-body-tertiary">
      
      <form class="row d-flex justify-content-center wv-100 vh-100">
        <div class="col-12 col-md-10 col-lg-4 py-5 shadow-lg bg-warning mb-5" style="--bs-bg-opacity: .5;">
        
      <div class="mb-2">
        <div class="row justify-content-center">
          <div class="col-10">
            <label for="exampleInputEmail1" class="form-label">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="data.email">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
          </div>    
        </div>
      </div>

      <div class="mb-2">
        <div class="row justify-content-center">
          <div class="col-10">
            <label for="exampleInputPassword1" class="form-label" >Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1" v-model="data.password">
          </div>
        </div>  
      </div>

      <div class="mb-2 form-check">
        <div class="row justify-content-center">
          <div class="col-10">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">Keep me Log In</label>
          </div>
        </div>
      </div>

      <div class="row justify-content-center">
        <button type="button" class="btn btn-success shadow col-10 nav-link active" aria-current="page" @click="login" >Entrar</button>  
      </div>
    

    
      <div class="mb-2">
        <div class="row justify-content-center text-center p-2">
          <h3 class="col-6 col-sm-7">Sing in with</h3>
        </div>
      </div>

      <div class="mb-2">
        <div class="row justify-content-center">
          <button type="button" class="btn btn-primary col-10 shadow border border-secondary" ><i class="bi bi-facebook"></i> Facebook</button>
        </div>
      </div>

      <div class="mb-2">
        <div class="row justify-content-center">
          <button type="button" class="btn btn-danger col-10 shadow border border-secondary"  ><i class="bi bi-google"></i> Google</button>
        </div>
      </div>

      <div class="mb-2">
        <div class="row justify-content-center">
          <button type="button" class="btn btn-light col-10 shadow rounded border border-secondary mt-4 p-3 mt-sm-2"><RouterLink to="/singup" class="nav-link active" aria-current="page">Sing up with E-mail</RouterLink></button>
        </div>
      </div>
      
      </div>
    </form>
    </div>
     
  
</template>