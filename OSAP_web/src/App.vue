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
          <info class="info"/>
<!--          <Record class="record"/>-->
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

.info {
  height: 10%;
  width: 70%;
  margin-top: 0%;
  margin-left: 8%;
}

.record {
  height: 10%;
  width: 70%;
  margin-top: 20%;
  margin-left: 8%;
}

.instruction {
  height: 20%;
  width: 70%;
  margin-top: 50%;
  margin-left: 15%;
}

</style>
