(this["webpackJsonpexcalidraw-tutorial"]=this["webpackJsonpexcalidraw-tutorial"]||[]).push([[0],{12:function(e,t,n){e.exports=n(19)},17:function(e,t,n){},19:function(e,t,n){"use strict";n.r(t);var r=n(1),a=n.n(r),c=n(8),i=n.n(c),o=(n(17),n(10)),l=n(0),u=n(2),s=n(3),f=n(6),d=n(9),y=(n(18),f.a.generator()),p=function(e,t,n,r,a,c){switch(c){case"line":case"rectangle":return{id:e,x1:t,y1:n,x2:r,y2:a,type:c,roughElement:"line"===c?y.line(t,n,r,a):y.rectangle(t,n,r-t,a-n)};case"pencil":return{id:e,type:c,points:[{x:t,y:n}]};default:throw new Error("Type not recognised: ".concat(c))}},h=function(e,t,n,r,a){return Math.abs(e-n)<5&&Math.abs(t-r)<5?a:null},b=function(e,t,n,r,a,c){var i=arguments.length>6&&void 0!==arguments[6]?arguments[6]:1,o={x:e,y:t},l={x:n,y:r},u={x:a,y:c},s=x(o,l)-(x(o,u)+x(l,u));return Math.abs(s)<i?"inside":null},v=function(e,t,n){var r=n.type,a=n.x1,c=n.x2,i=n.y1,o=n.y2;switch(r){case"line":var l=b(a,i,c,o,e,t),u=h(e,t,a,i,"start"),s=h(e,t,c,o,"end");return u||s||l;case"rectangle":var f=h(e,t,a,i,"tl"),d=h(e,t,c,i,"tr"),y=h(e,t,a,o,"bl"),p=h(e,t,c,o,"br");return f||d||y||p||(e>=a&&e<=c&&t>=i&&t<=o?"inside":null);case"pencil":return n.points.some((function(r,a){var c=n.points[a+1];return!!c&&null!=b(r.x,r.y,c.x,c.y,e,t,5)}))?"inside":null;default:throw new Error("Type not recognised: ".concat(r))}},x=function(e,t){return Math.sqrt(Math.pow(e.x-t.x,2)+Math.pow(e.y-t.y,2))},g=function(e,t,n){return n.map((function(n){return Object(s.a)(Object(s.a)({},n),{},{position:v(e,t,n)})})).find((function(e){return null!==e.position}))},m=function(e,t,n){switch(n.type){case"line":case"rectangle":e.draw(n.roughElement);break;case"pencil":var r=function(e){if(!e.length)return"";var t=e.reduce((function(e,t,n,r){var a=Object(u.a)(t,2),c=a[0],i=a[1],o=Object(u.a)(r[(n+1)%r.length],2),l=o[0],s=o[1];return e.push(c,i,(c+l)/2,(i+s)/2),e}),["M"].concat(Object(l.a)(e[0]),["Q"]));return t.push("Z"),t.join(" ")}(Object(d.a)(n.points));t.fill(new Path2D(r));break;default:throw new Error("Type not recognised: ".concat(n.type))}},w=function(){var e=function(e){var t=Object(r.useState)(0),n=Object(u.a)(t,2),a=n[0],c=n[1],i=Object(r.useState)([e]),o=Object(u.a)(i,2),s=o[0],f=o[1];return[s[a],function(e){var t=arguments.length>1&&void 0!==arguments[1]&&arguments[1],n="function"===typeof e?e(s[a]):e;if(t){var r=Object(l.a)(s);r[a]=n,f(r)}else{var i=Object(l.a)(s).slice(0,a+1);f([].concat(Object(l.a)(i),[n])),c((function(e){return e+1}))}},function(){return a>0&&c((function(e){return e-1}))},function(){return a<s.length-1&&c((function(e){return e+1}))}]}([]),t=Object(u.a)(e,4),n=t[0],c=t[1],i=t[2],d=t[3],y=Object(r.useState)("none"),h=Object(u.a)(y,2),b=h[0],v=h[1],x=Object(r.useState)("pencil"),w=Object(u.a)(x,2),O=w[0],j=w[1],E=Object(r.useState)(null),k=Object(u.a)(E,2),M=k[0],C=k[1];Object(r.useLayoutEffect)((function(){var e=document.getElementById("canvas"),t=e.getContext("2d");t.clearRect(0,0,e.width,e.height);var r=f.a.canvas(e);n.forEach((function(e){return m(r,t,e)}))}),[n]),Object(r.useEffect)((function(){var e=function(e){(e.metaKey||e.ctrlKey)&&"z"===e.key&&(e.shiftKey?d():i())};return document.addEventListener("keydown",e),function(){document.removeEventListener("keydown",e)}}),[i,d]);var S=function(e,t,r,a,i,o){var u=Object(l.a)(n);switch(o){case"line":case"rectangle":u[e]=p(e,t,r,a,i,o);break;case"pencil":u[e].points=[].concat(Object(l.a)(u[e].points),[{x:a,y:i}]);break;default:throw new Error("Type not recognised: ".concat(o))}c(u,!0)};return a.a.createElement("div",null,a.a.createElement("div",{style:{position:"fixed"}},a.a.createElement("input",{type:"radio",id:"selection",checked:"selection"===O,onChange:function(){return j("selection")}}),a.a.createElement("label",{htmlFor:"selection"},"Selection"),a.a.createElement("input",{type:"radio",id:"line",checked:"line"===O,onChange:function(){return j("line")}}),a.a.createElement("label",{htmlFor:"line"},"Line"),a.a.createElement("input",{type:"radio",id:"rectangle",checked:"rectangle"===O,onChange:function(){return j("rectangle")}}),a.a.createElement("label",{htmlFor:"rectangle"},"Rectangle"),a.a.createElement("input",{type:"radio",id:"pencil",checked:"pencil"===O,onChange:function(){return j("pencil")}}),a.a.createElement("label",{htmlFor:"pencil"},"Pencil")),a.a.createElement("div",{style:{position:"fixed",bottom:0,padding:10}},a.a.createElement("button",{onClick:i},"Undo"),a.a.createElement("button",{onClick:d},"Redo"),a.a.createElement("button",{onClick:function(){window.location.reload(!1)}},"Clear")),a.a.createElement("canvas",{id:"canvas",width:window.innerWidth,height:window.innerHeight,onMouseDown:function(e){var t=e.clientX,r=e.clientY;if("selection"===O){var a=g(t,r,n);if(a){if("pencil"===a.type){var i=a.points.map((function(e){return t-e.x})),o=a.points.map((function(e){return r-e.y}));C(Object(s.a)(Object(s.a)({},a),{},{xOffsets:i,yOffsets:o}))}else{var u=t-a.x1,f=r-a.y1;C(Object(s.a)(Object(s.a)({},a),{},{offsetX:u,offsetY:f}))}c((function(e){return e})),"inside"===a.position?v("moving"):v("resizing")}}else{var d=n.length,y=p(d,t,r,t,r,O);c((function(e){return[].concat(Object(l.a)(e),[y])})),C(y),v("drawing")}},onMouseMove:function(e){var t=e.clientX,r=e.clientY;if("selection"===O){var a=g(t,r,n);e.target.style.cursor=a?function(e){switch(e){case"tl":case"br":case"start":case"end":return"nwse-resize";case"tr":case"bl":return"nesw-resize";default:return"move"}}(a.position):"default"}if("drawing"===b){var i=n.length-1,u=n[i],f=u.x1,d=u.y1;S(i,f,d,t,r,O)}else if("moving"===b)if("pencil"===M.type){var y=M.points.map((function(e,n){return{x:t-M.xOffsets[n],y:r-M.yOffsets[n]}})),p=Object(l.a)(n);p[M.id]=Object(s.a)(Object(s.a)({},p[M.id]),{},{points:y}),c(p,!0)}else{var h=M.id,v=M.x1,x=M.x2,m=M.y1,w=M.y2,j=M.type,E=M.offsetX,k=M.offsetY,C=t-E,z=r-k;S(h,C,z,C+(x-v),z+(w-m),j)}else if("resizing"===b){var F=M.id,L=M.type,T=M.position,X=Object(o.a)(M,["id","type","position"]),Y=function(e,t,n,r){var a=r.x1,c=r.y1,i=r.x2,o=r.y2;switch(n){case"tl":case"start":return{x1:e,y1:t,x2:i,y2:o};case"tr":return{x1:a,y1:t,x2:e,y2:o};case"bl":return{x1:e,y1:c,x2:i,y2:t};case"br":case"end":return{x1:a,y1:c,x2:e,y2:t};default:return null}}(t,r,T,X),B=Y.x1,K=Y.y1,R=Y.x2,W=Y.y2;S(F,B,K,R,W,L)}},onMouseUp:function(){if(M){var e=M.id,t=n[e],r=t.id,a=t.type;if(("drawing"===b||"resizing"===b)&&function(e){return["line","rectangle"].includes(e)}(a)){var c=function(e){var t=e.type,n=e.x1,r=e.y1,a=e.x2,c=e.y2;if("rectangle"===t){var i=Math.min(n,a),o=Math.max(n,a);return{x1:i,y1:Math.min(r,c),x2:o,y2:Math.max(r,c)}}return n<a||n===a&&r<c?{x1:n,y1:r,x2:a,y2:c}:{x1:a,y1:c,x2:n,y2:r}}(n[e]),i=c.x1,o=c.y1,l=c.x2,u=c.y2;S(r,i,o,l,u,a)}}v("none"),C(null)}},"Canvas"))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));i.a.render(a.a.createElement(a.a.StrictMode,null,a.a.createElement(w,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[12,1,2]]]);
//# sourceMappingURL=main.1c864be8.chunk.js.map