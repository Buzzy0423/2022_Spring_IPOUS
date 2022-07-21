<template>
  <div class="Menu">
    <ul>
      <li><a href="#home">主页</a></li>
      <li><a href="#function">功能</a></li>
      <li><a href="#about">关于</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "MainMenu"
}
</script>

<style scoped>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #3039a1;
  position: relative;
  left: 0%;

}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover {
  background-color: grey;
}

li a.active{
  background-color: #fc6509;
  color: white;
}

</style>