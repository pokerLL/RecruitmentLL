import request from "../api/request"

export function getCity() {
    return request({
        url: "http://127.0.0.1:8000/api/city/",
        method: "GET"
    })
}
