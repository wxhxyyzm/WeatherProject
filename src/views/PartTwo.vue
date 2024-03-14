<template>
  <div>
    <header>
<h1>气候可视化</h1>
    </header>
  </div>
  <section class="container">

<section class="container-top">
<section class="top-left">
  <item><item1/></item>
  <item><item2/></item> 

</section>
<section class="top-mid">
  <cnmap/>
</section>
<section class="top-right">
  <item><item3/></item>
  <item><item4/></item>
</section>
</section>

<section class="container-bottom"></section>
  </section>
</template>

<script>
import item from "@/components/item.vue"
import item1 from "@/components/item1.vue"
import item2 from "@/components/item2.vue"
import item3 from "@/components/item3.vue"
import item4 from "@/components/item4.vue"
import cnmap from "@/components/cnmap.vue"
import { inject } from "vue"

export default {
components:{
item,item1,item2,item3,item4,cnmap
},
setup(){
  let $echarts= inject("echarts")
let $http= inject("axios")
console.log($echarts)
console.log($http)
}

}
</script>

<style>
header{
  height: 0.5rem;
  font-size: 0.25rem;
  line-height: 0.5rem;
  color: rgb(101, 101, 223);
}

.container {
  min-width: 1536px;
  max-width: 2200px;
  margin: 0 auto;
  border: 1px solid red;
  padding: 0.125rem;
  height: 11.4rem;
  display: flex;
  flex-direction: column;
}

.container-top {
  flex: 2;
  display: flex;
}

.container-bottom {
  flex: 1;
}

.top-left,
.top-right {
  flex: 2.5;
  border: 1px solid black;
}

.top-mid {
  flex: 5;
  border: 1px solid black;
}
.mymap{
padding:0.3rem;
margin:0.3rem;
border: 1px solid black;
height:6.5rem;
}
</style>
