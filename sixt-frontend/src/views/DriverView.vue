<script setup>
import { GoogleMap, Marker, InfoWindow } from 'vue3-google-map';
import {computed, onMounted, ref, watch } from "vue";

const map = ref(null)

var directionsService;
var directionsDisplay;

watch(() => map.value?.ready, (ready) => {
  if (!ready) return

  // do something with the api using `mapRef.value.api`
  // or with the map instance using `mapRef.value.map`
  directionsService = new map.value.api.DirectionsService();
  directionsDisplay = new map.value.api.DirectionsRenderer();
  directionsDisplay.setMap(map.value.map);
  Route()
})

const myPosition = ref({lat: 48.141922, lng: 11.558181})

const cars = [{
  s_id: "S_168",
  name: "red BMW",
  position: {
    lat: 48.241922,
    lng: 11.558181
  },
  id: 0,
  addr: "Arnulfstr. 16/18, 80335 München"
},{
  s_id: "S_5254",
  name: "white Tesla",
  position: {
    lat: 48.140033,
    lng: 11.566841
  },
  id: 1,
  addr: "Karlsplatz 3, 80335 München"
}];
const center = { lat: 48.145, lng: 11.550 }

const carIcon = "src/assets/c_pin.png"

const getCarInfo = (marker) => {
  const info = `<p><b>Car to pick up</b></p>
                ${marker.name}<br>
                ${marker.addr}<br>
                <div class="rounded-lg bg-black text-white p-2 font-bold mt-2 hover:cursor-pointer">Pick up and drive!</div>`
  return info
}


const Route = () => {
  console.log("called route")
  var start = new map.value.api.LatLng(48.141922, 11.558181);
  var end = new map.value.api.LatLng(48.140033, 11.566841);
  var request = {
    origin: start,
    destination: end,
    travelMode: map.value.api.TravelMode.TRANSIT
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
</script>

<template>
  <div class="bg-red-500 h-full">

    <div class="h-full">
      <GoogleMap ref="map"
                 api-key="AIzaSyCDzbtVQ0VGI-EaoCJat7kdT_vLAeSCcD4"
                 style="width: 100%; height: 100%;"
                 :center="center"
                 :zoom="10"
      >
        <template v-for="marker in cars">
          <Marker :options='{ position: marker.position, icon: carIcon }'>
            <InfoWindow :options="{ position: marker.position, content: getCarInfo(marker)}" />
          </Marker>
        </template>
      </GoogleMap>
    </div>
  </div>
</template>