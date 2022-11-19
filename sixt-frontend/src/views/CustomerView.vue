<script setup lang="ts">
import FetchData from "../components/FetchData.vue";
import {computed, ref} from "vue";

const endDate = Date.UTC(2022, 11, 20, 10, 0)

const timer = ref(endDate - Date.now());
let interval = setInterval(() => {
  if (timer.value === 0) {
    clearInterval(interval)
  } else {
    timer.value -= 1000
    console.log("seconds: " + (timer.value / 1000).)
    console.log("minutes: " + timer.value / 1000)
    console.log("hours: " + timer.value / 1000)
    console.log("days: " + timer.value / 1000)
    console.log(new Date(timer.value))
  }
}, 1000)
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
