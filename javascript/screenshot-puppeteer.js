const puppeteer = require('/usr/local/lib/node_modules/puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        headless: true
    });
    const page = await browser.newPage();
    // await page.goto('https://www.zhihu.com/question/22263777');
    await page.goto('https://www.jianshu.com/p/3c5227ccc48a');
    // await page.goto('http://www.iqiyi.com');
    await page.setViewport({
        width: 1200,
        height: 800
    });

    await autoScroll(page);

    // await page.screenshot({
    //     path: '1.png',
    //     fullPage: true
    // });

    await browser.close();
})();


function autoScroll(page) {
    return page.evaluate(() => {
        return new Promise((resolve, reject) => {
            var totalHeight = 0;
            var distance = 100;
            var timer = setInterval(() => {
                var scrollHeight = document.body.scrollHeight;
                window.scrollBy(0, distance);
                totalHeight += distance;
                if (totalHeight >= scrollHeight) {
                    clearInterval(timer);
                    resolve();
                }
            }, 100);
        })
    });
}