<template>
  <!-- <job-card v-for="item in joblist" :key="item.id" :jobid="item.id" :jobtitle="item.job_name"
          :jobcity="item.job_city.city_name"></job-card> -->
  <div>
    <el-table :data="joblist" height="250" style="width: 100%">
      <el-table-column prop="id" label="序号" width="180"/>
      <el-table-column prop="job_name" label="职位" width="180"/>
      <el-table-column prop="job_type.jobtype_name" label="类型" width="180"/>
      <el-table-column prop="job_city.city_name" label="城市" width="180"/>
      <el-table-column lable="操作" #default="scope">
        <el-button @click="goToDetailPage(scope.row.id)">查看</el-button>
      </el-table-column>
    </el-table>
  </div>

</template>

<script setup>
import {ref} from "vue";
// import jobCard from '../components/job/jobCard.vue';
import {getJobList} from "../api/job"
import {useRouter} from "vue-router"

let router = useRouter()

let joblist = ref([])

function init_data() {
  getList()
}

function getList(params) {
  getJobList().then(res => {
    joblist.value = res
  })
}

function goToDetailPage(jid) {
  // console.log("goToDetailPage"+props.jobtitle);
  router.push({name: 'detail', params: {id: jid}})
}

init_data()

</script>

<style lang="sass">

</style>
