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
                <el-input v-model="objData.form.born_address" />
            </el-form-item>
            <el-form-item label="专业">
                <el-input v-model="objData.form.major" />
            </el-form-item>
            <el-form-item label="学历">
                <el-input v-model="objData.form.degree" />
            </el-form-item>
            <el-form-item label="个人照片">
                <el-upload class="upload-demo" drag
                    action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15" multiple>
                    <el-icon class="el-icon--upload">
                        <upload-filled />
                    </el-icon>
                    <div class="el-upload__text">
                        Drop file here or <em>click to upload</em>
                    </div>
                    <template #tip>
                        <div class="el-upload__tip">
                            jpg/png files with a size less than 500kb
                        </div>
                    </template>
                </el-upload>
            </el-form-item>
            <el-form-item label="简历附件">
                <el-upload drag name="attachment" action="http://127.0.0.1:8000/api/upload/">
                    <el-icon class="el-icon--upload">
                        <upload-filled />
                    </el-icon>
                    <div class="el-upload__text">
                        Drop file here or <em>click to upload</em>
                    </div>
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
import { UploadFilled } from '@element-plus/icons-vue'

// do not use same name with ref
const objData = reactive({
    "form": {
        username: '',
        city_id: '',
        phone: '',
        email: '',
        apply_position_id: '',
        born_address: '',
        gender: '',
        picture: '',
        attachment: '',

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
        born_address: '',
        gender: '',
        picture: '',
        attachment: '',

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
    }).catch(err => {
        console.log(err);
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

const handleExceed = (files, fileList) => {
    if (state.fileList.length >= 1) {
        ElMessage.error('只能上传一个文件')
        return;
    }
}

const picBeforeUpload = (file) => {
    const type = ['image/jpeg', 'image/jpg', 'image/png']
    if (type.indexOf(file.type) === -1) {
        ElMessage.error('上传的文件必须是JPG、JPEG、PNG三种之一!')
        return false
    } else if (file.size / 1024 / 1024 > 2) {
        ElMessage.error('图片大小不能超过2MB!')
        return false
    }
    return true
}


init_data()
</script>



<style lang="sass">

</style>
