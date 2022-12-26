<template>
  <el-config-provider namespace="ep">
    <el-container>
      <el-header>
        <BaseHeader/>
      </el-header>
      <el-container>
        <el-aside width="20%">
          <instruction class="instruction"/>
        </el-aside>
        <el-main>
<!--          <Content class="content"/>-->
          <router-view class="main"/>
        </el-main>
      </el-container>
    </el-container>
  </el-config-provider>
</template>

<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}



.main {
  display: flex;
  justify-content: center;
  align-items: center;
}


</style>

<script lang="ts">


export default {
  name : "App",

}
</script>
