<template>

  <div class="image_upload">
    <el-card style="border-radius: 8px; width: 100%">
      <template #header>
        <span style="margin-left: -86%; font-weight: bold">眼底图片上传</span>
      </template>
      <el-upload
          v-if="!loading"
          v-model:file-list="fileList"
          class="upload_box"
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
      <div class="loading_bar" v-if="loading">
        <h3>正在增强图像，请稍等。。。</h3>
        <el-progress
            v-if="loading"
            :stroke-width="12"
            show-text="show-text"
            :percentage="percentage"
            :status="percentage === 100 ? 'success' : undefined"/>
      </div>
    </el-card>
  </div>

  <div>

  </div>

  <div style=" padding: 15px" class="record">
    <!--  题目-->
    <div style="margin: 15px">
      模型选择
    </div>
    <div style="margin: 15px">
      <el-select v-model="model" placeholder="选择模型" class="select">
        <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
      </el-select>
    </div>
    <el-button type="primary" :disabled="fileList.length < 1 || model === ''" @click="uploadImage">
      上传图片
    </el-button>
    <!--  题目-->
    <div style="margin: 15px">
      处理记录
    </div>
    <!--  功能区-->
    <el-table :data="tableData">
      <el-table-column fixed prop="date" label="上传时间" align="center" header-align="center"/>
      <el-table-column prop="model" label="模型" align="center" header-align="center"/>
      <el-table-column prop="name" label="图片名" align="center" header-align="center"/>
      <el-table-column prop="raw_image" label="原始图像" align="center" header-align="center">
        <template #default="scope">
          <el-image :src="scope.row.raw_image"
                    :preview-src-list="[scope.row.raw_image]" preview-teleported="true">
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
        </template>
      </el-table-column>
      <el-table-column prop="processed_image" label="结果预览" align="center" header-align="center">
        <template #default="scope">
          <el-image :src="scope.row.processed_image"
                    :preview-src-list="[scope.row.processed_image]" preview-teleported="true">
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
        </template>
      </el-table-column>
      <el-table-column fixed="right" label="操作" align="center" header-align="center">
        <template #default="scope">
          <el-button type="primary" @click="download(scope.row.real_name)">下载</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog v-model="dialogVisible" title="记录">
      记录
      <el-button link type="primary" size="small" @click="certainInR">

      </el-button>
    </el-dialog>

  </div>
</template>

<script>
import {ref} from "vue";
import {ElMessage, ElMessageBox} from 'element-plus'
import axios from "axios";

axios.defaults.baseURL = 'http://127.0.0.1:5003'


export default {
  data() {
    return {
      indeterminate: true,
      show_text: false,
      interval: '',
      isUploading: false,
      starttime: 0,
      currenttime: 0,
      averagetime: 4500,
      percentage: 0,
      model: '',
      fileList: [],
      nowtime: '',
      dialogVisible: false,
      loading: false,
      resCount: 0,
      resNum: 0,
      options: [
        {
          value: 'ArcNet',
          label: 'ArcNet',
        },
        {
          value: 'RCDG_model',
          label: 'RCDG_model',
        }
      ],
      tableData: [],
      Filename: ''
    }
  },
  methods: {
    findPercentage() {
      this.currenttime += 500
      console.log(this.currenttime)
      if (this.resNum === this.resCount) {
        this.percentage = 100
      }
      if ((Math.floor(this.currenttime - this.starttime) / (this.averagetime * this.resCount)) >= 1) {
        this.percentage = 99
      } else {
        this.percentage = Math.floor((this.currenttime - this.starttime) / (this.averagetime * this.resCount) * 100)
      }
    },
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
    load(filename, raw_image, model_name) {
      axios.get("show/" + filename, {responseType: "blob"}).then(res => {
        this.resNum += 1
        console.log(this.resNum + " " + this.resCount)
        if (this.resNum === this.resCount) {
          this.loading = false
          this.resNum = 0
          clearInterval(this.interval)
          this.percentage = 0
          this.currenttime = 0
        }
        console.log(this.starttime)
        console.log(this.currenttime)
        let year = new Date().getFullYear()
        let month = new Date().getMonth() + 1
        let day = new Date().getDate()
        month = month < 10 ? '0' + month : month
        day = day < 10 ? '0' + day : day
        let hour = new Date().getHours()
        let minuite = new Date().getMinutes()
        hour = hour < 10 ? '0' + hour : hour
        minuite = minuite < 10 ? '0' + minuite : minuite
        this.nowtime = year + '/' + month + '/' + day + '  ' + hour + ':' + minuite
        if (res.status === 200) {
          const im = window.URL.createObjectURL(res.data)
          console.log(res);
          this.tableData.push(
              {
                date: this.nowtime,
                model: model_name,
                real_name: filename,
                name: "case_" + filename.replace(/\.[^/.]+$/, ''),
                processed_image: im,
                raw_image: raw_image
              }
          )
        }
      })
    },
    async uploadImage() {
      this.starttime = 0
      this.loading = true
      this.resCount = this.fileList.length
      this.interval = setInterval(this.findPercentage, 500)

      for (let file of this.fileList) {
        try {
          let fileParam = new FormData();
          fileParam.append("file", file["raw"]);
          fileParam.append("fileName", file["name"]);
          await axios.post('upload/' + this.model, fileParam).then(
              (response) => {
                let raw_image = window.URL.createObjectURL(file["raw"])
                this.load(response.data.filename, raw_image, this.model)
              }
          )
        } catch (e) {
        }
      }
      this.fileList = []
    },
    download(filename) {
      try {
        axios.get("download/" + filename, {responseType: "blob"}).then(res => {
          const url = window.URL.createObjectURL(res.data)
          let link = document.createElement("a");
          link.style.display = "none";
          link.href = url;
          link.setAttribute("download", filename);
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
          window.URL.revokeObjectURL(url);
          if (res.status === 200) {
            ElMessage.success("下载成功")
          } else {
            ElMessage.error("下载失败，请重试")
          }
        })
      } catch (e) {
        ElMessage.error("下载失败，请重试")
      }
    }
  }
}
</script>

<style scoped>
.image_upload {
  width: 80%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 8%;
}

.record {
  width: 80%;
  margin-left: 8%;
}

.upload_box {
  display: v-bind(upload_display);
}

.loading_bar {
  display: v-bind(loading_display);
  margin-top: 10%;
  margin-bottom: 5%;
}

</style>