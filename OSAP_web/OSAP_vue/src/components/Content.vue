<template>
  <div class="image_upload">
    <el-card style="border-radius: 8px" shadow="never">
      <template #header>
        <span style="margin-left: -86%; font-weight: bold">眼底图片上传</span>
      </template>
      <el-upload
          v-model:file-list="fileList"
          class="upload"
          drag
          action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
          multiple
          accept=".jpg, .jpeg, .png, .tiff"
          :limit="5"
          :list-type="'text'"
          :auto-upload="false"
          :on-error="handleUploadError"
          :on-exceed="handleExceed"
          :on-success="handleUploadSuccess"
          :with-credentials="true"
          :on-change="handChange"
      >
        <el-icon class="el-icon--upload" size="50px">
          <upload-filled/>
        </el-icon>
        <div class="el-upload__text">
          拖动图片至此处或点击选择图片
        </div>
        <template #tip>
          <div class="el-upload__tip" style="margin-top: 10px">
            请上传最多五张png文件
          </div>
        </template>
      </el-upload>
    </el-card>
  </div>

  <div>
    <h6>{{this.fileList}}</h6>
  </div>

  <div style=" padding: 15px">
    <!--  题目-->
    <div style="margin: 15px">
      模型选择
    </div>
    <div style="margin: 15px">
      <el-select v-model="label" placeholder="Model" class="m-2">
        <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
      </el-select>
    </div>
    <el-button type="primary" :disabled="fileList.length < 1" @click="uploadImage">
      确定
    </el-button>
    <!--  题目-->
    <div style="margin: 15px">
      处理记录
    </div>
    <!--  功能区-->
    <div style="margin: 15px">
      <el-table :data="tableData" style="width: 100%">
        <el-table-column fixed prop="date" label="日期" width="150"/>
        <el-table-column prop="model" label="模型" width="120"/>
        <el-table-column prop="address" label="记录" sortable width="180" align="center" header-align="center">
          <template #default="scope">
            <el-image style="width: 100%; height: 100px" :src="scope.row.address"
                      :preview-src-list="[scope.row.address]" :key="scope.row.id" preview-teleported="true">
              <div slot="error" class="image-slot">
                <i class="el-icon-picture-outline"></i>
              </div>
            </el-image>
          </template>
        </el-table-column>


        <el-table-column fixed="right" label="操作" width="300">
          <template #default>
            <el-button link type="danger" size="small" @click = "download">下载</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div>
      <el-dialog v-model="dialogVisible" title="记录">
        记录
        <el-button link type="primary" size="small" @click="certainInR">

        </el-button>
      </el-dialog>
    </div>

  </div>
</template>

<script>
import {ElMessage, ElMessageBox} from 'element-plus'
import axios from "axios";
axios.defaults.baseURL = 'http://127.0.0.1:5003'

export default {
  name: "Record",
  data() {
    return {
      fileList: [],
      dialogVisible: false,
      options: [
        {
          value: 'model',
          label: 'model',
        }
      ],
      tableData: [],
      Filename: ''
    }
  },
  methods: {
    handleExceed() {
      ElMessage.warning('一次最多上传五张图片！')
    },
    handleUploadError() {
      ElMessage.error('上传失败！')
    },
    handleUploadSuccess() {
      ElMessage.success('上传成功！')
    },
    handChange(file, fileList) {
      this.fileList = fileList
    },
    checkRecord() {
      this.dialogVisible = true
    },
    certainInR() {
      this.dialogVisible = false
    },
    demo() {
      this.tableData.push(
          {
            date: '2022-7-21',
            model: 'model1',
            address: new URL('../assets/03_gt_dir.png', import.meta.url).href
          }
      )
    },
    load(filename) {
      axios.get("show/"+filename).then(res => {
        if (res) {
          console.log(res);
          this.tableData.push(
              {
                date: "something",
                model: "something",
                image: res.data
              }
          )
        }
      })
    },
    uploadImage() {
      for (let file of this.fileList){
        this.uploadSingle(file);
      }
      this.fileList = []
    },
    download(){
      axios.get("download/<path:file>").then(res =>{
        const remainder = document.createElement("remainder"),
              filename = "something",
              url = window.URL.createObjectURL(res.blob());
        remainder.herf = url;
        remainder.download = filename;
        remainder.click();
        window.URL.revokeObjectURL(url)
      })
    },
    uploadSingle(file){
      let fileParam = new FormData();
      fileParam.append("file", file["raw"]);
      fileParam.append("fileName", file["name"]);
      axios.post('upload/model1',fileParam).then(
          (response) =>{
            console.log(response)
            this.load(file["name"])
          }
      )
    }
  }
}
</script>

<style scoped>


</style>