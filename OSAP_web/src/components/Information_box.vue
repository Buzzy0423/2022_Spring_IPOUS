<template>
  <el-card
      id="CT_image_1"
      class="information"
      style="border-radius: 8px"
  >
    <el-button type="primary" class="edit_button" @click="changeHint()">
      {{ hint ? '编辑信息' : '确认信息' }}
    </el-button>
  </el-card>
</template>

<script>
export default {
  name: "Information_box"

}
const app = {
  data(){
  },
  methods:{
    changeHint(){
      hint = !hint
    }
  }
}
</script>

<style scoped>
.information {
  height: 400px;
  width: 800px;
  position: relative;
  top: 40px;
  left: 180px;
}

.edit_button {
  position: relative;
  top: 320px;
}
</style>