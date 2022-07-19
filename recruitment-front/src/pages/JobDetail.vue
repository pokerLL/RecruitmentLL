<template>
  <!-- <p>当前JobId为<b>{{id}}</b></p> -->
  <div>
    <div style="display:none">{{ jobInfo }}</div>
    <el-descriptions :column="1" :size="size" border>
      <el-descriptions-item label="职位名称">{{ jobInfo.job_name }}</el-descriptions-item>
      <el-descriptions-item label="职位类别">{{ jobInfo.job_type.jobtype_name }}</el-descriptions-item>
      <el-descriptions-item label="工作地点">{{ jobInfo.job_city.city_name }}</el-descriptions-item>
      <el-descriptions-item label="职位要求">{{ jobInfo.job_requirement }}</el-descriptions-item>
      <el-descriptions-item label="工作内容">{{ jobInfo.job_responsibility }}</el-descriptions-item>
      <el-descriptions-item label="创建时间">{{ jobInfo.created_date }}</el-descriptions-item>
      <el-descriptions-item label="操作">
        <el-button type="primary" round @click="postResume()">投递简历</el-button>
      </el-descriptions-item>
    </el-descriptions>
  </div>
</template>

<script setup>
import {defineProps, ref} from "vue";
import {getJobInfo} from "../api/job"
import {useRouter} from "vue-router"

let router = useRouter()

let props = defineProps({
  id: String
})

let jobInfo = ref("")

function init_data() {
  getInfo()
}

function getInfo(params) {
  getJobInfo(props.id).then(res => {
    console.log(res)
    jobInfo.value = res[0]
  })
}

init_data()

function postResume(id) {
  router.push({name: 'post'})
}


</script>

<style lang="sass">

</style>
