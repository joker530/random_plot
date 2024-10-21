document.getElementById("generate-button").addEventListener("click", function() {
    fetch('/generate_plot')
        .then(response => response.json())   // 这是一个Promise方法，这里的response就是/generate_plot的源码字符，需要把字符串格式转换为json数据格式
        .then(data => {
            const img = document.createElement('img');
            img.src = data.image_url;
            img.alt = 'Random Plot';
            let oldImg = document.body.querySelector('img'); // 选择第一个 img 元素
            if (oldImg) {
                document.body.removeChild(oldImg); // 移除旧的 img 元素
            }
            document.body.appendChild(img);
        })
        .catch(error => console.error('Error:', error));
});