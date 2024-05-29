<template>
  <div class="p3body">
    <navbar />
    <div class="container">
      <div class="incontainer">
        <div class="left">
          <div class="areaselect">
            <el-cascader
              class="inline-item"
              size="small"
              :options="options"
              v-model="selectedOptions"
              @change="handleChange"
              placeholder="杭州市"
            >
            </el-cascader>
            <el-button class="inline-item" round>
              <router-link to="/p42" class="router-link">
                <span class="link-text">点击查询</span>
              </router-link>
            </el-button>
          </div>
          <cnmap></cnmap>
        </div>
        <div class="right">
          <div class="qixiangzhan">
            <img src="../assets/qixiang.svg" alt="SVG" width="10%" />
            <div class="picqx">
              <div class="name">气象站：58457099999</div>
            </div>
          </div>
          <div class="grid-container">
            <div class="grid-item">
              <item1></item1>
            </div>
            <div class="grid-item"><item2></item2></div>
            <div class="grid-item"><item3></item3></div>
            <div class="grid-item"><item4></item4></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import cnmap from "@/components/cnmap3.vue";
import navbar from "@/components/navbar.vue";
import item1 from "@/components/p4-item1.vue";
import item2 from "@/components/p4-item2.vue";
import item3 from "@/components/p4-item3.vue";
import item4 from "@/components/p4-item4.vue";
import axios from "axios";
import bus from "./eventBus.js";
import { provinceAndCityData } from "element-china-area-data";
export default {
  components: {
    cnmap,
    navbar,
    item1,
    item2,
    item3,
    item4,
  },
  data() {
    return {
      options: provinceAndCityData,
      selectedOptions: [],
    };
  },
};
</script>

<style scoped>
.p3body {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url("../assets/p4bg.svg");
  background-size: cover;
  overflow: hidden;
}
.container {
  height: auto;
  display: flex;
  flex-wrap: wrap;
  margin: 0.125rem;
}

.incontainer {
  display: grid;
  grid-template-columns: 4fr 6fr; /* 定义五列布局，'nv'占用两倍空间 */
  gap: 8px; /* 格子之间的间隔 */
  align-items: center; /* 中心对齐 */
  justify-content: center; /* 中心对齐 */
  height: auto; /* 高度自适应 */
  /* border: 1px solid white; */
}
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 5px;
  height: 8rem;
}

.grid-item {
  padding: 10px;
  text-align: center;
}
.left {
  margin: 1rem;
  margin-top: -0.1rem;
}
.right {
  margin-top: -1.5rem;
  margin-left: -1.5rem;
}
.qixiangzhan {
  display: flex; /* 使用Flexbox布局 */
  align-items: center; /* 使子项在垂直方向上居中对齐 */
  padding: 0.2rem;
}
.picqx {
  box-sizing: border-box;
  padding: 10px; /* 根据需要调整内边距，使文本有足够的空间 */
  margin-left: 20px; /* 和图片保持一定距离 */
  background: linear-gradient(
    78.67deg,
    rgba(103, 204, 255, 0.6) -80.13%,
    /* 更亮的蓝色，减小绿色分量使其更靠近纯蓝 */ rgba(103, 224, 255, 0) 80.78%
  );
  border-radius: 14.1308px;
  /* 可能需要更多样式来调整文本的外观 */
  /* 设置最小宽度和高度以确保盒子的可见性 */
  min-width: 100px; /* 或根据实际内容调整 */
  min-height: 50px; /* 或根据实际内容调整 */
  display: flex;
  align-items: center; /* 垂直居中文本 */
  justify-content: center; /* 水平居中文本 */
}
.name {
  font-family: "Microsoft YaHei";
  font-style: normal;
  font-weight: 700;
  font-size: 17.6635px;
  line-height: 23px;
  color: #ffffff;
}
.areaselect {
  padding: 0.2rem;
}
.router-link {
  text-decoration: none;
  color: inherit;
}

.link-text {
  text-decoration: none;
  color: inherit;
}

/* */
</style>
