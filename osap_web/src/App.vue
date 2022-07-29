<template>
  <el-config-provider namespace="ep">
    <BaseHeader/>
    <info class="info"></info>
    <Record/>
  </el-config-provider>
</template>

<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}

.info {
  height: 10%;
  width: 70%;
  margin-top: 2%;
  margin-left: 15%;
}
</style>
