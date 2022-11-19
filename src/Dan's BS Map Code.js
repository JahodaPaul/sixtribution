// Based on Google Mpas example. Note that the anchor is set to (20,21) to correspond
// to the middle of the S.
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 10,
    center: { lat: 48.155, lng: 11.450 },
  });

  setMarkers(map);
}

// Data for the markers consisting of a name, a LatLng and a zIndex for the
// order in which these markers should display on top of each other.
const sixts = [
  ["S_168", 48.141922, 11.558181, 1],
  ["S_5254", 48.140033, 11.566841, 2],
];

function setMarkers(map) {
  // Adds markers to the map.
  // Marker sizes are expressed as a Size of X,Y where the origin of the image
  // (0,0) is located in the top left of the image.
  // Origins, anchor positions and coordinates of the marker increase in the X
  // direction to the right and in the Y direction down.
  const image = {
    url: "/assets/S.png",
    // This marker is 40 pixels wide by 42 pixels high.
    size: new google.maps.Size(40, 42),
    // The origin for this image is (0, 0).
    origin: new google.maps.Point(0, 0),
    // The anchor for this image is the middle
    anchor: new google.maps.Point(20, 21),
  };
  // Shapes define the clickable region of the icon. The type defines an HTML
  // <area> element 'poly' which traces out a polygon as a series of X,Y points.
  // The final coordinate closes the poly by connecting to the first coordinate.
  const shape = {
    coords: [1, 10, 10, 1, 34, 1, 42, 10, 42, 30, 40, 32, 40, 10, 30, 1],
    type: "poly",
  };

  for (let i = 0; i < sixts.length; i++) {
    const beach = sixts[i];

    new google.maps.Marker({
      position: { lat: beach[1], lng: beach[2] },
      map,
      icon: image,
      shape: shape,
      title: beach[0],
      zIndex: beach[3],
    });
  }
}

window.initMap = initMap;