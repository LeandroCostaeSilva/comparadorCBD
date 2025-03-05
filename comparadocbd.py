
# app comparativo de preço cbd

#coletar dados do produto
concentracaocbd = float(input("informe a concentração do CBD no produto (mg/mL): "))
vol = int(input("informe o volume do frasco em mililitros: "))
#cálculo de teor CBD
Teorcbd = concentracaocbd * vol
#correção do valor em moeda nacional
preco_usd = float(input("informe o valor em dólar do produto de cannabis: "))
USD = float(input("informe a cotação atual do dólar: "))
preco_brl = preco_usd * USD
#inserir custo de tributos (ICMS, II, pis/confins e IPI)
produto_tributado = preco_brl * 1.6
#coletar dados da importação
frete = float(input("informe o custo do frete internacional em USD: "))
frete_corrigido = frete * USD
armazenagem = int(input(" informe o número de dias estimado de permanência da carga no recinto alfandegado: " ))
custo_armazenagem = armazenagem * 100
outras_siscomex = float(input("informe o valor do serviço despachante e das taxas siscomex: "))
quantida_frascos = int(input("digite o número de frascos importados: "))
preco_unitario = produto_tributado + (frete_corrigido / quantida_frascos + custo_armazenagem / quantida_frascos + outras_siscomex / quantida_frascos)
preco_mg_cbd = preco_unitario / Teorcbd
                       
if preco_mg_cbd > 0.48:
    print(" o produto importado é mais caro que o CBD disponível no mercado nacional")
elif preco_mg_cbd < 0.48:
    print("a importação é vantajosa.")
else:
    print("valores informados com erro")
