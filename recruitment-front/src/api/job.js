import request from "../api/request"

export function getDogNote() {
    return request({
        url: "https://api.oick.cn/dog/api.php",
        method: "GET"
    })
}

export function getJobList() {
    return request({
        url: "http://127.0.0.1:8000/api/job",
        method: "GET"
    })
}

export function getJobInfo(id) {
    return request({
        url: "http://127.0.0.1:8000/api/job/%s".replace("%s", id),
        method: "GET"
    })
}

export function postResume(form) {
    return request({
        url: "http://127.0.0.1:8000/api/resume/",
        method: "POST",
        data: form,
    })
}