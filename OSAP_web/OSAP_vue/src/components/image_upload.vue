<template>
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
      limit="10"
      accept=".png"
      :list-type="'text'"
      :auto-upload="false"
      :on-exceed="handleExceed"
      :with-credentials="true"
      >
        <el-icon class="el-icon--upload" size="60px"><upload-filled /></el-icon>
        <div class="el-upload__text">
          拖动图片至此处或点击选择图片
        </div>
        <template #tip>
          <div class="el-upload__tip" style="margin-top: 10px">
            请上传最多十张png文件，新选择的文件会覆盖原有文件
            <!--          are there other types?-->
          </div>
        </template>
      </el-upload>
    </el-card>
</template>

<script setup lang="ts">
import {ElMessage, ElMessageBox} from 'element-plus'
import type {UploadProps, UploadUserFile} from 'element-plus'
import {UploadFilled} from '@element-plus/icons-vue'

const handleExceed: UploadProps['onExceed'] = (files, uploadFiles) => {
  ElMessage.warning(
      `The limit is 20, you selected ${files.length} files this time, add up to ${
          files.length + uploadFiles.length
      } totally`
  )
}

</script>

<style scoped>

</style>