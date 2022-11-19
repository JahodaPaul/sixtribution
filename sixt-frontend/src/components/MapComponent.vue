<template>
  <GoogleMap
      api-key="AIzaSyCDzbtVQ0VGI-EaoCJat7kdT_vLAeSCcD4"
      style="width: 100%; height: 500px"
      :center="center"
      :zoom="11"
  >
    <Marker :options="{ position: center }" />
  </GoogleMap>
</template>

<script>
import { defineComponent } from 'vue'
import { GoogleMap, Marker } from 'vue3-google-map'

export default defineComponent({
  components: { GoogleMap, Marker },
  setup() {
    const center = { lat: 48.145, lng: 11.550 }

    return { center }
  },
})
</script>
