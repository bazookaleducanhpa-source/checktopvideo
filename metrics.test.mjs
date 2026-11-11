import {test} from 'node:test';import assert from 'node:assert/strict';import {metrics} from './metrics.mjs';
const now=Date.UTC(2026,10,11,12),publishedAt=new Date(now-3600000).toISOString(),v={id:'a',views:200,publishedAt};
test('single old snapshot never counts as growth measurement',()=>{assert.equal(metrics(v,[{at:now-3600000,views:200}],[],now).velocity,null);});
test('two snapshots less than five minutes apart remain pending even when old',()=>{assert.equal(metrics(v,[{at:now-3600000,views:100},{at:now-3480000,views:200}],[],now).velocity,null);});
test('growth uses actual snapshot time, not wall clock',()=>{const m=metrics(v,[{at:now-7200000,views:100},{at:now-5400000,views:200}],[],now);assert.equal(m.velocity,200);assert.equal(m.windowMinutes,30);assert.equal(m.delta,100);});
test('unchanged views across sufficient snapshots yield measured zero',()=>assert.equal(metrics(v,[{at:now-3600000,views:200},{at:now-1800000,views:200}],[],now).velocity,0));
test('channel outlier and lifetime average available without growth history',()=>{let m=metrics(v,[],[v,{id:'b',views:50,publishedAt}],now);assert.equal(m.outlier,4);assert.equal(m.lifetimeRate,200);assert.equal(m.velocity,null);});
test('correction is explicit and does not produce negative velocity',()=>{const m=metrics(v,[{at:now-3600000,views:300},{at:now-1800000,views:200}],[],now);assert.equal(m.velocity,0);assert.equal(m.corrected,true);assert.equal(m.delta,-100);});
