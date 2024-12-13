
const crypto = require('crypto');
const Md5 = require('crypto-js/md5'); // 使用 `crypto-js` 库中的 md5


var v = function() {
    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {},
        n = arguments.length > 1 && void 0 !== arguments[1] && arguments[1],
        t = arguments.length > 2 ? arguments[2] : void 0,
        r = "zZ2EqtxhDk4xZK_U9Gw30vNem_QjyJS33OyNQ-LHKJRIncVD_3R6R3fPhAPZN6ow6Iizy5bLhvA-Ok5dsxZ1QNGQ3iwDE8c7Rs3W0Bf5Ci4VXZYzThtmqFzE1c0F9XffzC1Rbn03_3QSQyaMuy2fBg",
        o = "0B965FC48B3848C5B57DF062ADC09F30";
    r = r ? r.slice(7, r.length) : void 0;
    e.timestamp = Date.parse(new Date) / 1e3;
    n || (e.access_token = r);
    var a = Object.keys(e);
    a.includes("pageIndex") && a.includes("pageSize") && !e.sort && (a.push("sort"),
    e.sort = !1);
    a.sort();
    var i = {};
    a.forEach(function(n) {
        (e[n] || 0 === e[n] || !1 === e[n]) && (i[n] = e[n]);
    });

    const telephones = '18861613634';

// 当前 Unix 时间戳（秒）
const timestamp = Math.floor(Date.now() / 1000);

    // 模板字符串
let template = `customerTypes=116012874979938888848950,116268519059448888067837&mobile={}&pageIndex=1&pageSize=10&sort=false&timestamp={}&key=C9144542C0704926ADC20A6A5AB69687`;

// 替换模板中的 `{}` 占位符
let l = template.replace('{}', telephones).replace('{}', timestamp);
    var s = Md5(l).toString().toUpperCase();  // 直接传入字符串，调用 toString() 获取哈希值，并转换为大写

    result = s;
    console.log(result);
    l = l + "&signature=" + s;
    // ! 去掉&key=xxx
    l = l.replace(/&key=[A-Z0-9]{32}/, '');
    console.log(l);

    return i.signature = s,
    i;
};

v()