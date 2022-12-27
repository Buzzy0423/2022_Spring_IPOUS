<template>
  <h1 style="color: #3039a1 ;font-size: 50px ; font-family: 微软雅黑; margin-top: -5px; margin-bottom: -5px">
    IMED团队介绍</h1>
  <el-divider/>
  <div style="display: flex">
    <div id="container">
      <div id="left" :style="{ 'background-image':`url(${currentImg})` }">
        <!--      <img :src="currentImg"/>-->
      </div>
      <div id="right">
        <div v-for="imgSrc in imglist" @mouseenter="setCurrent(imgSrc)" :key="imgSrc" class="item">
          <img :src="imgSrc" :style="{opacity: imgSrc === currentImg?0:1}"/>
        </div>
      </div>
    </div>
    <div style="width: 40%">
      <div
          style="width: 100%; padding-left: 50px;margin: 50px 0 ;text-align: left ;font-family: 微软雅黑 ; text-indent: 2em">
        iMED 是智能医疗影像处理Intelligent Medical
        Imaging的简称，iMED团队是由刘江教授于2007年1月创建于新加坡科研局，是一个以专注眼科人工智能的国际化团队，目前由iMED深圳、iMED宁波、iMED新加坡团队组成。
        2007-2016年内iMED新加坡团队从创立1人发展到26余位科学家组成的当时世界上最大的眼科人工智能团队之一，成员包括来自新加坡，中国，马来西亚，德国以及印度的科学家。
        包括现在活跃于眼科人工智能领域的DAMON WONG，许言午，付华柱，段立新，刘慧颖，程骏，JIMMY LEE等。
      </div>
      <div
          style=" width: 100%;padding-left: 50px;margin-top: 20px ;text-align: left ;font-family: 微软雅黑 ; text-indent: 2em">
        2016年3月，刘江教授及其部分iMED新加坡团队核心成员来到中国发展，刘江教授落户宁波/慈溪，本着iMED做大做强的原则，
        仅用3年，在任中国科学院宁波慈溪医工所首任所长的同时，吸引了英国归国的赵一天博士，美国归国的杨建龙博士，
        日本归国的胡衍博士, 新加坡归国的程骏、JIMMY LEE博士等，在医工所重新创建了一个约40人的眼科人工智能研究团队iMED宁波。
      </div>
    </div>
  </div>

  <div
      style="width: 90% ;padding-left: 50px;margin-top: 20px ;text-align: left;font-family: 微软雅黑 ; text-indent: 2em">
    2019年2月，刘江教授来到了中国改革前沿城市深圳，加入了南方科技大学计算机系，开始了iMED的第3次创业。
    本着做精做深的新理念原则创建了iMED 深圳 （https://faculty.sustech.edu.cn/liuj/），iMED深圳团队已经在短短时间形成包括研究助理教授胡衍领导的手术导航团队，
    资深研究学者东田理莎教授领导的眼前节团队，包括缪函霈眼科医生和研究助理教授金日初，博后姜弘羊在内的眼脑联动团队，以及章晓庆博士生领导的跨媒体4个团队。
    形成了包括教授，研究教授，博后，博士，硕士，工程师，实验室科研本科生在内的布局优化的100多人团队。
    与此同时，2022年开始，赵一天研究员正式接手iMED宁波团队（https://imed.nimte.ac.cn/），
    付华柱资深科学家也在新加坡科研局负责继续发展iMED新加坡团队。
    在“团结，专注，坚持”的iMED团队文化凝结下， iMED作为一个整体正在有质量地在眼科人工智能方向持续发展。
  </div>
  <h1 style="color: #3039a1 ;font-size: 50px; font-family: 微软雅黑; margin-top: 50px; margin-bottom: -5px">
    模型介绍</h1>
  <el-divider/>
  <h2 style="color: #3039a1 ;font-size: 30px ; font-family: 微软雅黑 ;">ArcNet</h2>
  <div style="left: 50px; display: flex">
    <img src="../assets/arcnet.png" style="padding-left: 50px;margin-top: 20px;margin-bottom: 20px">
    <div
        style="width: 40%; padding-left: 50px ; margin-top: 20px;margin-bottom: 20px; text-indent: 2em; text-align: left">

      该模型主要由图像生成和领域自适应两个模块组成，其具体结构如左图所示。模型通过在清晰眼底图像上叠加模拟白内障噪声生成配对的图像，解决了现有手术前后配对图像稀缺的问题。
      为了使模型在真实数据集上也能有良好表现，模型加入了领域自适应模块。将真实白内障图片输入共享生成器G，得到增强图像t^,
      将真实白内障增强图t^和模拟白内障增强图 sˆ
      输入辨别器D_d，通过训练使原域逐渐向向目标域靠近。 此模型的性能超越了以往的的增强模型，并在真实场景 下也有良好的表现。
    </div>
  </div>
  <h2 style="color: #3039a1 ;font-size: 30px ; font-family: 微软雅黑 ;">RCDG</h2>
  <div style="left: 50px; display: flex">
    <img src="../assets/rcdg.png" style="padding-left: 50px;margin-top: 20px;margin-bottom: 20px; width: 45%">
    <div
        style="width: 40%; padding-left: 50px ; margin-top: 20px;margin-bottom: 20px; text-indent: 2em; text-align: left">
      该模型通过从清晰的眼底图像模拟白内障患者的眼底 图像来构建训练的源域，并通过随机调整模拟图像的参
      数生成不同风格的模拟图像来覆盖潜在的目标域，实现领域泛化。
      同时将图像的高频成分作为域不变特征，减小域偏移，对齐源域中的各个域，提高模型泛化性能。
      模型的基本结构如图所示。先在清晰图像s上增加模拟白内障噪声生成模拟图像，在提取模拟图像的高频成分。
      通过生成器G_H重建高频成分，最后通过生成器G_R得到恢复后的图像。
    </div>
  </div>
  <h1 style="color: #3039a1 ;font-size: 50px ; font-family: 微软雅黑 ;margin-bottom: -5px">模型参考文献</h1>
  <el-divider/>
  <div style="padding-left: 50px ;text-align: left; font-family: 'Times New Roman'; font-style: italic">
    [1] Li H , Liu H , Hu Y , et al. Restoration Of Cataract Fundus Images Via Unsupervised Domain Adaptation[C]// 2021
    IEEE 18th International Symposium on Biomedical Imaging (ISBI). IEEE, 2021.
  </div>
  <div style="padding-left: 50px ;text-align: left; font-family: 'Times New Roman'; font-style: italic">
    [2] Li H , Liu H , Hu Y , et al. An Annotation-free Restoration Network for Cataractous Fundus Images[J]. 2022.
  </div>
</template>

<script setup lang="ts">
import img1 from '../assets/IMED1.png'
import img2 from '../assets/IMED2.png'
import img3 from '../assets/IMED3.png'
import img4 from '../assets/IMED4.png'
import {ref} from "vue";

const imglist = ref([
  img1,
  img2,
  img3,
  img4,
])
const currentImg = ref(imglist.value[0])

function setCurrent(imgSrc: string) {
  currentImg.value = imgSrc
}
</script>

<style scoped>
#container {
  margin-top: 50px;
  margin-bottom: 20px;
  padding-left: 50px;
  padding-right: 50px;
  width: 500px;
  height: 300px;
  display: flex;
}

#left {
  flex: 3;
  /*background-image: url("../assets/logo.png");*/
  background-position: center;
  background-size: cover;
}

#right {
  flex: 1;
}

.item {
  display: flex;
  flex-direction: column;
  margin: 2px;
  transition: opacity .2s ease-in-out;
}

.item img {
  width: 100%;
  height: 100%;
}

.item:hover {
  opacity: 0;
}
</style>