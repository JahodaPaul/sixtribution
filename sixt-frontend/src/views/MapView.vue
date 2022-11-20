<script setup>
import { GoogleMap, Marker, InfoWindow } from 'vue3-google-map';
import {onMounted, ref, watch} from "vue";
import {useRoute} from 'vue-router'

const route = useRoute()
let zoom = 15
const map = ref(null)

const address = ref(null)
const getAddress = async () => {
  return await fetch('https://maps.googleapis.com/maps/api/geocode/json?address='+
      encodeURIComponent('Brienner Str. 56, 80333 München') + '&key=AIzaSyCDzbtVQ0VGI-EaoCJat7kdT_vLAeSCcD4')
      .then((res) => res.json())
}

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

watch(() => address.value, (addr) => {
  let loc = addr?.results[0].geometry.location
  console.log(addr?.results[0].geometry.location)
  if (loc) {
    center.lat = loc.lat
    center.lng = loc.lng
    zoom = 15
  }
  console.log(center)
})

const myPosition = ref( { lat: 48.1576827, lng: 11.4594431 })


const center =  { lat: 48.1476827, lng: 11.5594431 }

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
},
  {
    name: "Munich Airport (DE)",
    position: {
      lat: 48.353919982910156,
      lng: 11.7872896194458
    },
    addr: "Terminalstr. Mitte/MWZ, 85356 München"
  },
  {
    name: "Munich Pasing Station 24h (DE)",
    position: {
      lat: 48.14899444580078,
      lng: 11.461827278137207
    },
    addr: "Josef-Felder-Str. 53, 81241 München"
  },
  {
    name: "Munich Laim Train Station",
    position: {
      lat: 48.14612579345703,
      lng: 11.503302574157715
    },
    addr: "Wotanstr. 9, 80639 München"
  },
  {
    name: "Munich Sendling ",
    position: {
      lat: 48.11296081542969,
      lng: 11.516751289367676
    },
    addr: "Luise-Kiesselbach-Platz 35, 81377 München"
  },
  {
    name: "Munich/Hotel Bayerischer Hof",
    position: {
      lat: 48.1405029296875,
      lng: 11.573044776916504
    },
    addr: "Promenadenplatz 2-6, 80333 München"
  },
  {
    name: "Munich Schwabing",
    position: {
      lat: 48.17815399169922,
      lng: 11.591404914855957
    },
    addr: "Anni-Albers-Strasse 11, 80807 München"
  },
  {
    name: "Munich/Hotel Westin Grand",
    position: {
      lat: 48.151790618896484,
      lng: 11.61715030670166
    },
    addr: "Arabellapark, Arabellastr. 6, 81925 München"
  },
  {
    name: "Munich/Hotel City Hilton",
    position: {
      lat: 48.13010787963867,
      lng: 11.592764854431152
    },
    addr: "Rosenheimer Str. 15, 81667 München"
  },
  {
    name: "Munich Freiham",
    position: {
      lat: 48.13893508911133,
      lng: 11.411298751831055
    },
    addr: "Hans-Stützle-Str. 20, 81249 München"
  },
  {
    name: "Munich Altstadt-Lehel",
    position: {
      lat: 48.140403747558594,
      lng: 11.584742546081543
    },
    addr: "Seitzstr. 9-11, 80538 München"
  },
  {
    name: "Munich Messestadt Riem",
    position: {
      lat: 48.13224792480469,
      lng: 11.690564155578613
    },
    addr: "Willy-Brandt-Platz 5, 81829 München"
  },
  {
    name: "Munich Giesing",
    position: {
      lat: 48.10932540893555,
      lng: 11.579368591308594
    },
    addr: "Tegernseer Landstr. 163, 81539 München"
  },
  {
    name: "Munich Haidhausen 24h",
    position: {
      lat: 48.136329650878906,
      lng: 11.608949661254883
    },
    addr: "Einsteinstr. 106, 81675 München"
  }];

const markerIcon = "src/assets/s_pin.png"
const chargingIcon = "src/assets/c_pin.png"
const myLocationIcon = "src/assets/my_icon.png"
const myHomeIcon = "src/assets/h_pin.png"

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
  address.value = await getAddress()
});
</script>

<template>
  <div class="h-full">
  <GoogleMap ref="map"
      api-key="AIzaSyCDzbtVQ0VGI-EaoCJat7kdT_vLAeSCcD4"
      style="width: 100%; height: 100%;"
      :center="center"
      :zoom="zoom"
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


    <Marker :options='{ position: myPosition, icon: myLocationIcon }'>
    </Marker>
    <Marker :options='{ position: center, icon: myHomeIcon }'>
    </Marker>
  </GoogleMap>
  </div>
</template>