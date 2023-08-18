    import datetime
    import gzip
    import shutil
    import json
    import re
    import os

    now = datetime.datetime.now()
    ano = str(now.year)
    mes = str(now.month)
    dia = str(now.day)
    hora = str(now.hour)
    if hora == '0':
        hora = '00'
    def get_json(path):
        # Descompacta o json
        with gzip.open(path+'resources.json.gz', 'rb') as entrada:
            with open(path+'resources.json', 'wb') as saida:
                shutil.copyfileobj(entrada, saida)
        # Carrega o json
        with open(path+'resources.json') as file:
            json_data = json.load(file)
    
        return json_data
    resources_total = 0
    resources_count = 0
    resources       = ''
    politica        = ''
    tittle          = ''
    body            = ''
    #-----------------------------------------------------------------------------
    politica = 's3-tag-compliance-name'
    descricao = 'Recursos S3 sem tags "environment, vertical, startup"'
    path = 'policies/'+politica+'/'+ano+'/'+mes+'/'+dia+'/'+hora+'/'
    # Lista os dados
    s3_json = get_json(path)
    resources_total = len(get_json(path))
    tittle = '<div"><span style="font-family:sans-serif; font-size:16px;f ont-weight:bold; color:#006400;">'+descricao+' - </span><span style="font-family:sans-serif; color: #A52A2A; font-weight: bold;">'+str(resources_total).zfill(4)+'</span></div>'
    resources_count = 0
    while resources_count < resources_total:
        Name = '<div  style="width:350px; display:inline-block; font-size:12px;">'+str(s3_json[resources_count]['Name'])+'</div>'
        resources += '<span style="color:#7CCD7C; font-weight:bold; font-size:12px;">'+str(resources_count).zfill(4)+'</span> - '+Name+'<br/>'
        resources_count += 1
    body += tittle+'<div id="div1" style="font-family:sans-serif;color:#999999;">'+resources+'<br/></div>'
    #-----------------------------------------------------------------------------

    codigo_html = '''
    <html>
    <head>
    <title>Cloud Custodian</title>
    </head>
    <body style="background-color: #111111;" >'''+body
    '''
    </body>
    </html>
    '''
    arq_html = open('index.html', 'w')
    arq_html.write(codigo_html)
    arq_html.close()

    # envia html para o pod do cloud-custodian-console
    out = os.popen("kubectl get pods -n teste").read()
    x = re.search(r"\bclou\w+\b-\bcus\w+\-\bcon\w+\-\w+\-\w+", out)
    pod = str(x.group())
    cmd = 'kubectl cp index.html -n teste '+pod+':/usr/share/nginx/html/'
    res = os.system(cmd)
    if res == 0:
        print(f'HTML enviado ao pod {pod} com sucesso!')