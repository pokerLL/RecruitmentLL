<template>
  <div style="width:50%;left: 20%;position: absolute;">
    <el-form :model="form" label-width="120px">
      <el-form-item label="姓名">
        <el-input v-model="objData.form.username" />
      </el-form-item>
      <el-form-item label="性别">
        <el-select v-model="objData.form.gender" placeholder="please select your zone">
          <el-option label="男" value="man" />
          <el-option label="女" value="woman" />
        </el-select>
      </el-form-item>
      <el-form-item label="城市">
        <el-select v-model="objData.form.city_id" placeholder="please select your zone">
          <el-option v-for="city in citylist" :key="city.id" :label="city.city_name" :value="city.id" />
        </el-select>
      </el-form-item>
      <el-form-item label="手机号码">
        <el-input v-model="objData.form.phone" />
      </el-form-item>
      <el-form-item label="邮箱">
        <el-input v-model="objData.form.email" />
      </el-form-item>
      <el-form-item label="应聘职位">
        <el-select v-model="objData.form.apply_position_id" placeholder="please select your zone">
          <el-option v-for="job in joblist" :key="job.id" :label="job.job_name" :value="job.id" />
        </el-select>
      </el-form-item>
      <el-form-item label="生源地">
        <el-input v-model="objData.form.from_address" />
      </el-form-item>
      <el-form-item label="专业">
        <el-input v-model="objData.form.major" />
      </el-form-item>
      <el-form-item label="学历">
        <el-input v-model="objData.form.degree" />
      </el-form-item>
      <el-form-item label="个人照片">
        <el-upload ref="userPicture" action="http://127.0.0.1:3000/api/picture/" :auto-upload="false"
          :on-success="uploadUserPictureSuccess">
          <template #trigger>
            <el-button type="primary">select file</el-button>
          </template>

          <el-button class="ml-3" type="success" @click="uploadUserPicture">
            upload to server
          </el-button>

          <template #tip>
            <div class="el-upload__tip">
              jpg/png files with a size less than 500kb
            </div>
          </template>
        </el-upload>
      </el-form-item>
      <el-form-item label="简历附件">
        <el-upload ref="attachment" action="http://127.0.0.1:3000/api/attachment/" :auto-upload="false"
          :on-success="uploadAttachmentSuccess">
          <template #trigger>
            <el-button type="primary">select file</el-button>
          </template>

          <el-button class="ml-3" type="success" @click="uploadAttachment">
            upload to server
          </el-button>

          <template #tip>
            <div class="el-upload__tip">
              jpg/png files with a size less than 500kb
            </div>
          </template>
        </el-upload>
      </el-form-item>
      <el-form-item label="自我介绍">
        <el-input v-model="objData.form.candidate_introduction" type="textarea" />
      </el-form-item>
      <el-form-item label="工作经历">
        <el-input v-model="objData.form.work_experience" type="textarea" />
      </el-form-item>
      <el-form-item label="项目经历">
        <el-input v-model="objData.form.project_experience" type="textarea" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit()">Submit</el-button>
        <el-button @click="resetForm()">Reset</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { getCity } from '../api/city';
import { getJobList, postResume } from '../api/job';
import { ElMessage } from 'element-plus'
// do not use same name with ref
const objData = reactive({
  "form": {
    username: '',
    city_id: '',
    phone: '',
    email: '',
    apply_position_id: '',
    from_address: '',
    gender: '',
    picture_id: '',
    attachment_id: '',

    major: '',
    degree: '',

    candidate_introduction: '',
    work_experience: '',
    project_experience: '',
  }
})

const resetForm = () => {
  objData.form = {
    username: '',
    city_id: '',
    phone: '',
    email: '',
    apply_position_id: '',
    from_address: '',
    gender: '',
    picture_id: '',
    attachment_id: '',

    major: '',
    degree: '',

    candidate_introduction: '',
    work_experience: '',
    project_experience: '',
  }
}

const onSubmit = () => {
  console.log(objData.form);
  // console.log(JSON.stringify(objData.form));
  let _data = JSON.stringify(objData.form)
  postResume(_data).then(res => {
    console.log(res);
    if (res.id) {
      ElMessage({
        showClose: true,
        message: '简历投递成功',
        type: 'success',
      })
    }else{
      ElMessage({
        showClose: true,
        message: '简历投递失败',
        type: 'warning',
      })
    }
  }).catch(err => {
    console.log(err);
    ElMessage({
        showClose: true,
        message: '简历投递失败',
        type: 'warning',
      })
  })
}


let citylist = ref("")
let joblist = ref("")

function init_data() {
  getCity().then(res => {
    citylist.value = res
  })
  getJobList().then(res => {
    joblist.value = res
  })
}

init_data()

const userPicture = ref("userPicture");
const attachment = ref("attachment");
const uploadUserPicture = () => {
  if (userPicture.value) {
    userPicture.value.submit();
  }
}

const uploadUserPictureSuccess = (res) => {
  console.log(res);
  objData.form.picture_id = res.id;
}

const uploadAttachment = () => {
  if (attachment.value) {
    attachment.value.submit();
  }
}

const uploadAttachmentSuccess = (res) => {
  console.log(res);
  objData.form.attachment_id = res.id;
}

</script>


<style lang="sass">

</style>
