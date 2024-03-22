<template>
  <div class="p3body">
  <navbar />
  <div class="container">
    <div class="left-top">
      <div class="grid-container">
        <div class="grid-item">
          <img
            src="../assets/event.png"
            alt="Image 1"
            @click="displayText(text1)"
          />
          <div class="content">
            <h3>Text 1</h3>
            <p>Content 1</p>
          </div>
        </div>
        <div class="grid-item">
          <img
            src="../assets/event.png"
            alt="Image 2"
            @click="displayText('Text 2')"
          />
        </div>
        <div class="grid-item">
          <img
            src="../assets/event.png"
            alt="Image 3"
            @click="displayText('Text 3')"
          />
        </div>
        <div class="grid-item">
          <img
            src="../assets/event.png"
            alt="Image 4"
            @click="displayText('Text 4')"
          />
        </div>
      </div>
    </div>
    <div class="right-top">


      <div id="text-display">{{ displayedText }}</div>
    </div>
    <div class="left-bottom">      <el-cascader
        class="inline-item2"
        size="small"
        :options="options"
        v-model="selectedOptions"
        @change="handleChange"
      >
      </el-cascader>

      <el-button class="inline-item" round @click="getData">点击查询</el-button><cnmap /></div>
    <div class="right-bottom"><lunbo /></div>
  </div>
</div>
</template>
  
  <script>
import cnmap from "@/components/cnmap.vue";
import lunbo from "@/components/lunbo.vue";
import navbar from "@/components/navbar.vue";
export default {
  components: {
    cnmap,
    lunbo,
    navbar,
  },
  data() {
    return {
      displayedText: "",
      text1:
        "台风是一种热带气旋，属于强烈的旋转性气象系统。它是由海洋表面温暖的水蒸气获得能量，并通过热力和动力机制产生的一个低气压中心。台风在热带海洋上形成并逐渐发展，其特征包括强烈的风力、大量的降水和高度发达的云系。",
    };
  },
  methods: {
    displayText(text) {
      this.displayedText = text;
    },
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
  background: url("../assets/p3bg.svg");
  background-size: cover;
}
.container {
  height: auto;
  display: flex;
  flex-wrap: wrap;
  margin: 10px;
}
.container > div {
  box-sizing: border-box;
  border: 2px solid white;
}
.left-top {
  width: calc(50% - 20px);
  height: 30%;
  border: 2px solid white;
  box-sizing: border-box;
}

.right-top {
  width: calc(50% - 20px);
  height: 70%;
  border: 2px solid white;
  box-sizing: border-box;
}

.left-bottom {
  width: calc(50% - 20px);
  height: 60%;
  border: 2px solid white;
  box-sizing: border-box;
}

.right-bottom {
  width: calc(50% - 20px);
  height: 60%;
  border: 2px solid white;
  box-sizing: border-box;
}
.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 10px;
}

.grid-item {
  position: relative;
}

.grid-item img {
  width: 25vh;
  height: auto;
  cursor: pointer;
  margin: 10px;
  
}

.grid-item .content {
  display: none;
  position: absolute;
  top: 0;
  left: 0;
  width: 20%;
  height: 20%;
  background-color: rgba(0, 0, 0, 0.8);
  color: #fff;
  text-align: center;
  padding: 20px;
  margin: 20px;
}

.grid-item:hover .content {
  display: block;
}

#text-display {
  margin-top: 20px;
  background-color: transparent;
  padding: 10px;
  font-size: 18px;
  font-weight: bold;
  color:red;
}


/* */
</style>