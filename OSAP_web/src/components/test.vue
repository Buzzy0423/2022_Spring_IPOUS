<template>
  <div>
    <el-upload
        class="upload-demo"
        ref="upload"
        :limit="limitNum"
        :class="{hide:hideUploadEdit}"
        :on-remove="handleRemove"
        :on-change="handleEditChange"
        :http-request="handleUpload"
        :before-upload="uploadPreview"
        :with-credentials="true"
        :auto-upload="true"
        accept=".png"
        action=""
        list-type="picture-card"
        :file-list="fileList"
    >
      <i slot="trigger" class="el-icon-plus"></i>
    </el-upload>
    <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hideUploadEdit: false, // 隐藏'上传按钮'
      limitNum: 1, // 图片数量
      fileList: [] // 图片列表
    };
  },
  methods: {
    handleEditChange(file, fileList) {
      this.hideUploadEdit = fileList.length >= this.limitNum;
      console.log("this.fileList:", this.fileList);
      console.log("this.hideUploadEdit:", this.hideUploadEdit);
    },

    uploadPreview(file) {
      const isPNG = /^.png$/.test(file.name.substring(file.name.lastIndexOf('.')));
      const isLt100KB = file.size / 1024  < 100;

      if (!isPNG) {
        this.$message.error("上传图片只能是 PNG 格式!");
        return false;
      }
      if (!isLt100KB) {
        this.$message.error("上传图片大小不能超过 80KB!");
        return false;
      }

      let is80x56 = true;
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = (theFile) => {
        const image = new Image();
        image.src = theFile.target.result;
        image.onload = () => {
          const { width, height } = image;
          if(width !== 80 || height !== 56) {
            this.$message.error("请上传 80*56 px 的图片！");
            is80x56 = false;
          }
        };
      };
      return isPNG && isLt100KB && is80x56;
    },

    handleRemove(file, fileList) {
      if (fileList.length === 0) {
        this.fileList = [];
      } else {
        let dl = this.fileList.indexOf(file);
        this.fileList.splice(dl, 1);
      }
      this.hideUploadEdit = fileList.length >= this.limitNum;
    },

    handleUpload(param) {
      this.param = param;
      // 这里可以进行上传
      // let formData = new FormData(); //formdata格式
      // formData.append("fileName", this.param.file);
      // 将formData 作为 body 上传即可， 有额外的参数可携带
    },

    submitUpload() {
      if (!this.param) {
        this.$message("请选择图片");
      } else {
        let formData = new FormData(); //formdata格式
        formData.append("file", this.param.file);
        // 也可以在这里进行上传
        // let formData = new FormData(); //formdata格式
        // formData.append("fileName", this.param.file);
        // 将formData 作为 body 上传即可， 有额外的参数可携带
      }
    },
  }
};
</script>
<style>
.hide .el-upload--picture-card {
  display: none;
}
.el-upload-list__item {
  transition: none !important;
}
</style>
