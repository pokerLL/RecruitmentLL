<template>
    <div @click="goToDetailPage">{{ jobtitle }} - {{ jobcity }}</div>
</template>

<script setup>

import {defineProps,computed} from "vue";
import {useRouter} from "vue-router"
let router = useRouter()
let props = defineProps({
    jobid: Number,
    jobtitle: String,
    jobcity: String,
})
function goToDetailPage(){
    console.log("goToDetailPage"+props.jobtitle);
    let jid =  props.jobid
    router.push({ name: 'detail', params: { id:jid }})
}
</script>

<style lang="sass">

</style>
