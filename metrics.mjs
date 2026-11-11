export function metrics(v,h=[],peers=[],now=Date.now()){
const age=Math.max((now-Date.parse(v.publishedAt))/3600000,1);
const samples=h.filter(p=>Number.isFinite(p.at)&&Number.isFinite(p.views)&&p.at<=now).sort((a,b)=>a.at-b.at);
const latest=samples.at(-1);
const prev=latest?[...samples].reverse().find(p=>latest.at-p.at>=300000):null;
const elapsed=prev?(latest.at-prev.at)/3600000:null;
const delta=prev?latest.views-prev.views:null;
const rates=peers.filter(p=>p.id!==v.id).map(p=>p.views/Math.max((now-Date.parse(p.publishedAt))/3600000,1)).sort((a,b)=>a-b);
const baseline=rates.length?rates[Math.floor(rates.length/2)]:0;
return {velocity:prev?Math.max(0,delta)/elapsed:null,delta,windowMinutes:elapsed===null?null:elapsed*60,measuredFrom:prev?.at??null,measuredAt:latest?.at??null,corrected:delta!==null&&delta<0,lifetimeRate:v.views/age,outlier:baseline?v.views/age/baseline:null};
}
