<template>
  <el-form :model="formData" ref="vForm" :rules="rules" label-position="left" label-width="80px"
           size="default" @submit.prevent>
    <el-card
        class="information"
        style="border-radius: 8px"
    >
      <template #header>
        <div class="clear-fix">
          <span style="margin-left: 1%">病人信息</span>
        </div>
      </template>
      <el-row>
        <el-form :inline="true" :model="formInline" class="first_line_info">
          <el-form-item label="姓名">
            <el-input v-model="patient.name" placeholder=""/>
          </el-form-item>
          <el-form-item label="性别">
            <el-select v-model="patient.sex" placeholder="">
              <el-option label="男" value="M"/>
              <el-option label="女" value="F"/>
            </el-select>
          </el-form-item>
        </el-form>
      </el-row>
      <el-row>
        <el-form :inline="true" :model="formInline" class="first_line_info">
          <el-form-item label="年龄">
            <el-input v-model="patient.age" placeholder=""/>
          </el-form-item>
          <el-form-item label="联系方式">
            <el-input v-model="patient.tel" placeholder=""/>
          </el-form-item>
        </el-form>
      </el-row>
      <el-row>
        <el-form-item label="" label-width="0" prop="pictureupload93431" class="small-margin-bottom">
          <el-upload :file-list="pictureupload93431FileList" :headers="pictureupload93431UploadHeaders"
                     :data="pictureupload93431UploadData" list-type="picture-card" show-file-list :limit="1">
            <template #default><i class="el-icon-plus"></i></template>
          </el-upload>
        </el-form-item>
      </el-row>
    </el-card>
  </el-form>
</template>

<style scoped>
.information {
  height: 400px;
  width: 1000px;
  position: relative;
  top: 40px;
  left: 220px;
}

.information_text {
  font-size: large;
  margin-left: 1%;
}
</style>

<script setup lang="ts">
import {reactive, ref} from "vue";
import {ElMessage} from 'element-plus'

const patient = reactive({
  name: '',
  sex: '',
  age: '',
  tel: ''
})

const options = [
  {
    value: '男',
    label: '男'
  },
  {
    value: '女',
    label: '女'
  }
]
</script>