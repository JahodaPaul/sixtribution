<script setup>
import { GoogleMap, Marker, InfoWindow } from 'vue3-google-map';
import {computed, onMounted, ref, watch } from "vue";
import DummyComponent from "../components/DummyComponent.vue"
import {useRoute} from 'vue-router'

const route = useRoute()

const fleet = ref(null)
onMounted(async () => {
  const res = await fetch('http://131.159.199.176:5000/api/fleet').then((res) => res.json())
  fleet.value = Object.values(res).map(v => JSON.parse(v))
  let v = fleet.value[0]
  console.log(v)
});

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

  // do something with the api using `mapRef.value.api`
  // or with the map instance using `mapRef.value.map`
  directionsService = new map.value.api.DirectionsService();
  directionsDisplay = new map.value.api.DirectionsRenderer();
  directionsDisplay.setMap(map.value.map);

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

const carIcon = "src/assets/w_pin.png"
const myLocationIcon = "src/assets/my_icon.png"

const getCarInfo = (marker) => {
  const info = `<p><b>Car to pick up</b></p>
                <img class="h-[100px]" src="src/assets/cars/a2786d1a61ec2647f210be504202ec10f9fc7999.png"/><br>
                <div class="rounded-lg bg-black text-white p-2 font-bold mt-2 hover:cursor-pointer"
                    onclick="window.location.href = '/driver#lat=${marker.latitude}&lng=${marker.latitude}'">Pick up and drive!</div>`
  return info
}


const Route = (end) => {
  console.log("called route with arguments: ")
  console.log(end)
  //var start = new map.value.api.LatLng(48.141922, 11.558181);
  //var end = new map.value.api.LatLng(48.140033, 11.566841);
  var request = {
    origin: myPosition.value,
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

const setMarkers = () => {
  console.log("setting markers")
  const gMap = map.value.mapRef;
  const marker = new map.value.api.Marker({
    position: center,
    map,
    title: "Uluru (Ayers Rock)",
  });
  console.log(marker)

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
        <template v-for="marker in fleet">
          <Marker :options='{ position: {lat: Number(marker.latitude), lng: Number(marker.longitude)}, icon: carIcon }'>
            <InfoWindow :options="{ position: {lat: Number(marker.latitude), lng: Number(marker.longitude)}, content: getCarInfo(marker)}" />
          </Marker>
        </template>
        <Marker :options='{ position: myPosition, icon: myLocationIcon }'>
        </Marker>
      </GoogleMap>
    </div>
  </div>
</template>