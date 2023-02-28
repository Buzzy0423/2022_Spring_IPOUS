<script setup lang="ts">
import {toggleDark} from '~/composables';
import {useDark} from '@vueuse/core'
const isDark = useDark()
</script>

<template>
  <el-menu default-active="content" :router="true" class="el-menu-demo" mode="horizontal">
    <el-menu-item index="/content">白内障患者眼底影像增强系统</el-menu-item>
    <el-menu-item index="/team">团队介绍</el-menu-item>
    <el-menu-item>
      <div class="toggle" @click.stop="toggleDark()">
        <button class="border-none w-full bg-transparent cursor-pointer" style="height: var(--ep-menu-item-height);">
          <i inline-flex i="dark:ep-moon ep-sunny" />
        </button>
      </div>
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

