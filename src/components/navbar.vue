<template>
  <div class="menu-wrapper">
    <header>
      <h1>气候可视化</h1>
    </header>
    <div class="el-menu-demo">
      <el-button type="primary" icon="el-icon-search"
        ><router-link to="/p1">pppart1</router-link>
      </el-button>
      <el-button type="primary" icon="el-icon-search" color="#252525"
        ><router-link to="/p2">pppart2</router-link></el-button
      >
      <el-button type="primary" icon="el-icon-search"
        ><router-link to="/p3">pppart3</router-link></el-button
      >
    </div>
  </div>
</template>
  
  <script>
</script>
<style scoped>
a {
  text-decoration: none;
  color: #fff;
}

.router-link-active {
  text-decoration: none;
}
.menu-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: "transparent";
  padding: 2px;
  width: 100%;
}

header {
  height: 0.5rem;
  font-size: 0.25rem;
  line-height: 0.5rem;
  color: rgb(101, 101, 223);
  margin-left: 100px;
}

.el-menu-demo {
  background-color: transparent;
  color: #fff;
  font-size: 16px;
  /* margin-left: auto; */
  margin-left: 1200px;
  margin-right: auto;
}

.el-menu-demo .el-menu-item,
.el-menu-demo .el-submenu .el-menu {
  background-color: transparent;
  color: #fff;
}

.el-menu-demo .el-submenu .el-menu {
  border: none;
}

.el-menu-demo .el-menu-item.is-active {
  color: #ffd04b;
}

.el-menu-demo .el-submenu__title {
  font-size: 16px;
  color: #fff;
}

.el-menu-demo .el-submenu__title:hover {
  color: #ffd04b;
}
</style>