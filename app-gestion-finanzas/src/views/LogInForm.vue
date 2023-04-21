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
            } else {
              localStorage.setItem('group_id', groups[0].id)
              router.replace({ name: "transactions", path: "/transactions" });
            }
        })
    .catch(error => console.log('error', error));
   
};


</script>

<template>
  
  
    <div class="container bg-body-tertiary">
      
      <form class="row d-flex align-items-center justify-content-center wv-100 vh-100">
        <div class="col-12 col-md-7 col-lg-6 col-xl-4 py-5" style="--bs-bg-opacity: .5; background-color: #DDDDDD;">
        
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

      <div class="d-grid gap-2 text-center">
        <button type="button" class="btn btn-success shadow my-3" aria-current="page" @click="login" >Login</button>
        <h5>Sing in with</h5>
        <button type="button" class="btn btn-primary shadow border border-secondary" ><i class="bi bi-facebook"></i> Facebook</button>
        <button type="button" class="btn btn-danger shadow border border-secondary"  ><i class="bi bi-google"></i> Google</button>
        <div class="m-2"></div>
        <RouterLink to="/singup" class="btn btn-light shadow rounded border border-secondary " aria-current="page">Create Account</RouterLink>
      </div>
      
      </div>
    </form>
    </div>
     
  
</template>