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
  addr: "Arnulfstr. 16/18, 80335 München"
},{
  s_id: "S_5254",
  name: "Munich Stachus (City)",
  position: {
    lat: 48.140033,
    lng: 11.566841
  },
  id: 1,
  addr: "Karlsplatz 3, 80335 München"
}];

const markerIcon = "src/assets/s_pin.png"
const chargingIcon = "src/assets/c_pin.png"

const getSixtInfo = (marker) => {
  const info = `<p><b>SIXT station</b></p>
                ${marker.name}<br>
                ${marker.addr}<br>
                <div class="rounded-lg bg-black text-white p-2 font-bold mt-2 hover:cursor-pointer">Return here!</div>`
  return info
}

const getChargingInfo = (marker) => {
  const info = `<p><b>Charging station</b></p>
                ${marker.name}<br>
                ${marker.addr}<br>
                <div class="rounded-lg bg-black text-white p-2 font-bold mt-2 hover:cursor-pointer">Return here!</div>`
  return info
}

const chargingStations = ref([
  {
    name: "Demo charging station 1",
    position: {
      lat: 48.20,
      lng: 11.53
    },
  },
  {
    name: "Demo charging station 2",
    position: {
      lat: 48.1,
      lng: 11.6
    },
  }
]);

onMounted(async () => {
  console.log("mounted")
  //const res = await fetch('http://131.159.205.244:5000/api/stations').then((res) => res.json())
  //chargingStations.value = res
  //console.log(chargingStations)
});
</script>

<template>
  <div class="h-full">
  <GoogleMap ref="map"
      api-key="AIzaSyCDzbtVQ0VGI-EaoCJat7kdT_vLAeSCcD4"
      style="width: 100%; height: 100%;"
      :center="center"
      :zoom="10"
  >
    <template v-for="marker in sixts">
      <Marker :options='{ position: marker.position, icon: markerIcon }'>
        <InfoWindow :options="{ position: marker.position, content: getSixtInfo(marker)}" />
      </Marker>
    </template>

    <template v-for="chst in chargingStations">
      <Marker :options='{ position: chst.position, icon: chargingIcon }'>
        <InfoWindow :options="{ position: chst.position, content: getChargingInfo(chst)}" />
      </Marker>
    </template>
  </GoogleMap>
  </div>
</template>