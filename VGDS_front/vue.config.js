module.exports = {
  lintOnSave: false,
  publicPath: '/vgds/', // 配置基本路径
  outputDir: 'vgds', // 构建时的输出目录 不能改
  devServer: {
    open: true,
    host: 'localhost',
    port: 8080,
    https: false,
    // 以上的ip和端口是我们本机的;下面为需要跨域的
    /* proxy: { // 配置跨域
      '/api': {
        target: 'https://bit.zust.edu.cn:6905', // 这里后台的地址模拟的;应该填写你们真实的后台接口
        ws: true, // 是否启用websockets:在WebSocket API中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，轮询
        changOrigin: true // 允许跨域
      } */
    /* proxy: { // 配置跨域
      '/api': {
        target: 'http://172.18.45.221:5000', // 这里后台的地址模拟的;应该填写你们真实的后台接口
        ws: true, // 是否启用websockets:在WebSocket API中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，轮询
        changOrigin: true // 允许跨域
      }
    } */
    // 本机
    proxy: { // 配置跨域
      '/api': {
        target: 'http://127.0.0.1:5000', // 这里后台的地址模拟的;应该填写你们真实的后台接口
        ws: true, // 是否启用websockets:在WebSocket API中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，轮询
        changOrigin: true // 允许跨域
      }
    }
    // //本地服务器
    // proxy: { // 配置跨域
    //   '/api': {
    //     target: 'http://172.18.45.179:5000', // 这里后台的地址模拟的;应该填写你们真实的后台接口
    //     ws: true, // 是否启用websockets:在WebSocket API中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，轮询
    //     changOrigin: true // 允许跨域
    //   }
    // }

    /*proxy: { // 配置跨域
      '/api': {
        target: 'https://bit.zust.edu.cn:6905', // 这里后台的地址模拟的;应该填写你们真实的后台接口
        ws: true, // 是否启用websockets:在WebSocket API中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，轮询
        changOrigin: true // 允许跨域
      }
    }*/
  }
}
