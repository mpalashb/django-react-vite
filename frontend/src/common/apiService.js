import { CSRF_TOKEN } from "./csrf_token";

async function getJSON(response) {
  if (response.status === 204) return "";
  return response.json();
}

function apiService(endpoint, method, data) {
  const config = {
    method: method || "GET",
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: {
      "content-type": "application/json",
      "X-CSRFTOKEN": CSRF_TOKEN,
    },
  };
  return fetch(endpoint, config)
    .then(getJSON)
    .catch((err) => console.log(err));
}

export { apiService };
