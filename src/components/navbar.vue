<template><div class="contain">
  <div class="title">观云图志——以多彩数据，绘中国气象</div>
  <div class="nv"><img src="../assets/bav.svg" alt="SVG" /></div>
  <router-link to="/p1" class="bu1">主页</router-link>
  <router-link to="/p2" class="bu2">地区简报</router-link>
  <router-link to="/p3" class="bu3">极端天气</router-link>
  </div>


</template>
  
  <script>
</script>
<style scoped>
.contain{
  height:0.55rem;
}
a {
  text-decoration: none;
  color: #fff;
}
.title{
  /* 观云图志——以多彩数据，绘中国气象 */

position: absolute;
width: 430px;
height: 33px;
left: 49px;
top: 15px;

font-family: 'Microsoft YaHei';
font-style: normal;
font-weight: 700;
font-size: 25px;
line-height: 33px;
/* identical to box height */
color: #FFFFFF;
}

.nv{

/* Group 427322773 */
position: absolute;
width: 42.5px;
height: 17.5px;
left: 500px;
top: 25px;
}
.bu1 {
  /* 继承原有样式 */
  box-sizing: border-box;
  position: absolute;
  width: 134px;
  height: 32px;
  left: 1400px;
  top: 20px;
  border-radius: 47px;
  
  /* 新增样式 */
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.8); /* 半透明背景 */
  color: white; /* 文字颜色 */
  font-size: 15px; /* 字体大小，根据实际需要调整 */
  text-decoration: none; /* 去除下划线 */
  transition: background-color 0.3s ease; /* 平滑过渡效果 */
  font-family: 'Microsoft YaHei';
  font-style: normal;
  
  /* 渐变边框 */
  border: 1px solid transparent; /* 渐变边框基础 */
  background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), /* 内部背景 */
                    linear-gradient(to right, #67E0FF, black); /* 渐变色边框 */
  background-origin: border-box; /* 内部背景基于边框框 */
  background-clip: content-box, border-box; /* 切割背景到内容和边框 */
}

.bu1:hover {
  background-image: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.2)), /* 鼠标悬停时的背景颜色 */
                    linear-gradient(to right, #67E0FF, black); /* 维持渐变色边框 */
}

.bu2 {
  /* 继承原有样式 */
  box-sizing: border-box;
  position: absolute;
  width: 134px;
  height: 32px;
  left: 1550px;
  top: 20px;
  border-radius: 47px;
  
  /* 新增样式 */
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.8); /* 半透明背景 */
  color: white; /* 文字颜色 */
  font-size: 15px; /* 字体大小，根据实际需要调整 */
  text-decoration: none; /* 去除下划线 */
  transition: background-color 0.3s ease; /* 平滑过渡效果 */
  font-family: 'Microsoft YaHei';
  font-style: normal;
  
  /* 渐变边框 */
  border: 1px solid transparent; /* 渐变边框基础 */
  background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), /* 内部背景 */
                    linear-gradient(to right, #67E0FF, black); /* 渐变色边框 */
  background-origin: border-box; /* 内部背景基于边框框 */
  background-clip: content-box, border-box; /* 切割背景到内容和边框 */
}

.bu2:hover {
  background-image: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.2)), /* 鼠标悬停时的背景颜色 */
                    linear-gradient(to right, #67E0FF, black); /* 维持渐变色边框 */
}

.bu3 {
  /* 继承原有样式 */
  box-sizing: border-box;
  position: absolute;
  width: 134px;
  height: 32px;
  left: 1700px;
  top: 20px;
  border-radius: 47px;
  
  /* 新增样式 */
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.8); /* 半透明背景 */
  color: white; /* 文字颜色 */
  font-size: 15px; /* 字体大小，根据实际需要调整 */
  text-decoration: none; /* 去除下划线 */
  transition: background-color 0.3s ease; /* 平滑过渡效果 */
  font-family: 'Microsoft YaHei';
  font-style: normal;
  
  /* 渐变边框 */
  border: 1px solid transparent; /* 渐变边框基础 */
  background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), /* 内部背景 */
                    linear-gradient(to right, #67E0FF, black); /* 渐变色边框 */
  background-origin: border-box; /* 内部背景基于边框框 */
  background-clip: content-box, border-box; /* 切割背景到内容和边框 */
}

.bu3:hover {
  background-image: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.2)), /* 鼠标悬停时的背景颜色 */
                    linear-gradient(to right, #67E0FF, black); /* 维持渐变色边框 */
}

.router-link-active {
  /* 继承原有样式 */
  text-decoration: none;
}


</style>