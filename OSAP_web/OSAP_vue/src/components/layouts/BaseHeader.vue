<script  setup lang="ts">
import {toggleDark} from '~/composables';
</script>

<!-- 顶部菜单栏，需要加网站标题，不知道加哪-->

<template>
  <el-menu default-active="content" :router="true" class="el-menu-demo" mode="horizontal">
    <div class="logo_image">
      <a href="http://www.imed-lab.com/">
        <el-image src='src/assets/logo.png' style="width: 128px; height: 39px" fit="fill"/>
      </a>
    </div>
    <el-menu-item index="/content">首页</el-menu-item>
    <el-menu-item index="/team">团队介绍</el-menu-item>
  </el-menu>
</template>



<style>
.logo_image {
  padding-top: 6px;
  padding-left: 15px;
  padding-right: 15px;
}
</style>

