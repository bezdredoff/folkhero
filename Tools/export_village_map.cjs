const fs=require('fs'),vm=require('vm');
class E{constructor(tag){this.tag=tag;this.attrs={};this.children=[];this.textContent='';this.style={};this.classList={remove(){},add(){}};}setAttribute(k,v){this.attrs[k]=v;}appendChild(e){this.children.push(e);return e;}replaceChildren(){this.children=[];}addEventListener(){}querySelectorAll(){return [];} }
const svg=new E('svg'),picks=new E('div'),detail=new E('div'),root=new E('div');root.clientWidth=1000;root.querySelector=s=>s==='svg'?svg:s==='#village-picks'?picks:detail;
const context={document:{getElementById:()=>root,createElementNS:(_,tag)=>new E(tag),createElement:t=>new E(t)},ResizeObserver:class{observe(){}},console};
const file='References/Targets/Act_I_Village/Layout/village-terrain-selected.fragment.html';vm.runInNewContext(fs.readFileSync(file,'utf8').split('<script>')[1].split('</script>')[0],context);
const colors={'--foreground':'#302e28','--border':'#c2c0af','--card':'#fffaf0','--muted-foreground':'#87785e','--viz-series-1':'#b5844e','--viz-series-2':'#4c8d9b','--viz-series-3':'#77954c'};
const esc=x=>String(x).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
function ser(e){return '<'+e.tag+' '+Object.entries(e.attrs).map(([k,v])=>k+'="'+esc(v)+'"').join(' ')+'>'+esc(e.textContent)+e.children.map(ser).join('')+'</'+e.tag+'>';}
svg.setAttribute('xmlns','http://www.w3.org/2000/svg');svg.setAttribute('width',1000);svg.setAttribute('height',1334);const css=fs.readFileSync(file,'utf8').split('<style>')[1].split('</style>')[0].replace(/#folkhero-map /g,'');let out=ser(svg).replace('>','><style>'+css+'</style><title>Accepted terrain schematic — 23 households</title>');out=out.replace(/var\((--[a-z0-9-]+)\)/g,(_,k)=>colors[k]||'#302e28');fs.writeFileSync('References/Targets/Act_I_Village/Layout/village-terrain-selected.svg',out);
if(svg.children.filter(e=>e.attrs['data-key']?.startsWith('h')).length!==23)throw Error('yard count');
console.log('Static SVG exported; 23 numbered yards.');
