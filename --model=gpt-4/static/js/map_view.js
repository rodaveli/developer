const googleGeocodeApiKey = "AIzaSyDM5zZdZCOfguxHyDESvEhzxVJIOeqmGto";
const googleMapApiKey = "AIzaSyDM5zZdZCOfguxHyDESvEhzxVJIOeqmGto";

let map;
let markers = [];

function initMap() {
  map = new google.maps.Map(document.getElementById("mapView"), {
    center: { lat: 0, lng: 0 },
    zoom: 2,
  });
}

function addMarker(voter) {
  const marker = new google.maps.Marker({
    position: { lat: voter.location.lat, lng: voter.location.lng },
    map: map,
    title: voter.fullName,
  });

  markers.push(marker);
}

function clearMarkers() {
  for (const marker of markers) {
    marker.setMap(null);
  }
  markers = [];
}

function displayVoters(voters) {
  clearMarkers();
  for (const voter of voters) {
    addMarker(voter);
  }
}

async function getVotersInRadius(center, radius) {
  const response = await fetch(`/api/voters?center=${center}&radius=${radius}`);
  const voters = await response.json();
  displayVoters(voters);
}

function filterVoters(filterOptions) {
  // Implement filtering logic based on filterOptions
}

document.getElementById("filterButton").addEventListener("click", () => {
  const filterOptions = {}; // Collect filter options from the UI
  filterVoters(filterOptions);
});