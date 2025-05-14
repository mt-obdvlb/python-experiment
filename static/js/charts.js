// 页面图表加载示例，假设使用 Chart.js
window.addEventListener('DOMContentLoaded', function() {
  const plots = document.querySelectorAll('.plot-img');
  plots.forEach(img => {
    // 可添加点击放大、下载等功能
    img.addEventListener('click', () => {
      const src = img.src;
      window.open(src, '_blank');
    });
  });
});