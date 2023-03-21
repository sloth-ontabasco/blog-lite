const API_URL = "http://127.0.0.1:8081"
export async function authenticate(userData) {
    let response = await fetch(`${API_URL}/login`,{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        mode: 'cors',
        body: JSON.stringify(userData)
    })
    return response.json()
}

export async function register(userData) {
    let res = await fetch(`${API_URL}/register`,{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(userData)
    })
    return res.json()
}

export function addPost(postData, token) {
    let res =  fetch(`${API_URL}/post`,{
        method: "POST",
        headers: {
            "Authorization": `Bearer: ${token}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(postData)
    })
    return res
}

export function gatherUserHome(token) {
    let res = fetch(`${API_URL}/home`,{
        headers: {
            "Authorization": `Bearer ${token}`
        }
    })
    return res;
}