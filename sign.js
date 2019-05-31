function i(e, t) {
    var n = (65535 & e) + (65535 & t);
    return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
}
function u(e, t, n, r, o, u) {
    return i(function(e, t) {
        return e << t | e >>> 32 - t
    } (i(i(t, e), i(r, u)), o), n)
}
function a(e, t, n, r, o, i, a) {
    return u(t & n | ~t & r, e, t, o, i, a)
}
function c(e, t, n, r, o, i, a) {
    return u(t & r | n & ~r, e, t, o, i, a)
}
function f(e, t, n, r, o, i, a) {
    return u(t ^ n ^ r, e, t, o, i, a)
}
function s(e, t, n, r, o, i, a) {
    return u(n ^ (t | ~r), e, t, o, i, a)
}
function d(e, t) {
    var n, r, o, u, d;
    e[t >> 5] |= 128 << t % 32,
    e[14 + (t + 64 >>> 9 << 4)] = t;
    var l = 1732584193,
    p = -271733879,
    v = -1732584194,
    g = 271733878;
    for (n = 0; n < e.length; n += 16) r = l,
    o = p,
    u = v,
    d = g,
    p = s(p = s(p = s(p = s(p = f(p = f(p = f(p = f(p = c(p = c(p = c(p = c(p = a(p = a(p = a(p = a(p, v = a(v, g = a(g, l = a(l, p, v, g, e[n], 7, -680876936), p, v, e[n + 1], 12, -389564586), l, p, e[n + 2], 17, 606105819), g, l, e[n + 3], 22, -1044525330), v = a(v, g = a(g, l = a(l, p, v, g, e[n + 4], 7, -176418897), p, v, e[n + 5], 12, 1200080426), l, p, e[n + 6], 17, -1473231341), g, l, e[n + 7], 22, -45705983), v = a(v, g = a(g, l = a(l, p, v, g, e[n + 8], 7, 1770035416), p, v, e[n + 9], 12, -1958414417), l, p, e[n + 10], 17, -42063), g, l, e[n + 11], 22, -1990404162), v = a(v, g = a(g, l = a(l, p, v, g, e[n + 12], 7, 1804603682), p, v, e[n + 13], 12, -40341101), l, p, e[n + 14], 17, -1502002290), g, l, e[n + 15], 22, 1236535329), v = c(v, g = c(g, l = c(l, p, v, g, e[n + 1], 5, -165796510), p, v, e[n + 6], 9, -1069501632), l, p, e[n + 11], 14, 643717713), g, l, e[n], 20, -373897302), v = c(v, g = c(g, l = c(l, p, v, g, e[n + 5], 5, -701558691), p, v, e[n + 10], 9, 38016083), l, p, e[n + 15], 14, -660478335), g, l, e[n + 4], 20, -405537848), v = c(v, g = c(g, l = c(l, p, v, g, e[n + 9], 5, 568446438), p, v, e[n + 14], 9, -1019803690), l, p, e[n + 3], 14, -187363961), g, l, e[n + 8], 20, 1163531501), v = c(v, g = c(g, l = c(l, p, v, g, e[n + 13], 5, -1444681467), p, v, e[n + 2], 9, -51403784), l, p, e[n + 7], 14, 1735328473), g, l, e[n + 12], 20, -1926607734), v = f(v, g = f(g, l = f(l, p, v, g, e[n + 5], 4, -378558), p, v, e[n + 8], 11, -2022574463), l, p, e[n + 11], 16, 1839030562), g, l, e[n + 14], 23, -35309556), v = f(v, g = f(g, l = f(l, p, v, g, e[n + 1], 4, -1530992060), p, v, e[n + 4], 11, 1272893353), l, p, e[n + 7], 16, -155497632), g, l, e[n + 10], 23, -1094730640), v = f(v, g = f(g, l = f(l, p, v, g, e[n + 13], 4, 681279174), p, v, e[n], 11, -358537222), l, p, e[n + 3], 16, -722521979), g, l, e[n + 6], 23, 76029189), v = f(v, g = f(g, l = f(l, p, v, g, e[n + 9], 4, -640364487), p, v, e[n + 12], 11, -421815835), l, p, e[n + 15], 16, 530742520), g, l, e[n + 2], 23, -995338651), v = s(v, g = s(g, l = s(l, p, v, g, e[n], 6, -198630844), p, v, e[n + 7], 10, 1126891415), l, p, e[n + 14], 15, -1416354905), g, l, e[n + 5], 21, -57434055), v = s(v, g = s(g, l = s(l, p, v, g, e[n + 12], 6, 1700485571), p, v, e[n + 3], 10, -1894986606), l, p, e[n + 10], 15, -1051523), g, l, e[n + 1], 21, -2054922799), v = s(v, g = s(g, l = s(l, p, v, g, e[n + 8], 6, 1873313359), p, v, e[n + 15], 10, -30611744), l, p, e[n + 6], 15, -1560198380), g, l, e[n + 13], 21, 1309151649), v = s(v, g = s(g, l = s(l, p, v, g, e[n + 4], 6, -145523070), p, v, e[n + 11], 10, -1120210379), l, p, e[n + 2], 15, 718787259), g, l, e[n + 9], 21, -343485551),
    l = i(l, r),
    p = i(p, o),
    v = i(v, u),
    g = i(g, d);
    return [l, p, v, g]
}
function l(e) {
    var t, n = "";
    for (t = 0; t < 32 * e.length; t += 8) n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
    return n
}
function p(e) {
    var t, n = [];
    for (n[(e.length >> 2) - 1] = void 0, t = 0; t < n.length; t += 1) n[t] = 0;
    for (t = 0; t < 8 * e.length; t += 8) n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
    return n
}
function v(e) {
    var t, n, r = "";
    for (n = 0; n < e.length; n += 1) t = e.charCodeAt(n),
    r += "0123456789abcdef".charAt(t >>> 4 & 15) + "0123456789abcdef".charAt(15 & t);
    return r
}
function g(e) {
    return unescape(encodeURIComponent(e))
}
function h(e) {
    return function(e) {
        return l(d(p(e), 8 * e.length))
    } (g(e))
}
function y(e, t) {
    return function(e, t) {
        var n, r, o = p(e),
        i = [],
        u = [];
        for (i[15] = u[15] = void 0, o.length > 16 && (o = d(o, 8 * e.length)), n = 0; n < 16; n += 1) i[n] = 909522486 ^ o[n],
        u[n] = 1549556828 ^ o[n];
        return r = d(i.concat(p(t)), 512 + 8 * t.length),
        l(d(u.concat(r), 640))
    } (g(e), g(t))
}
function b(e, t, n) {
    return t ? n ? y(t, e) : function(e, t) {
        return v(y(e, t))
    } (t, e) : n ? h(e) : function(e) {
        return v(h(e))
    } (e)
}

function sign(api_name, version, param, time) {
    var c = "6f3e29a35278d71c7f65495871231324&" + api_name + "&" + version + "&" + b(param) + "&" + time;
    return b(c)
}