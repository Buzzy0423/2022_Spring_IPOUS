<script lang="ts" setup>
import {toggleDark} from '~/composables';
</script>

<!-- 顶部菜单栏，需要加网站标题，不知道加哪-->

<template>
  <el-menu class="el-menu-demo" mode="horizontal">
    <div class="logo_image">
      <a href="http://www.imed-lab.com/">
        <el-image src='src/assets/logo.png' style="width: 128px; height: 39px" fit="fill"/>
      </a>
    </div>
    <el-menu-item index="1">首页</el-menu-item>
    <el-menu-item index="2">功能</el-menu-item>
    <el-menu-item index="3">团队介绍</el-menu-item>
    <el-menu-item h="full" @click="toggleDark()">
      <button class="border-none w-full bg-transparent cursor-pointer" style="height: var(--ep-menu-item-height);">
        <i inline-flex i="dark:ep-moon ep-sunny"/>
      </button>
    </el-menu-item>
  </el-menu>
</template>

<style>
.logo_image {
  padding-top: 6px;
  padding-left: 15px;
  padding-right: 15px;
}
</style>