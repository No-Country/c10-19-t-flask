<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary col-md-12">
    <div class="container-fluid p-2">
      <div class="row">
        <div class="">
          <div class="collapse navbar-collapse d-flex p-2" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item p-2">
                <RouterLink to="/" class="nav-link active" aria-current="page">temporary home</RouterLink>
              </li>
              <li class="nav-item p-2">
                <RouterLink to="/transactions" class="nav-link active" aria-current="page"><i class="bi bi-journal-text p-1 text-wrap"></i>
                  Transactions</RouterLink>
              </li>
              <li class="nav-item p-2">
                <RouterLink to="/about" class="nav-link active" aria-current="page"><i class="bi bi-inboxes p-1 fs-2 aling-text-center"></i><br><text class="fs-6">Categories</text></RouterLink>
              </li>
              <li class="nav-item p-2">
                <RouterLink to="/login" class="nav-link active" aria-current="page"><i class="bi bi-three-dots-vertical p-1"></i>Menu</RouterLink>
              </li>
          
            </ul>
          </div>
        </div>
    </div>
  </div>
</nav>
</template>