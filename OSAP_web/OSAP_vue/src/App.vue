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
          <Content class="content"/>
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

.instruction {
  width: 60%;
  height: 45%;
  margin-top: 50%;
  margin-left: 15%;
}

</style>
