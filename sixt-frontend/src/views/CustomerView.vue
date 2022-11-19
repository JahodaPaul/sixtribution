<script setup lang="ts">
import FetchData from "../components/FetchData.vue";
import {computed} from "vue";

const endDate = Date.UTC(2022, 11, 20, 10, 0)
const timer = computed(() => {
  return (Date.now() - endDate)
})
</script>

<template>
  <div class="px-8 py-2">
    <div class="text-3xl">
      My car
    </div>
    <div>

    </div>
    <div>
      Rental ends in {{ timer }}
    </div>
    fetch data: <FetchData />

  </div>
</template>
