import math
from .common import number,integer,identifier,unique_ids
def run(d):
 rows=d['samples'];period=integer(d['ticks_per_turn'],2,2**32)
 if not 2<=len(rows)<=1000:raise ValueError('samples')
 x=[number(r['raw_ticks'])for r in rows];y=[number(r['reference_radians'])for r in rows];scale=2*math.pi/period
 if max(x)==min(x):raise ValueError('no_excitation')
 candidates=[]
 for sign in [-1,1]:
  offset=sum(yy-sign*xx*scale for xx,yy in zip(x,y))/len(x);res=[sign*xx*scale+offset-yy for xx,yy in zip(x,y)];candidates.append(dict(sign=sign,offset_radians=offset,offset_ticks=-offset/(sign*scale),rmse=math.sqrt(sum(v*v for v in res)/len(res)),residuals=res))
 best=min(candidates,key=lambda c:c['rmse']);return dict(candidates=candidates,best=best,rmse_gap=abs(candidates[0]['rmse']-candidates[1]['rmse']),raw_wrap_handled=False)
