<script setup lang="ts">
import {ref} from "vue";
import {ElMessage} from 'element-plus'

let button_click: boolean = false;

</script>

<template>
  <el-card
      id="information"
      class="information"
      style="border-radius: 8px"
  >
    <div class='patient_info'>
      <p><b>
        病人信息
      </b></p>
    </div>
    <el-button type="primary" class="edit_button" @click="button_click = !button_click">
      {{ button_click ? '编辑信息' : '更改信息' }}
    </el-button>
  </el-card>
</template>

<style scoped>
.information {
  height: 400px;
  width: 1000px;
  position: relative;
  top: 40px;
  left: 220px;
}

.patient_info {
  position: relative;
  right: 420px;
}

.edit_button {
  position: relative;
  top: 260px;
}
</style>