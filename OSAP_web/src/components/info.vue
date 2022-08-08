<template>
  <el-form :model="formData" ref="vForm" :rules="rules" label-position="left" label-width="80px"
           size="default" @submit.prevent>
    <div class="card-container">
      <el-card style="border-radius: 8px" shadow="never">
        <template #header>
          <span style="margin-left: -94%; font-weight: bold">病人信息</span>
        </template>
        <el-row>
          <el-col :span="11" class="grid-cell">
            <el-form-item label="姓名" prop="name_input">
              <el-input v-model="formData.name_input" size="large" type="text" clearable></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="11" :push="1" class="grid-cell">
            <el-form-item label="性别" prop="sex_select">
              <el-select v-model="formData.sex_select" class="full-width-input" size="large" clearable>
                <el-option v-for="(item, index) in sex_selectOptions" :key="index" :label="item.label"
                           :value="item.value" :disabled="item.disabled"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="11" class="grid-cell">
            <el-form-item label="年龄" prop="age_input">
              <el-input v-model="formData.age_input" size="large" type="text" clearable></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="11" :push="1" class="grid-cell">
            <el-form-item label="联系方式" prop="tel_input">
              <el-input v-model="formData.tel_input" size="large" type="text" clearable></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="15" class="grid-cell">
            <el-form-item label="眼底图片上传" label-width="120px" prop="pic_upload">
              <el-upload :file-list="pic_uploadFileList" :headers="pic_uploadUploadHeaders"
                         :data="pic_uploadUploadData" list-type="picture-card" show-file-list :limit="1">
                <template
                    #default><i class="el-icon-plus"></i></template>
              </el-upload>
            </el-form-item>
          </el-col>
        </el-row>
      </el-card>
    </div>
  </el-form>

</template>

<script>
import {
  defineComponent,
  toRefs,
  reactive,
  getCurrentInstance
}
  from 'vue'

export default defineComponent({
  components: {},
  props: {},
  setup() {
    const state = reactive({
      formData: {
        name_input: "",
        sex_select: "",
        age_input: "",
        tel_input: "",
        pic_upload: null,
      },
      rules: {
        age_input: [{
          pattern: /^\d+(\.\d+)?$/,
          trigger: ['blur', 'change'],
          message: '请输入阿拉伯数字'
        }],
        tel_input: [{
          pattern: /^\d+(\.\d+)?$/,
          trigger: ['blur', 'change'],
          message: '请输入阿拉伯数字'
        }],
      },
      sex_selectOptions: [{
        "label": "男",
        "value": "M"
      }, {
        "label": "女",
        "value": "F"
      }],
      pic_uploadFileList: [],
      pic_uploadUploadHeaders: {},
      pic_uploadUploadData: {},
    })
    const instance = getCurrentInstance()
    const submitForm = () => {
      instance.ctx.$refs['vForm'].validate(valid => {
        if (!valid) return
        //TODO: 提交表单
      })
    }
    const resetForm = () => {
      instance.ctx.$refs['vForm'].resetFields()
    }
    return {
      ...toRefs(state),
      submitForm,
      resetForm
    }
  }
})

</script>

<style lang="scss">
.el-input-number.full-width-input,
.el-cascader.full-width-input {
  width: 100% !important;
}

.el-form-item--medium {
  .el-radio {
    line-height: 36px !important;
  }

  .el-rate {
    margin-top: 8px;
  }
}

.el-form-item--small {
  .el-radio {
    line-height: 32px !important;
  }

  .el-rate {
    margin-top: 6px;
  }
}

.el-form-item--mini {
  .el-radio {
    line-height: 28px !important;
  }

  .el-rate {
    margin-top: 4px;
  }
}

.float-right {
  float: right;
}

</style>

<style lang="scss" scoped>
div.table-container {
  table.table-layout {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;

    td.table-cell {
      display: table-cell;
      height: 36px;
      border: 1px solid #e1e2e3;
    }
  }
}

div.tab-container {
}

.label-left-align :deep(.el-form-item__label) {
  text-align: left;
}

.label-center-align :deep(.el-form-item__label) {
  text-align: center;
}

.label-right-align :deep(.el-form-item__label) {
  text-align: right;
}

.custom-label {
}

.static-content-item {
  min-height: 20px;
  display: flex;
  align-items: center;

  :deep(.el-divider--horizontal) {
    margin: 0;
  }
}

</style>