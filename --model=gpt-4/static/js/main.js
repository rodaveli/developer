document.addEventListener("DOMContentLoaded", () => {
  const voterList = document.getElementById("voterList");
  const referralList = document.getElementById("referralList");
  const requestList = document.getElementById("requestList");
  const kanbanView = document.getElementById("kanbanView");
  const mapView = document.getElementById("mapView");

  async function fetchVoters() {
    const response = await fetch("/api/voters");
    const voters = await response.json();
    displayVoters(voters);
  }

  function displayVoters(voters) {
    voterList.innerHTML = "";
    voters.forEach((voter) => {
      const listItem = document.createElement("li");
      listItem.textContent = `${voter.full_name} (${voter.vote_intent})`;
      voterList.appendChild(listItem);
    });
  }

  async function fetchReferrals() {
    const response = await fetch("/api/referrals");
    const referrals = await response.json();
    displayReferrals(referrals);
  }

  function displayReferrals(referrals) {
    referralList.innerHTML = "";
    referrals.forEach((referral) => {
      const listItem = document.createElement("li");
      listItem.textContent = `${referral.referrer_name} -> ${referral.referred_name}`;
      referralList.appendChild(listItem);
    });
  }

  async function fetchRequests() {
    const response = await fetch("/api/requests");
    const requests = await response.json();
    displayRequests(requests);
  }

  function displayRequests(requests) {
    requestList.innerHTML = "";
    kanbanView.innerHTML = "";
    requests.forEach((request) => {
      const listItem = document.createElement("li");
      listItem.textContent = `${request.name} (${request.status})`;
      requestList.appendChild(listItem);

      const kanbanItem = document.createElement("div");
      kanbanItem.textContent = `${request.name} (${request.status})`;
      kanbanItem.classList.add("kanban-item");
      kanbanItem.classList.add(request.status.toLowerCase());
      kanbanView.appendChild(kanbanItem);
    });
  }

  async function fetchMapView() {
    const response = await fetch("/api/map_view");
    const mapViewData = await response.json();
    displayMapView(mapViewData);
  }

  function displayMapView(mapViewData) {
    mapView.innerHTML = "";
    // Add Google Maps API integration and display voters on the map
  }

  fetchVoters();
  fetchReferrals();
  fetchRequests();
  fetchMapView();
});