<template>
  <el-card class="inst" style="border-radius: 8px" shadow="never">
    <template #header>
      <span style="margin-left: -72%; font-weight: bold">使用指南</span>
    </template>
    <div style="height: 150px; margin-left: 15px; margin-top: 20px">
      <el-steps direction="vertical" active="3">
        <el-step title="上传图像"/>
        <el-step title="选择模型"/>
        <el-step title="等待结果"/>
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