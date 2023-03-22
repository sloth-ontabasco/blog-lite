const API_URL = "http://127.0.0.1:8081";

async function authenticate(userData) {
  let response = await fetch(`${API_URL}/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    mode: "cors",
    body: JSON.stringify(userData),
  });
  return response.json();
}
async function register(userData) {
  let res = await fetch(`${API_URL}/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  });
  return res.json();
}
async function addPost(postData, token) {
  console.log("inside add post");
  let res = await fetch(`${API_URL}/api/post`, {
    method: "POST",
    headers: {
      Authorization: `Bearer: ${token}`,
    },
    body: postData,
  });
  console.log(res.status);
  return res.json();
}
async function getHomePage(token) {
  console.log("inside api call");
  let res = await fetch(`${API_URL}/home`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return res.json();
}

export {
    getHomePage,
    addPost,
    authenticate,
    register
}