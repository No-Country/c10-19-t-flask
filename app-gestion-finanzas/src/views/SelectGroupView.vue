<script setup>
import NavBar from '../components/NavBar.vue'
import FooterNavBar from '../components/FooterNavBar.vue'
import AsideNavBar from '../components/AsideBar.vue'
import { useRouter } from "vue-router";
import { ref } from 'vue'

const router = useRouter();


const user = JSON.parse(sessionStorage.getItem("user"))
const user_id = user.user.id
const groups = ref(user.user.groups)

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
            <h2>Select Group</h2>
        </div>
        <div class="row mt-4 justify-content-start me-2">
          <div class="col-6" v-for="group in groups" :key="group.id" :id="group.id">
          <div class="card text-dark bg-light mb-3" style="max-width: 18rem;">
            <div class="card-body">
              <h5 class="card-title mb-3">{{ group.name }}</h5>
              <a href="#" class="btn btn-primary">Transactions</a>
            </div>
          </div>
        </div>
        </div>

      </div>
    </div>
  </div>


<footer>
    
  <FooterNavBar class="d-md-none d-block fixed-bottom"/> 
</footer>

</template>