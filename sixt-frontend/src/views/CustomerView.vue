<script setup lang="ts">
import {computed, ref} from "vue";
import {useRouter} from 'vue-router'

const router = useRouter()

const homeAddress = ref("Brienner Str. 56, 80333 München")

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
    <div class="text-3xl pt-2">
      My car
    </div>
    <div class="h-[200px]">
      <img alt="my car" class="h-full -m-4 -ml-6" src="@/assets/cars/a2786d1a61ec2647f210be504202ec10f9fc7999.png" />
    </div>
    <div class="rounded-xl bg-white border p-4 ">
      <div><span class="font-bold text-xl">Opel</span> Corsa E</div>
      <div>Rented since: 18. 11. 2022 15:00</div>
    </div>
    <div class="rounded-xl bg-sixt-orange my-4 p-4">
      <div class="flex flex-row justify-around">
        <div class="flex flex-col">
          <img alt="battery" class="h-[70px] w-[70px]" src="@/assets/icon_bat.png" />
          <div class="text-3xl font-bold text-center">42%</div>
          <div class="text-xs text-center">battery state</div>
        </div>
        <div class="flex flex-col">
          <img alt="km" class="h-[70px] w-[70px] text-center" src="@/assets/distance.png" />
          <div class="text-3xl font-bold text-center">126</div>
          <div class="text-xs text-center">km driven</div>
        </div>
        <div class="flex flex-col justify-content-center items-center">
          <img alt="km" class="h-[70px] w-[70px] text-center justify-self-center" src="@/assets/time.png" />
          <div class="text-3xl font-bold text-center">{{ days > 0? days + "d" : "" }} {{hours + "h"}} {{minutes + "min"}}</div>
          <div class="text-xs text-center">time left</div>
        </div>
      </div>
    </div>
    <div class="rounded-xl bg-white border p-4 mb-4 flex flex-col gap-4">
      <div class="text-xl font-bold">My information</div>
      <div class="flex flex-row justify-between">
        <div>Name:</div>
        <div class="font-bold text-lg">Max Mustermann</div>
      </div>
      <div class="flex flex-row justify-between">
        <div class="self-center">Home address:</div>
        <input class="border p-2 rounded-lg" v-model="homeAddress">
      </div>
    </div>
  <div class="bg-black text-white p-3 hover:scale-105 rounded-lg fixed hover:cursor-pointer fixed z-90 bottom-10 right-8 text-lg"
  @click="router.push('/map')">Return the car</div>
  </div>
</template>
