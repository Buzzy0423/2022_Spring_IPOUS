<template>
  <el-config-provider namespace="ep">
    <BaseHeader/>
    <info class="info"/>
    <Record class="record"/>
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

.record {
  height: 10%;
  width: 70%;
  margin-top: 0%;
  margin-left: 15%;
}
</style>
