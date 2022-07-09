<template>
<p>当前JobId为<b>{{id}}</b></p>
</template>

<script setup>
import {defineProps,computed} from "vue";
import {useRouter} from "vue-router"
let props  = defineProps({
    id:String
})
</script>

<style lang="sass">

</style>
