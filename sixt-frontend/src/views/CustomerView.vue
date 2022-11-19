<script setup lang="ts">
import FetchData from "../components/FetchData.vue";
import {computed, ref} from "vue";

const endDate = Date.UTC(2022, 11, 20, 10, 0)
const today = new Date().getTime();

const timer = ref(endDate - today);
let interval = setInterval(() => {
  if (timer.value === 0) {
    clearInterval(interval)
  } else {
    timer.value -= 1000
    const days = Math.floor(timer.value / 1000 / 60 / 60 / 24)
    const hours = ((timer.value - days*(1000*60*60*24)) / 1000 / 60 / 60).toFixed(0)
    console.log(days, hours, Date.now())
    console.log("seconds: " + Math.floor(timer.value / 1000))
    console.log("minutes: " + (timer.value / 1000 / 60).toFixed(0))
    console.log("hours: " + (timer.value / 1000 / 60 / 60).toFixed(0))
    console.log("days: " + (timer.value / 1000 / 60 / 60 / 24).toFixed(0))
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
  <div class="bg-black text-white p-2 rounded-lg fixed hover:cursor-pointer fixed z-90 bottom-10 right-8 ">Button</div>
  </div>
</template>
