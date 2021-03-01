import os 
import csv

d = {}
paired_d = {}

with open('LCHC-VJ.csv', 'r') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        hv = row['heavy_v']
        hj = row['heavy_j']
        lv = row['light_v']
        lj = row['light_j']
        
        heavy_vj = row['heavy_v'] + '_' + row['heavy_j']
        light_vj = row['light_v'] + '_' + row['light_j']
        paired_vj = heavy_vj + '_' + light_vj
        
        if hv not in d:
            d[hv] = {'IGHJ1': 0, 'IGHJ2': 0, 'IGHJ3': 0, 'IGHJ4': 0, 'IGHJ5': 0, 'IGHJ6': 0}
        d[hv][hj] += 1
        
        if lv not in d:
            d[lv] = {'IGKJ1': 0, 'IGKJ2': 0, 'IGKJ3': 0, 'IGKJ4': 0, 'IGKJ5': 0, 'IGLJ1': 0, 'IGLJ2': 0, 'IGLJ3': 0, 'IGLJ4': 0, 'IGLJ5': 0, 'IGLJ6': 0, 'IGLJ7': 0}
                
        d[lv][lj] += 1
        
        if paired_vj not in paired_d:
            paired_d[paired_vj] = 0
        
        paired_d[paired_vj] += 1
        
        with open('LCHC-VJ-lights.csv', 'w') as lout, open('LCHC-VJ-heavies.csv', 'w') as hout:
    lout.write('V,IGLJ1,IGLJ2,IGLJ3,IGLJ4,IGLJ5,IGLJ6,IGLJ7,IGKJ1,IGKJ2,IGKJ3,IGKJ4,IGKJ5\n')
    hout.write('V,IGHJ1,IGHJ2,IGHJ3,IGHJ4,IGHJ5,IGHJ6\n')
    for v in sorted(d.keys()):
        if 'H' in v:
            hout.write(','.join([v,str(d[v]['IGHJ1']),str(d[v]['IGHJ2']),str(d[v]['IGHJ3']),str(d[v]['IGHJ4']),str(d[v]['IGHJ5']),str(d[v]['IGHJ6'])]) + '\n')
        else:
            lout.write(','.join([v,str(d[v]['IGLJ1']),str(d[v]['IGLJ2']),str(d[v]['IGLJ3']),str(d[v]['IGLJ4']),str(d[v]['IGLJ5']),str(d[v]['IGLJ6']),str(d[v]['IGLJ7']),str(d[v]['IGKJ1']),str(d[v]['IGKJ2']),str(d[v]['IGKJ3']),str(d[v]['IGKJ4']),str(d[v]['IGKJ5'])]) + '\n')
        
with open('LCHC-VJ-paired.csv', 'w') as fout:
    fout.write('vj,count\n')
    for vj in paired_d:
        fout.write(vj + ',' + str(paired_d[vj]) + '\n')
