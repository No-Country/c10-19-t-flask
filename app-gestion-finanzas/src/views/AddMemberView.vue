<script setup>
import NavBar from '../components/NavBar.vue'
import FooterNavBar from '../components/FooterNavBar.vue'
import AsideNavBar from '../components/AsideBar.vue'
import { useRouter } from "vue-router";

const router = useRouter();


const user = JSON.parse(sessionStorage.getItem("user"))
console.log(user)
const group_id = user.user.groups[0].id
console.log(group_id)
const user_id = user.user.id
console.log(user_id)

const data = {
    email: undefined
}

async function addMemberGroup(){
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data), 
    redirect: 'follow'
  };

  // eslint-disable-next-line no-unused-vars
  const res = await fetch(`https://clownstech.com/app-finanzas/api/v1/${user_id}/group/${group_id}/members`, requestOptions);
  router.replace({ name: "transactions", path: "/transactions" });
}

</script>

<template>
<header>
    
    <NavBar class="sticky-top bg-body-tertiary d-none d-md-block"/> 
  </header>

  <AsideNavBar />

  <div class="container me-md-1">
    <div class="row d-flex align-items-center justify-content-center">
      <div class="col-12 col-md-9 p-5 m-3 shadow-lg bg-light">
        
        <div class="col-12 text-center p-2 shadow">
            <h2>Add Person</h2>
        </div>

      <div class="row mt-4 justify-content-center me-2">
        <div class="col-3 p-0 m-0 text-center">
          <text class="fs-3  fw-semibold">Email</text></div>
        <div class="col-7 p-0 m-0">
          <input type="email" class= "form-control-plaintext border-0 border-bottom border-warning" id="email_invited" v-model="data.email">
        </div>
      </div>
    
      <div class="row">
        <div class="mt-4 text-center d-grid gap-2 col-7 mx-auto">
          <button type="botton" class="btn btn-success btn-lg fs-4" @click="addMemberGroup">Add</button>
        </div>
      </div>
      </div>
    </div>
  </div>


<footer>
    
  <FooterNavBar class="d-md-none d-block fixed-bottom"/> 
</footer>

</template>