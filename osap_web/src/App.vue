<template>
  <el-config-provider namespace="ep">
    <BaseHeader />
    <div class="information_box">
      <Information_box/>
    </div>
    <Record/>
  </el-config-provider>
</template>

<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}

.element-plus-logo {
  width: 50%;
}
</style>
