<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="flex flex-col h-screen">
    <Header></Header>

    <div class="h-full">
    <RouterView />
    </div>

    <Footer></Footer>

  </div>

</template>
