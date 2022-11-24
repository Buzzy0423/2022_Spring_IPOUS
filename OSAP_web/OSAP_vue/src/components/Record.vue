<template>

  <div style=" padding: 15px">
    <!--  题目-->
    <div style="margin: 15px">
      模型选择
    </div>
    <div style="margin: 15px">
      <el-select v-model="label" placeholder="Model" class="m-2">
        <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
      </el-select>
    </div>
    <el-button type="primary" @click="demo">
      确定
    </el-button>
    <!--  题目-->
    <div style="margin: 15px">
      处理记录
    </div>
    <!--  功能区-->
    <div style="margin: 15px">
      <el-table :data="tableData" style="width: 100%">
        <el-table-column fixed prop="date" label="日期" width="150"/>
        <el-table-column prop="model" label="模型" width="120"/>
        <el-table-column prop="address" label="记录" sortable width="180" align="center" header-align="center">
          <template #default="scope">
            <el-image style="width: 100%; height: 100px" :src="scope.row.address"
                      :preview-src-list="[scope.row.address]" :key="scope.row.id" preview-teleported="true">
              <div slot="error" class="image-slot">
                <i class="el-icon-picture-outline"></i>
              </div>
            </el-image>
          </template>
        </el-table-column>


        <el-table-column fixed="right" label="操作" width="300">
          <template #default>
            <el-button link type="danger" size="small">下载</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div>
      <el-dialog v-model="dialogVisible" title="记录">
        记录
        <el-button link type="primary" size="small" @click="certainInR">

        </el-button>
      </el-dialog>
    </div>

  </div>

</template>

<script type="module">

export default {
  name: "Record",
  data() {
    return {
      dialogVisible: false,
      options: [
        {
          value: 'model',
          label: 'model',
        }
      ],
      tableData: []
    }
  },
  methods: {
    checkRecord() {
      this.dialogVisible = true
    },
    certainInR() {
      this.dialogVisible = false
    },
    demo() {
      this.tableData.push(
          {
            date: '2022-7-21',
            model: 'model1',
            address: new URL('../assets/03_gt_dir.png', import.meta.url).href
          }
      )
    }
  }
}

</script>

<style scoped>

</style>
