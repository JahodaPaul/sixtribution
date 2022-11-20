<script setup>
import { GoogleMap, Marker, InfoWindow } from 'vue3-google-map';
import {onMounted, ref, watch} from "vue";
import {useRoute} from 'vue-router'

const route = useRoute()

const map = ref(null)

var directionsService;
var directionsDisplay;

watch(() => route.hash, (hash) => {
  let lat, lng;
  lat = hash.substring(hash.indexOf("lat=")+4, hash.indexOf("lng=")-1)
  lng = hash.substring(hash.indexOf("lng=")+4)
  Route({lat: Number(lat), lng: Number(lng)})
})

watch(() => map.value?.ready, (ready) => {
  if (!ready) return
  console.log("map ready")
  // do something with the api using `mapRef.value.api`
  // or with the map instance using `mapRef.value.map`
  directionsService = new map.value.api.DirectionsService();
  directionsDisplay = new map.value.api.DirectionsRenderer();
  directionsDisplay.setMap(map.value.map);
})

const myPosition = ref({lat: 48.141922, lng: 11.558181})


const center = { lat: 48.145, lng: 11.550 }

const showingRoute = ref(false)

const Route = (end) => {
  showingRoute.value = true
  console.log("called route with arguments: ")
  console.log(end)
  //var start = new map.value.api.LatLng(48.141922, 11.558181);
  //var end = new map.value.api.LatLng(48.140033, 11.566841);
  var request = {
    origin: myPosition.value,
    destination: end,
    travelMode: map.value.api.TravelMode.DRIVING
  };
  console.log(request)
  directionsService.route(request, function(result, status) {
    if (status == map.value.api.DirectionsStatus.OK) {
      directionsDisplay.setDirections(result);
    } else {
      alert("couldn't get directions:" + status);
    }
  });
}

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
                <div class="rounded-lg bg-black text-white p-2 font-bold mt-2 hover:cursor-pointer"
                onclick="window.location.href = '/map#lat=${marker.position.lat}&lng=${marker.position.lng}'">Return here!</div>`
  return info
}

const getChargingInfo = (marker) => {
  const info = `<p><b>Charging station</b></p>
                ${marker.operator}<br>
                <div class="rounded-lg bg-black text-white p-2 font-bold mt-2 hover:cursor-pointer"
                onclick="window.location.href = '/map#lat=${marker.latitude}&lng=${marker.longitude}'">Return here!</div>`
  return info
}

const chargingStations = ref(null);
let test = ref(
    [
  {
    name: "Demo charging station 1",
    latitude: 48.20,
    longitude: 11.53
  },
  {
    name: "Demo charging station 2",
    latitude: 48.1,
    longitude: 11.6,
  }
]);

onMounted(async () => {
  console.log("mounted")
  const res = await fetch('http://131.159.199.176:5000/api/stations').then((res) => res.json())
  chargingStations.value = Object.values(res).map(v => JSON.parse(v))
  let v = chargingStations.value[0]
  console.log(v)
  console.log("onmounted ended")
  console.log(v)
  console.log(v.latitude)
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
      <Marker :options='{ position: {lat: Number(chst.latitude), lng: Number(chst.longitude)}, icon: chargingIcon }'>
        <InfoWindow :options="{ position: {lat: Number(chst.latitude), lng: Number(chst.longitude)}, content: getChargingInfo(chst)}" />
      </Marker>
    </template>
  </GoogleMap>
  </div>
</template>