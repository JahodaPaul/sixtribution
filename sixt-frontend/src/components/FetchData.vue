<script setup lang="ts">
import {onMounted, ref} from "vue";

const data = ref(2)

onMounted(async () => {
  const res = await fetch('http://131.159.205.244:5000/api/example/13').then((res) => res.json())
  data.value = res
});

</script>

<template>
  the number: {{data}}
</template>