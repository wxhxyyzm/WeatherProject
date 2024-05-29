<template>
  <div class="main">
    <el-menu
      v-if="showMenu"
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#000"
      active-text-color="#67e0ff"
      style="height: 0.7rem; background-color: white; display: flex"
      :router="true"
    >
      <div class="title">观云图志—以多彩数据，绘中国气象</div>
      <el-menu-item index="/home">主页&nbsp;</el-menu-item>
      <el-menu-item index="/p2">地区简报</el-menu-item>
      <el-menu-item index="/p3">极端天气</el-menu-item>
      <el-menu-item index="/p4">天气预测</el-menu-item>
      <el-menu-item index="/pz">个人中心</el-menu-item>
    </el-menu>
  </div>
</template>
  
  
  <script>
// beforeRouteEnter(to, from, next) {
//   next((vm) => {
//     vm.loadData();
//   });
// },
// beforeRouteUpdate(to, from, next) {
//   this.loadData();
//   next();
// },
// methods: {
//   loadData() {
//     // 加载数据的逻辑
//   },
// },
export default {
  data() {
    return {
      showMenu: false,
      activeIndex: "", // Set the default active index
    };
  },
  mounted() {
    this.showMenu = true; // Show the navigation menu once the component is mounted
  },
  methods: {
    handleSelect(index) {
      this.activeIndex = index; // Update the active index when a menu item is selected
    },
  },
};
</script>
  
  
  <script>
</script>

<style scoped >
.main {
  justify-content: center;
}
.title {
  margin-top: 0.12rem;
  /* border: 1px solid white; */
  font-family: "Microsoft YaHei";
  font-style: normal;
  font-weight: 800;
  font-size: 0.3rem;
  color: #000;
  margin-left: 0.5rem;
  margin-right: 0.5rem;
}

.router-link-active {
  text-decoration: none;
}

.personal-center {
  margin-left: auto;
}
</style>

