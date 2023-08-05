import xmltodict

def ler_xml_danfe(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    #print(documento)
    # valor_total, produtos/serviços (valores), cnpj_vendedor, nome_vendeu, cpf/cnpj_comprou, nome_comprou

    dic_notafiscal = documento['nfeProc']['NFe']['infNFe']

    valor_total = dic_notafiscal['total']['ICMSTot']['vNF']
    cnpj_vendedor = dic_notafiscal['emit']['CNPJ']
    nome_vendeu = dic_notafiscal['emit']['xNome']
    cpf_comprou = dic_notafiscal['dest']['CPF']
    nome_comprou = dic_notafiscal['dest']['xNome']

    produtos = dic_notafiscal['det']
    lista_produtos = []
    for produto in produtos:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['xProd']
        lista_produtos.append((nome_produto, valor_produto))

    resposta = {'Valor total': [valor_total],
                'cnpj_vendedor': [cnpj_vendedor],
                'nome_vendedor': [nome_vendeu],
                'cpf_comprador': [cpf_comprou],
                'nome_comprador': [nome_comprou],
                'lista_produtos': [lista_produtos]
                } 
    
    return resposta

def ler_xml_servico(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    # print(documento)
    dic_notafiscal = documento['ConsultarNfseResposta']['ListaNfse']['CompNfse']['Nfse']['InfNfse']

    valor_total = dic_notafiscal['Servico']['Valores']['ValorServicos']
    cnpj_vendeu = dic_notafiscal['PrestadorServico']['IdentificacaoPrestador']['Cnpj']
    nome_vendeu = dic_notafiscal['PrestadorServico']['RazaoSocial']
    cpf_comprou = dic_notafiscal['TomadorServico']['IdentificacaoTomador']['CpfCnpj']['Cnpj']
    nome_comprou = dic_notafiscal['TomadorServico']['RazaoSocial']
    produtos = dic_notafiscal['Servico']['Discriminacao']
    resposta = {
        'valor_total': [valor_total],
        'cnpj_vendeu': [cnpj_vendeu],
        'nome_vendeu': [nome_vendeu],
        'cpf_comprou': [cpf_comprou],
        'nome_comprou': [nome_comprou],
        'lista_produtos': [produtos],
    }
    return resposta


# print(ler_xml_danfe('Mentorias/Mentoria Leitura de XML e Notas Fiscais/DANFEBrota.xml'))
# print(ler_xml_danfe('Mentorias/Mentoria Leitura de XML e Notas Fiscais/DANFENespresso.xml'))

import os
lista_arquivos = os.listdir('Mentorias/Mentoria Leitura de XML e Notas Fiscais/')

for arquivo in lista_arquivos:
    if 'xml' in arquivo:
        if 'DANFE' in arquivo:
            print(ler_xml_danfe(f'Mentorias/Mentoria Leitura de XML e Notas Fiscais/{arquivo}'))
        else:
            print(ler_xml_servico(f'Mentorias/Mentoria Leitura de XML e Notas Fiscais/{arquivo}'))

# import pandas as pd

# tabela = pd.DataFrame.from_dict(resposta)
# tabela.to_excel('NF.xlsx')

