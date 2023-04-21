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

                <RouterLink to="/selectgroup" class="nav-link active" aria-current="page"><li class="p-3 text-center fs-5">
                    <text><i class="bi bi-people-fill text-success p-2" ></i>Select Group</text>
                </li></RouterLink>
 
                <!--<RouterLink to="/addnewgroup" class="nav-link active link-opacity-50-hover" aria-current="page"><li class="p-3 text-center fs-5">
                    <text><i class="bi bi-folder-plus text-success p-2 "></i>Start a New Group</text>
                </li></RouterLink> -->

            </ul>
        </section>
    </aside>

</template>

<style>
  .nav-link:hover {
    background-color: #f0f0f0;
    color: #000;
    text-decoration: none;
  }
</style>