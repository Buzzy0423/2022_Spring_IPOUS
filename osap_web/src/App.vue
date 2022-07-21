<template>
  <div class="logo" style="float: left">
    <img alt="IMED logo" src="./assets/logo.png" width="128" height="39">
  </div>

  <br/>

  <MainMenu></MainMenu>
</template>

<script>
import MainMenu from './components/Main-Menu'

export default {
  name: 'App',
  components: {
    MainMenu
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.logo {
  position: relative;
  left: 0%;
  top: 0%;
}
</style>
