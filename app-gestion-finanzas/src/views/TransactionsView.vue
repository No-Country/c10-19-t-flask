<script setup>
import NavBar from '../components/NavBar.vue'
import FooterBar from '../components/FooterNavBar.vue'
import {RouterLink} from 'vue-router'
</script>

<template>
<header>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <NavBar class="d-none d-lg-block"/>
                
            </div>
        </div>
    </div>
</header>
<div class="container">
<div class="row">
    <h1>soy transactions</h1>
</div>
</div>
<footer>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <FooterBar class="d-lg-none"/>
                
            </div>
        </div>
    </div>
</footer>

</template>