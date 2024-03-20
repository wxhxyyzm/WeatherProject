<template>
  <div class="container">
    <!-- 左侧按钮 -->
    <img
      src="~@/assets/button1.png"
      @click="previousComponent"
      class="button-left"
    />

    <!-- 显示当前选中的组件 -->
    <component :is="getSelectedComponent()" class="content" />

    <!-- 右侧按钮 -->
    <img
      src="~@/assets/button2.png"
      @click="previousComponent"
      class="button-right"
    />
  </div>
</template>

<script>
import item1 from "@/components/p3-item1.vue";
import item2 from "@/components/p3-item2.vue";
import item3 from "@/components/p3-item3.vue";

export default {
  components: {
    item1,
    item2,
    item3,
  },
  data() {
    return {
      components: [item1, item2, item3], // 所有的组件列表
      currentIndex: 0, // 当前选中组件的索引
    };
  },
  methods: {
    getSelectedComponent() {
      return this.components[this.currentIndex]; // 返回选中的组件
    },
    previousComponent() {
      // 切换到上一个组件
      this.currentIndex =
        (this.currentIndex - 1 + this.components.length) %
        this.components.length;
    },
    nextComponent() {
      // 切换到下一个组件
      this.currentIndex = (this.currentIndex + 1) % this.components.length;
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
}

.button-left,
.button-right {
  flex: 1;
  padding: 10px;
  border: none;
  cursor: pointer;
  height: 5rem; /* 调整按钮的高度 */
}

.content {
  flex: 11;
  margin: 0 10px;
}
</style>
