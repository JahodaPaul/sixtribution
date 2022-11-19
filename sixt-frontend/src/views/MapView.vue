<script setup>
import { GoogleMap, Marker } from 'vue3-google-map';

const center = { lat: 48.145, lng: 11.550 }
</script>

<template>
  <div class="bg-red-500">
  <GoogleMap
      api-key="AIzaSyCDzbtVQ0VGI-EaoCJat7kdT_vLAeSCcD4"
      style="width: 100%; height: 100%;"
      :center="center"
      :zoom="11"
  >
    <Marker :options="{ position: center }" />
  </GoogleMap>
  </div>
</template>