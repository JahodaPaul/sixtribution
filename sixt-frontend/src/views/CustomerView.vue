<script setup lang="ts">
import {computed, ref} from "vue";

const endDate = Date.UTC(2022, 11, 20, 10, 0)
const today = Date.UTC(new Date().getFullYear(), new Date().getMonth()+1, new Date().getDate(), new Date().getHours(), new Date().getMinutes())

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
    }
}, 1000)
</script>

<template>
  <div class="px-8">
    <div class="text-3xl py-2">
      My car
    </div>
    <div class="h-[200px] bg-red-500">
      Picture of a car
    </div>
    <div>Rented since: 18. 11. 2022 15:00</div>
    <div>
      Battery state: {{ "70%" }}
    </div>
    <div>
      Kilometers driven: {{ 126 }}
    </div>
    <div>
      Rental ends in: {{ days > 0? days + "days" : "" }} {{ hours }} hours {{ minutes }} minutes {{ days > 0? seconds + "seconds" : ""}}
    </div>
  <div class="bg-black text-white p-3 hover:scale-105 rounded-lg fixed hover:cursor-pointer fixed z-90 bottom-10 right-8 text-lg">Return the car</div>
  </div>
</template>
