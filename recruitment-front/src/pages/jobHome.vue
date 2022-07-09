<template>
    <job-card v-for="item in joblist" :key="item[0]" :jobid="item[0]" :jobtitle="item[1]" :jobcity="item[2]"></job-card>
</template>

<script setup>
import { computed } from '@vue/runtime-core';
import jobCard from '../components/job/jobCard.vue';

// joblist = [
//     [0,"C++程序员","北京"],
//     [1,"C程序员","上海"],
//     [2,"Java程序员","深圳"],
//     [3,"Python程序员","广州"],
//     [4,"Go程序员","纽约"],
//     [5,"Ruby程序员","东京"],
// ]

let joblist = computed(()=>[
    [0,"C++程序员","北京"],
    [1,"C程序员","上海"],
    [2,"Java程序员","深圳"],
    [3,"Python程序员","广州"],
    [4,"Go程序员","纽约"],
    [5,"Ruby程序员","东京"],
])

</script>

<style lang="sass">

</style>
