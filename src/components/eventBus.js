// 导入mitt
import mitt from 'mitt'
// 创建eventBus的实例对象
const bus = mitt()

// 将eventBus的实例对象共享出去
export default bus
