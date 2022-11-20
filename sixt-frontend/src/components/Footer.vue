<script setup lang='ts'>

</script>

<template>
  <div class="bottom w-full px-8 flex flex-col pb-4 pt-2 text-gray-400" v-if="!['driver'].includes($route.name)">
    <div class="flex flex-row">
      <img alt="SIXT logo" class="logo h-[40px] w-[40px]" src="@/assets/sixt-gray.svg" />
      <div class="text-sm font-bold self-center pt-1">ribution</div>
    </div>
    <div class="text-sm -mt-3 mb-2">might be a new business concept of SIXT.</div>
    <div>Created at <span class="font-bold">HackaTUM 2022</span></div>
  </div>
</template>