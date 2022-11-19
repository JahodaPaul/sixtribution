<script setup>
import { GoogleMap, Marker, InfoWindow } from 'vue3-google-map';
import {onMounted, ref} from "vue";

const center = { lat: 48.145, lng: 11.550 }

const map = ref(null)
onMounted(() => {
  console.log(map)
})

const sixts = [{
  s_id: "S_168",
  name: "Munich Central Train Station",
  position: {
    lat: 48.141922,
    lng: 11.558181
  },
  id: 0,
  ref: null,
  addr: "Arnulfstr. 16/18, 80335 München"
},{
  s_id: "S_5254",
  name: "Munich Stachus (City)",
  position: {
    lat: 48.140033,
    lng: 11.566841
  },
  id: 1,
  ref: null,
  addr: "Karlsplatz 3, 80335 München"
}];

const markerIcon = "src/assets/S.png"
const sixtStation = "<p><b>SIXT station</b></p>"
</script>

<template>
  <div class="bg-red-500">
  <GoogleMap ref="map"
      api-key="AIzaSyCDzbtVQ0VGI-EaoCJat7kdT_vLAeSCcD4"
      style="width: 100%; height: 100%;"
      :center="center"
      :zoom="10"
  >
    <template v-for="marker in sixts">
      <Marker :options='{ position: marker.position, icon: markerIcon, anchorPoint: null }'>
      <InfoWindow :options="{ position: marker.position, content: sixtStation + marker.name +'\n' + marker.addr }" :ref="marker.ref" />
      </Marker>
    </template>
  </GoogleMap>
  </div>
</template>