<script setup>
import { RouterLink, RouterView } from 'vue-router'



</script>


<template>
    <aside class="p-1 float-md-start d-none vh-100 d-md-block bg-light shadow border border-start-0 d-inline-block p3" >
        <section class="">
        <ul class="navbar-nav me-auto">
            
            <RouterLink to="/addexpending" class="nav-link active" aria-current="page"><li class="p-3 text-center fs-5"><text><i class="bi bi-plus-circle-fill text-success p-2" ></i>Add expending
                    </text>
                </li></RouterLink>
 
            <li id="calendar"><button type="button" class="btn">Mostrar calendario</button>
                </li>
            </ul>
        </section>
    </aside>

    <aside class="p-1 d-md-none d-sm-block bg-light shadow border border-start-0 d-inline-block p3 vw-100" >
        <div class="container-fluid">
        <ul class="navbar-nav me-auto d-flex flex-row justify-content-between p-3">
                <li >Months</li>
                <li><i class="bi bi-pencil fs-3"></i></li>
                
            </ul>
        </div>
    </aside>

</template>