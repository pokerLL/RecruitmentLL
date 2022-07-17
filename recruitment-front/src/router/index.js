import {
    createRouter,
    createWebHashHistory,
} from "vue-router"

import JobHome from "../pages/JobHome.vue"
import JobDeatil from "../pages/JobDetail.vue"
import PostResume from "../pages/PostResume.vue"
const routes = [
    {
        path: "/",
        name: "home",
        component: JobHome,
    }, {
        path: "/detail/:id",
        name: "detail",
        component: JobDeatil,
        props:true,
    }, {
        path: "/post",
        name: "post",
        component: PostResume,
        props:true,
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router