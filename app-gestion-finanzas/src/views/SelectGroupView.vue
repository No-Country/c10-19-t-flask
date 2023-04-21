<script setup>
import NavBar from '../components/NavBar.vue'
import AsideNavBar from '../components/AsideBar.vue'
import { useRouter } from "vue-router";
import { ref } from 'vue'

const router = useRouter();

const user = JSON.parse(sessionStorage.getItem("user"))
const groups = ref(user.user.groups)
const selectGroup = (group_id) => {
  localStorage.setItem('group_id', group_id)
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
      <div class="col-12 col-md-10 p-5 m-3 shadow-lg bg-light">
        <div class="col-12 text-center p-2 shadow">
            <h2>Select Group</h2>
        </div>
        <div class="row d-flex align-items-center mt-4 justify-content-center">
          <div class="col-12 col-md-10 col-lg-6 text-center" v-for="group in groups" :key="group.id" :id="group.id">
          <div class="card text-dark bg-light mb-3 shadow rounded-4"  >
            <div class="card-body rounded-4" style="background-color: #EEEEEE;">
              <h5 class="card-title mb-3">{{ group.name }}</h5>
              <p>{{ group.description }}</p>
              <button class="btn btn-success btn-small col-10 fs-4" @click="selectGroup(group.id)">View</button>
            </div>
          </div>
        </div>
        </div>

      </div>
    </div>
  </div>


<footer>
    
 
</footer>

</template>