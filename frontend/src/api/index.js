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

async function addPost(token, form) {
    console.log("inside add post");
    let res = await fetch(`${API_URL}/api/post`, {
        headers: {
            "Authorization": `Bearer ${token}`,
            // "Content-Type": "multipart/form-data",
        },
        method: "POST",
        body: form,
    });
    if(res.status != 200) {
        let msg = await res.json()
        throw new Error(msg.error_message)
    }
    return res.json();
}

async function getHomePage(token) {
    console.log("inside api call");
    let res = await fetch(`${API_URL}/api/home`, {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });
    return res.json();
}

async function getPost(token, id) {

    let res = await fetch(`${API_URL}/api/post/${id}`, {
        method: "GET",
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });

    return res.json()
}

async function getLikedUsers(id) {
    let res = await fetch(`${API_URL}/api/post/${id}/like`,{
        method: "GET"
    })

    return res.json()
}

async function getPostComments(id) {
    let res = await fetch(`${API_URL}/api/post/${id}/comment`,{
        method: "GET"
    })

    return res.json()
}

async function getImageURL(url) {
    const res = await fetch(`${API_URL}/static/${url}`)
    if(res.status == 404) throw new Error("Image does not exist")
    const blob = await res.blob()
    return URL.createObjectURL(blob)
}

export {
    getHomePage, addPost,
    authenticate, register,
    getPost, getLikedUsers,
    getPostComments, getImageURL
};
