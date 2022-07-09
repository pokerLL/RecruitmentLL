import {
    createRouter,
    createWebHashHistory,
} from "vue-router"

import JobHome from "../pages/jobHome.vue"
import JobDeatil from "../pages/jobDetail.vue"
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
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router