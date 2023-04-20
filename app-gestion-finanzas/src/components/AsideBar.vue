<script setup>
import { RouterLink, RouterView } from 'vue-router'




</script>


<template>
    
    <aside class="p-1 float-md-start d-none vh-100 d-md-block bg-light shadow border border-start-0 d-inline-block p3" >
        <section class="">
        <ul class="navbar-nav me-auto">
            
                <RouterLink to="/addexpending" class="nav-link active" aria-current="page"><li class="p-3 text-center fs-5">
                    <text><i class="bi bi-plus-circle-fill text-success p-2" ></i>Add expending</text>
                </li></RouterLink>
 
                <!-- <li id="calendar">
                    <button type="button" class="btn link-opacity-50-hover">Mostrar calendario</button>
                </li>

                <RouterLink to="/addnewgroup" class="nav-link active link-opacity-50-hover" aria-current="page"><li class="p-3 text-center fs-5">
                    <text><i class="bi bi-folder-plus text-success p-2 "></i>Start a New Group</text>
                </li></RouterLink> -->

            </ul>
        </section>
    </aside>

    <aside class="p-1 d-md-none d-sm-block bg-light shadow border border-start-0 d-inline-block p3 vw-100" >
        <!-- <div class="container-fluid">
        <ul class="navbar-nav me-auto d-flex flex-row justify-content-between p-3">
                <li >Months</li>
                <RouterLink to="/addnewgroup" class="nav-link active" aria-current="page">
                    <li>New Group</li>
                </RouterLink>
            </ul>
        </div> -->
    </aside>

</template>

<style>
  .nav-link:hover {
    background-color: #f0f0f0;
    color: #000;
    text-decoration: none;
  }
</style>