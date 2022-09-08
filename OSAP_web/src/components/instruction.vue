<template>
  <el-card class="inst" style="border-radius: 8px" shadow="never">
    <template #header>
      <span style="margin-left: -72%; font-weight: bold">使用指南</span>
    </template>
    <div style="height: 300px; margin-left: 20px; margin-top: 20px">
      <el-steps direction="vertical" active="3">
        <el-step title="上传图像" description="拖动图像至选择框内或直接选择图像"/>
        <el-step title="选择模型" />
        <el-step title="等待结果" description="服务器性能有限，请耐心等待"/>
      </el-steps>
    </div>
  </el-card>
</template>

<script lang="ts">
export default {
  name: "instruction"
}
</script>

<style scoped>

</style>