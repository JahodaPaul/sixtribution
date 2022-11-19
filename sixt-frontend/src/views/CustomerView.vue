<script setup lang="ts">
import FetchData from "../components/FetchData.vue";
import {computed, ref} from "vue";

const endDate = Date.UTC(2022, 11, 20, 10, 0)
const today = Date.UTC(new Date().getFullYear(), new Date().getMonth()+1, new Date().getDate(), new Date().getHours()+1, new Date().getMinutes()+1)

const timer = ref(endDate - today);
const days = ref(0)
const hours = ref(0)
const minutes = ref(0)
const seconds = ref(0)
let interval = setInterval(() => {
  if (timer.value === 0) {
    clearInterval(interval)
  } else {
    timer.value -= 1000
    days.value = Math.floor(timer.value / 1000 / 60 / 60 / 24)
    hours.value = Math.floor((timer.value - days.value*(1000*60*60*24)) / 1000 / 60 / 60)
    minutes.value = Math.floor((timer.value - days.value*(1000*60*60*24) - hours.value*(1000*60*60)) / 1000 / 60 )
    seconds.value = Math.floor((timer.value - days.value*(1000*60*60*24) - hours.value*(1000*60*60) - minutes.value*(1000*60)) / 1000)
    console.log(days, hours, Date.now())
    console.log("seconds: " + Math.floor(timer.value / 1000))
    console.log("minutes: " + (timer.value / 1000 / 60).toFixed(0))
    console.log("hours: " + (timer.value / 1000 / 60 / 60).toFixed(0))
    console.log("days: " + new Date().getDay())
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
      Rental ends in {{ days }} days {{ hours }} hours {{ minutes }} minutes {{ seconds }} seconds
    </div>
    fetch data: <FetchData />
  <div class="bg-black text-white p-2 rounded-lg fixed hover:cursor-pointer fixed z-90 bottom-10 right-8 ">Button</div>
  </div>
</template>
