import pandas as pd
import re 


df = pd.read_csv('votacao_primeiro_2023')


df.columns = ['data', 'nome', 'ano', 'voto']


df['LGG'] = df['voto'].apply(lambda x: len(re.findall(r"\bLGG\b", x)))
df['MAT'] = df['voto'].apply(lambda x: len(re.findall(r"\bMAT\b", x)))
df['CHS'] = df['voto'].apply(lambda x: len(re.findall(r"\bCHS\b", x)))
df['CNT'] = df['voto'].apply(lambda x: len(re.findall(r"\bCNT\b", x)))
df['LGG_MAT'] = df['voto'].apply(lambda x: len(re.findall(r"\bLGG_MAT\b", x)))
df['CHS_CNT'] = df['voto'].apply(lambda x: len(re.findall(r"\bCHS_CNT\b", x)))
df['CNT_LGG'] = df['voto'].apply(lambda x: len(re.findall(r"\bCNT_LGG\b", x)))
df['MAT_CHS'] = df['voto'].apply(lambda x: len(re.findall(r"\bMAT_CHS\b", x)))
df['CNT_MAT'] = df['voto'].apply(lambda x: len(re.findall(r"\bCNT_MAT\b", x)))
df['LGG_CHS'] = df['voto'].apply(lambda x: len(re.findall(r"\bLGG_CHS\b", x)))
df['LGG_MAT_CHS_CNT_1'] = df['voto'].apply(lambda x: len(re.findall(r"\bLGG_MAT_CHS_CNT_1\b", x)))
df['LGG_MAT_CHS_CNT_2'] = df['voto'].apply(lambda x: len(re.findall(r"\bLGG_MAT_CHS_CNT_2\b", x)))


nao_acertaram_nada = df.query('LGG_MAT_CHS_CNT_1 == 0 & LGG_MAT_CHS_CNT_2 == 0 & MAT_CHS == 0')
acertaram_tudo = df.query('LGG_MAT_CHS_CNT_1 == 1 & LGG_MAT_CHS_CNT_2 == 1 & MAT_CHS == 1')


nao_acertaram_nada.to_excel('nao_acertaram_nada_segundo_ano.xlsx')
acertaram_tudo.to_excel('acertaram_tudo.xlsx')



df = pd.read_excel('votacao_terceiro.xlsx')


df.columns = ['data', 'nome', 'ano', 'voto']

df['voto'] = df['voto'].apply(lambda x: x.replace('LGG_MAT_CHS_CNT _2', 'LGG_MAT_CHS_CNT_2'))

df['LGG'] = df['voto'].apply(lambda x: len(re.findall(r"\bLGG\b", x)))
df['MAT'] = df['voto'].apply(lambda x: len(re.findall(r"\bMAT\b", x)))
df['CHS'] = df['voto'].apply(lambda x: len(re.findall(r"\bCHS\b", x)))
df['CNT'] = df['voto'].apply(lambda x: len(re.findall(r"\bCNT\b", x)))
df['LGG_MAT'] = df['voto'].apply(lambda x: len(re.findall(r"\bLGG_MAT\b", x)))
df['CHS_CNT'] = df['voto'].apply(lambda x: len(re.findall(r"\bCHS_CNT\b", x)))
df['CNT_LGG'] = df['voto'].apply(lambda x: len(re.findall(r"\bCNT_LGG\b", x)))
df['MAT_CHS'] = df['voto'].apply(lambda x: len(re.findall(r"\bMAT_CHS\b", x)))
df['CNT_MAT'] = df['voto'].apply(lambda x: len(re.findall(r"\bCNT_MAT\b", x)))
df['LGG_CHS'] = df['voto'].apply(lambda x: len(re.findall(r"\bLGG_CHS\b", x)))

df['LGG_MAT_CHS_CNT_1'] = df['voto'].apply(lambda x: len(re.findall(r"\bLGG_MAT_CHS_CNT_1\b", x)))
df['LGG_MAT_CHS_CNT_2'] = df['voto'].apply(lambda x: len(re.findall(r"\bLGG_MAT_CHS_CNT_2\b", x)))



nao_acertaram_nada_terceiro = df.query('LGG_MAT_CHS_CNT_1 == 0 & LGG_MAT_CHS_CNT_2 == 0 & LGG == 0')
acertaram_tudo_terceiro = df.query('LGG_MAT_CHS_CNT_1 == 1 & LGG_MAT_CHS_CNT_2 == 1 & LGG == 1')


nao_acertaram_nada.to_excel('nao_acertaram_nada_segundo_ano.xlsx')


nao_acertaram_nada_terceiro.to_excel('nao_acertaram_nada_terceiro_ano.xlsx')






















