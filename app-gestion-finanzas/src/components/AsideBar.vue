<script setup>
import { ref } from 'vue'

const listGroups = ref([])
const groups = JSON.parse(sessionStorage.getItem('user')).user.groups
console.log(groups)
listGroups.value = groups

</script>
<template>
    
    <aside class="p-1 float-md-start d-none vh-100 d-md-block bg-light shadow border border-start-0 d-inline-block p3" >
        <section class="">
        <ul class="navbar-nav me-auto">
            
                <RouterLink to="/addexpending" class="nav-link active" aria-current="page"><li class="p-3 text-center fs-5">
                    <text><i class="bi bi-plus-circle-fill text-success p-2" ></i>Add expending</text>
                </li></RouterLink>
 
                <li id="calendar">
                    <ul class="navbar-nav me-auto fs-5 fw-semibold text-center ">Grupos</ul>
                    <li class="p-3 fs-6">Grupo 1</li>
                </li>

                <!--<RouterLink to="/addnewgroup" class="nav-link active link-opacity-50-hover" aria-current="page"><li class="p-3 text-center fs-5">
                    <text><i class="bi bi-folder-plus text-success p-2 "></i>Start a New Group</text>
                </li></RouterLink> -->

            </ul>
        </section>
    </aside>

    <aside class="p-1 d-md-none d-sm-block bg-light shadow border border-start-0 d-inline-block p3 vw-100" >
        <div class="container-fluid">
            <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button"  id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                        GRUPOS
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1" v-for="group in listGroups" :key="group.id">
                    <li><a class="dropdown-item" href="#">{{ group.name }}</a></li>
                </ul>
            </div>
        </div>
    </aside>

</template>

<style>
  .nav-link:hover {
    background-color: #f0f0f0;
    color: #000;
    text-decoration: none;
  }
</style>