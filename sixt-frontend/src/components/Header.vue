<script setup lang='ts'>

</script>

<template>
  <div class="top sticky w-full px-8 bg-sixt-orange flex flex-row justify-between">
    <div>
    <router-link class="flex flex-row max-w-min" to="/home">
    <img alt="SIXT logo" class="logo h-[80px] w-[80px]" src="@/assets/sixt-vector-logo-cropped.svg" />
    <div class="text-3xl font-bold self-center pt-1">ribution</div>
    </router-link>
    </div>
    <div class="text-3xl font-bold self-center pt-1 text-right">{{['driver'].includes($route.name)? "Drive" : "Rent"}}</div>
  </div>
</template>