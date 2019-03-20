from django.db import models


SIM_NAO = (
    ('S', 'Sim'),
    ('N', 'Não'),
)


class Grupo(models.Model):
    co_grupo = models.CharField(
        'Código', max_length=2,
        help_text='Código do grupo dos procedimentos')
    no_grupo = models.CharField(
        'Descrição', max_length=100,
        help_text='Nome do grupo dos procedimentos')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_grupo'
        ordering = ['co_grupo']

    def __str__(self):
        return self.co_grupo


class SubGrupo(models.Model):
    co_sub_grupo = models.CharField(
        'Código', max_length=2,
        help_text='Código do sub-grupo dos procedimentos')
    no_sub_grupo = models.CharField(
        'Descrição', max_length=100,
        help_text='Nome do sub-grupo dos procedimentos')
    co_grupo = models.CharField(
        'Grupo', max_length=2, db_column='co_grupo',
        help_text='Código do grupo dos procedimentos')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        unique_together = (('co_grupo', 'co_sub_grupo'),)
        db_table = 'tb_sub_grupo'
        ordering = ['co_grupo', 'co_sub_grupo']

    def __str__(self):
        return self.co_sub_grupo


class FormaOrganizacao(models.Model):
    co_forma_organizacao = models.CharField(
        'Código', max_length=2,
        help_text='Código  da forma de organização dos procedimentos')
    no_forma_organizacao = models.CharField(
        'Descrição', max_length=100,
        help_text='Nome  da forma de organização dos procedimentos')
    co_sub_grupo = models.CharField(
        'Sub Grupo', max_length=2, db_column='co_sub_grupo',
        help_text='Código do sub-grupo dos procedimentos')
    co_grupo = models.CharField(
        'Grupo', max_length=2, db_column='co_grupo',
        help_text='Código do grupo dos procedimentos')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        unique_together = (
            ('co_grupo', 'co_sub_grupo', 'co_forma_organizacao'),)
        db_table = 'tb_forma_organizacao'
        ordering = ['co_grupo', 'co_sub_grupo', 'co_forma_organizacao']

    def __str__(self):
        return self.co_forma_organizacao


class Procedimento(models.Model):
    COMPLEXIDADE = (
        ('0', 'Não se aplica'),
        ('1', 'Atenção Básica Complexidade'),
        ('2', 'Média Complexidade'),
        ('3', 'Alta Complexidade'),
    )
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('I', 'Indiferente/Ambos'),
        ('N', 'Não se aplica'),
    )
    co_procedimento = models.CharField(
        'Código', primary_key=True,
        max_length=10, help_text='Código do procedimento')
    no_procedimento = models.CharField(
        'Descrição', max_length=250,
        help_text='Nome descritivo do procedimento')
    tp_complexidade = models.CharField(
        'Complexidade', max_length=1,
        choices=COMPLEXIDADE,
        help_text='Define a complexidade do procedimento')
    tp_sexo = models.CharField(
        'Sexo', max_length=1, choices=SEXO,
        help_text='Define a abrangência de sexo para a aplicação do procedimento')
    qt_maxima_execucao = models.PositiveIntegerField(
        'Qtd Maxima Execução',
        help_text='Número máximo de execuções permitidas')
    qt_dias_permanencia = models.PositiveIntegerField(
        'Qtd Dias Permanência',
        help_text='Número máximo de dias de internações possíveis')
    qt_pontos = models.PositiveIntegerField(
        'Qtd Pontos',
        help_text='Quantidade de pontos para o procedimento')
    vl_idade_minima = models.PositiveIntegerField(
        'Idade Mínima',
        help_text='Idade mínima para o uso um procedimento em meses')
    vl_idade_maxima = models.PositiveIntegerField(
        'Idade Máxima',
        help_text='Idade máxima para o uso um procedimento em meses')
    vl_sh = models.DecimalField(
        'Valor Hospitalar', max_digits=8, decimal_places=2,
        help_text='Valor pago para o serviço hospitalar deste procedimento')
    vl_sa = models.DecimalField(
        'Valor Ambulatorial', max_digits=8, decimal_places=2,
        help_text='Valor pago para o serviço ambulatorial deste procedimento')
    vl_sp = models.DecimalField(
        'Valor Profissional', max_digits=8, decimal_places=2,
        help_text='Valor pago para o serviço profissional deste procedimento')
    co_financiamento = models.CharField(
        'Financiamento', max_length=2,
        help_text='Código que identifica os tipos de financiamento de um procedimento')
    co_rubrica = models.CharField(
        'Descrição', max_length=6,
        help_text='Código que identifica as rubricas')
    qt_tempo_permanencia = models.PositiveIntegerField(
        'Tempo de Permanência',
        help_text='Tempo de Permanência')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_procedimento'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class ProcedimentoOrigem(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_procedimento_origem = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE,
        related_name='procedimento_origem',
        db_column='co_procedimento_origem',
        help_text='Código do PRocedimento Origem')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_origem'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class Financiamento(models.Model):
    co_financiamento = models.CharField(
        'Código', primary_key=True, max_length=2,
        help_text='Código que identifica os tipos de financiamento de um procedimento')
    no_financiamento = models.CharField(
        'Descrição', max_length=100,
        help_text='Nome que descreve os tipos de financiamento de um procedimento')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_financiamento'
        ordering = ['co_financiamento']

    def __str__(self):
        return '{}-{}'.format(self.co_financiamento, self.no_financiamento)


class Cid(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('I', 'Indiferente/Ambos'),
    )
    AGRAVO = (
        ('0', 'Sem Agravo'),
        ('1', 'Agravo de notificação'),
        ('2', 'Agravo de bloqueio'),
    )
    co_cid = models.CharField(
        'Código', primary_key=True, max_length=4,
        help_text='Código que identifica o CID-10')
    no_cid = models.CharField(
        'Descrição', max_length=100,
        help_text='Nome da doença')
    tp_agravo = models.CharField(
        'Agravo', max_length=1, choices=AGRAVO,
        help_text='Define o tipo de agravo que deve ser notificado')
    tp_sexo = models.CharField(
        'Sexo', max_length=1, choices=SEXO,
        help_text='Define a abrangência de sexo para a doença')
    tp_estadio = models.CharField(
        'Estadio', max_length=1, choices=SIM_NAO,
        help_text='Diz se o cid é ou não estadiável')
    vl_campos_irradiados = models.PositiveIntegerField(
        'Campos Irradiados',
        help_text='')

    class Meta:
        db_table = 'tb_cid'
        ordering = ['co_cid']

    def __str__(self):
        return self.co_cid


class ProcedimentoCid(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_cid = models.ForeignKey(
        Cid, on_delete=models.CASCADE, db_column='co_cid',
        help_text='Código do CID')
    st_principal = models.CharField(
        'Principal', max_length=1,
        help_text='')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_cid'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class Detalhe(models.Model):
    co_detalhe = models.CharField(
        'Código', primary_key=True, max_length=3,
        help_text='Código que identifica os atributos de detalhes de um procedimento')
    no_detalhe = models.CharField(
        'Descrição', max_length=100,
        help_text='Nome que descreve os atributos de detalhes de um procedimento')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_detalhe'
        ordering = ['co_detalhe']

    def __str__(self):
        return self.co_detalhe


class ProcedimentoDetalhe(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_detalhe = models.ForeignKey(
        Detalhe, on_delete=models.CASCADE, db_column='co_detalhe',
        help_text='Código do CID')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_detalhe'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class Habilitacao(models.Model):
    co_habilitacao = models.CharField(
        'Código', primary_key=True, max_length=4,
        help_text='Código que identifica uma habilitação para o CNES')
    no_habilitacao = models.CharField(
        'Descrição', max_length=150,
        help_text='Nome de uma habilitação')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_habilitacao'
        ordering = ['co_habilitacao']

    def __str__(self):
        return self.co_habilitacao


class ProcedimentoIncremento(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_habilitacao = models.ForeignKey(
        Habilitacao, on_delete=models.CASCADE, db_column='co_habilitacao',
        help_text='Código da Habilitação')
    vl_percentual_sh = models.DecimalField(
        'Percentual Hospitalar', max_digits=5, decimal_places=2,
        help_text='')
    vl_percentual_sa = models.DecimalField(
        'Percentual Ambulatorial', max_digits=5, decimal_places=2,
        help_text='')
    vl_percentual_sp = models.DecimalField(
        'Percentual Profissional', max_digits=5, decimal_places=2,
        help_text='')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_incremento'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class GrupoHabilitacao(models.Model):
    nu_grupo_habilitacao = models.CharField(
        'Código', primary_key=True, max_length=4,
        help_text='Código do grupo de habilitação')
    no_grupo_habilitacao = models.CharField(
        'Nome Curto', max_length=20,
        help_text='Nome (curto) do grupo de habilitação')
    ds_grupo_habilitacao = models.CharField(
        'Descrição', max_length=25,
        help_text='Descrição (longa) do grupo de habilitação')

    class Meta:
        db_table = 'tb_grupo_habilitacao'
        ordering = ['nu_grupo_habilitacao']

    def __str__(self):
        return self.nu_grupo_habilitacao


class ProcedimentoHabilitacao(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_habilitacao = models.ForeignKey(
        Habilitacao, on_delete=models.CASCADE, db_column='co_habilitacao',
        help_text='Código da Habilitação')
    nu_grupo_habilitacao = models.ForeignKey(
        GrupoHabilitacao, on_delete=models.CASCADE, db_column='nu_grupo_habilitacao',
        help_text='Código do grupo de habilitação')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_habilitacao'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class TipoLeito(models.Model):
    co_tipo_leito = models.CharField(
        'Código', primary_key=True, max_length=2,
        help_text='Código da classificação de leito')
    no_tipo_leito = models.CharField(
        'Descrição', max_length=60,
        help_text='Nome da classificação de leito.')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_tipo_leito'
        ordering = ['co_tipo_leito']

    def __str__(self):
        return self.co_tipo_leito


class ProcedimentoTipoLeito(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_tipo_leito = models.ForeignKey(
        TipoLeito, on_delete=models.CASCADE, db_column='co_tipo_leito',
        help_text='Código do Tipo de Leito')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_leito'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class Registro(models.Model):
    co_registro = models.CharField(
        'Código', primary_key=True, max_length=2,
        help_text='Código do instrumento de registro do procedimento')
    no_registro = models.CharField(
        'Descrição', max_length=50,
        help_text='Nome do instrumento de registro do procedimento')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_registro'
        ordering = ['co_registro']

    def __str__(self):
        return self.co_registro


class ProcedimentoRegistro(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_registro = models.ForeignKey(
        Registro, on_delete=models.CASCADE,
        db_column='co_registro',
        help_text='Código do Tipo de Registro')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_registro'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class ProcedimentoCompativel(models.Model):
    co_procedimento_principal = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE,
        db_column='co_procedimento_principal',
        related_name='procedimento_principal_comp',
        help_text='Código do procedimento')
    co_registro_principal = models.ForeignKey(
        Registro, on_delete=models.CASCADE,
        db_column='co_registro_principal',
        related_name='registro_principal_comp',
        help_text='Código do Tipo de Registro')
    co_procedimento_compativel = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE,
        db_column='co_procedimento_compativel',
        related_name='procedimento_compativel_comp',
        help_text='Código do procedimento')
    co_registro_compativel = models.ForeignKey(
        Registro, on_delete=models.CASCADE,
        db_column='co_registro_compativel',
        related_name='registro_compativel_comp',
        help_text='Código do Tipo de Registro')
    tp_compatibilidade = models.CharField(
        'Tipo Compatibilidade', max_length=1,
        help_text='')
    qt_permitida = models.PositiveIntegerField(
        'Qtd Permitida',
        help_text='')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_compativel'
        ordering = ['co_procedimento_principal']

    def __str__(self):
        return self.co_procedimento_principal


class Servico(models.Model):
    co_servico = models.CharField(
        'Código', primary_key=True, max_length=3,
        help_text='Código que identifica os serviços')
    no_servico = models.CharField(
        'Descrição', max_length=120,
        help_text='Nome que descreve os serviços')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_servico'
        ordering = ['co_servico']

    def __str__(self):
        return self.co_servico


class ProcedimentoServico(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_servico = models.ForeignKey(
        Servico, on_delete=models.CASCADE,
        db_column='co_servico',
        help_text='Código do Serviço')
    co_classificacao = models.CharField(
        'Código', max_length=3,
        help_text='Código que identifica os serviços')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_servico'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class ServicoClassificacao(models.Model):
    co_classificacao = models.CharField(
        'Código', max_length=3,
        help_text='Código que identifica os serviços')
    co_servico = models.ForeignKey(
        Servico, on_delete=models.CASCADE, db_column='co_servico',
        help_text='Código que identifica a classificação de um serviço')
    no_classificacao = models.CharField(
        'Descrição', max_length=150,
        help_text='Nome que descreve a classificação de um serviço')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_servico_classificacao'
        ordering = ['co_classificacao']

    def __str__(self):
        return self.co_classificacao


class Ocupacao(models.Model):
    co_ocupacao = models.CharField(
        'Código', primary_key=True, max_length=6,
        help_text='Código que identifica a classificação das ocupações definidas pela CBO-2002')
    no_ocupacao = models.CharField(
        'Descrição', max_length=150,
        help_text='Nome das ocupações definidas pela CBO-2002')

    class Meta:
        db_table = 'tb_ocupacao'
        ordering = ['co_ocupacao']

    def __str__(self):
        return self.co_ocupacao


class ProcedimentoOcupacao(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_ocupacao = models.ForeignKey(
        Ocupacao, on_delete=models.CASCADE,
        db_column='co_ocupacao',
        help_text='Código que identifica a classificação das ocupações definidas pela CBO-2002')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_ocupacao'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class Rubrica(models.Model):
    co_rubrica = models.CharField(
        'Código', primary_key=True, max_length=6,
        help_text='Código que identifica as rubricas. As duas primeiras posições identifica o código de financiamento')
    no_rubrica = models.CharField(
        'Descrição', max_length=100,
        help_text='Nome das rubricas.')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_rubrica'
        ordering = ['co_rubrica']

    def __str__(self):
        return self.co_rubrica


class SiaSih(models.Model):
    TP_PROCEDIMENTO = (
        ('A', 'Ambulatorial'),
        ('H', 'Hospitalar'),
    )
    co_procedimento_sia_sih = models.CharField(
        'Código', max_length=10,
        help_text='Código que identifica os procedimento do SAI e SIH na data de vigência da nova tabela')
    no_procedimento_sia_sih = models.CharField(
        'Descrição', max_length=100,
        help_text='Nome dos procedimento do SAI e SIH na data de vigência da nova tabela')
    tp_procedimento = models.CharField(
        'Tipo', max_length=1, choices=TP_PROCEDIMENTO,
        help_text='Define qual era o tipo do procedimento SAI e/ou SIH de origem do novo procedimento')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_sia_sih'
        ordering = ['co_procedimento_sia_sih']

    def __str__(self):
        return self.co_procedimento_sia_sih


class ProcedimentoSiaSih(models.Model):
    TP_PROCEDIMENTO = (
        ('A', 'Ambulatorial'),
        ('H', 'Hospitalar'),
    )
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código doprocedimento')
    co_procedimento_sia_sih = models.ForeignKey(
        SiaSih, on_delete=models.CASCADE,
        db_column='co_procedimento_sia_sih',
        help_text='Código que identifica o procedimento do SAI e SIH que deu origem ao novo procedimento da tabela unificada')
    tp_procedimento = models.CharField(
        'Tipo', max_length=1, choices=TP_PROCEDIMENTO,
        help_text='Define qual era o tipo do procedimento SAI e/ou SIH de origem do novo procedimento')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_sia_sih'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class Descricao(models.Model):
    co_procedimento = models.CharField(
        'Código', primary_key=True,
        max_length=10, help_text='Código do procedimento')
    ds_procedimento = models.TextField(
        'Descrição',
        help_text='Descrição do procedimento')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_descricao'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class DescricaoDetalhe(models.Model):
    co_detalhe = models.CharField(
        'Código', primary_key=True,
        max_length=3, help_text='Código do detalhe')
    ds_detalhe = models.TextField(
        'Descrição',
        help_text='Descrição do detalhe')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_descricao_detalhe'
        ordering = ['co_detalhe']

    def __str__(self):
        return self.co_detalhe


class RegraCondicionada(models.Model):
    co_regra_condicionada = models.CharField(
        'Código', primary_key=True,
        max_length=4, help_text='Código da regra condicionada')
    no_regra_condicionada = models.CharField(
        'Código',
        max_length=150, help_text='Nome da regra condicionada')
    ds_regra_condicionada = models.TextField(
        'Descrição',
        help_text='Descrição da regra condicionada')

    class Meta:
        db_table = 'tb_regra_condicionada'
        ordering = ['co_regra_condicionada']

    def __str__(self):
        return self.co_regra_condicionada


class ProcedimentoRegraCondicionada(models.Model):
    co_regra_condicionada = models.ForeignKey(
        RegraCondicionada, on_delete=models.CASCADE,
        db_column='co_regra_condicionada',
        help_text='Código da regra condicionada')
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código doprocedimento')

    class Meta:
        db_table = 'rl_procedimento_regra_cond'
        ordering = ['co_regra_condicionada']

    def __str__(self):
        return self.co_regra_condicionada


class RedeAtencao(models.Model):
    co_rede_atencao = models.CharField(
        'Código', primary_key=True,
        max_length=3, help_text='Código')
    no_rede_atencao = models.CharField(
        'Código',
        max_length=50, help_text='Descrição')

    class Meta:
        db_table = 'tb_rede_atencao'
        ordering = ['co_rede_atencao']

    def __str__(self):
        return self.co_rede_atencao


class ComponenteRede(models.Model):
    co_componente_rede = models.CharField(
        'Código', primary_key=True,
        max_length=10, help_text='Código')
    no_componente_rede = models.CharField(
        'Código',
        max_length=150, help_text='Descrição')
    co_rede_atencao = models.CharField(
        'Descrição', max_length=3,
        help_text='')

    class Meta:
        db_table = 'tb_componente_rede'
        ordering = ['co_componente_rede']

    def __str__(self):
        return self.co_componente_rede


class ProcedimentoComponenteRede(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_componente_rede = models.ForeignKey(
        ComponenteRede, on_delete=models.CASCADE, db_column='co_componente_rede',
        help_text='Código do CID')

    class Meta:
        db_table = 'rl_procedimento_comp_rede'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class Modalidade(models.Model):
    co_modalidade = models.CharField(
        'Código', primary_key=True, max_length=2,
        help_text='Código da Modalidade')
    no_modalidade = models.CharField(
        'Descrição', max_length=100,
        help_text='Nome da Modalidade')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'tb_modalidade'
        ordering = ['co_modalidade']

    def __str__(self):
        return self.co_modalidade


class ProcedimentoModalidade(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_modalidade = models.ForeignKey(
        Modalidade, on_delete=models.CASCADE,
        db_column='co_modalidade',
        help_text='Código da Modalidade')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_procedimento_modalidade'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class Renases(models.Model):
    co_renases = models.CharField(
        'Código', primary_key=True,
        max_length=10, help_text='Código')
    no_renases = models.CharField(
        'Código',
        max_length=150, help_text='Descrição')

    class Meta:
        db_table = 'tb_renases'
        ordering = ['co_renases']

    def __str__(self):
        return self.co_renases


class ProcedimentoRenases(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_renases = models.ForeignKey(
        Renases, on_delete=models.CASCADE,
        db_column='co_renases',
        help_text='Código do Renases')

    class Meta:
        db_table = 'rl_procedimento_renases'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class Tuss(models.Model):
    co_tuss = models.CharField(
        'Código', primary_key=True,
        max_length=10, help_text='Código')
    no_tuss = models.CharField(
        'Código',
        max_length=150, help_text='Descrição do procedimento TUSS')

    class Meta:
        db_table = 'tb_tuss'
        ordering = ['co_tuss']

    def __str__(self):
        return self.co_tuss


class ProcedimentoTuss(models.Model):
    co_procedimento = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento',
        help_text='Código do procedimento')
    co_tuss = models.ForeignKey(
        Tuss, on_delete=models.CASCADE,
        db_column='co_tuss',
        help_text='Código do Procedimento Tuss')

    class Meta:
        db_table = 'rl_procedimento_tuss'
        ordering = ['co_procedimento']

    def __str__(self):
        return self.co_procedimento


class ExcecaoCompatibilidade(models.Model):
    co_procedimento_restricao = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento_restricao',
        related_name='procedimento_restricao',
        help_text='Código doprocedimento')
    co_procedimento_principal = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento_principal',
        related_name='procedimento_principal',
        help_text='Código doprocedimento')
    co_registro_principal = models.ForeignKey(
        Registro, on_delete=models.CASCADE, db_column='co_registro_principal',
        related_name='registro_principal',
        help_text='Registro Principal')
    co_procedimento_compativel = models.ForeignKey(
        Procedimento, on_delete=models.CASCADE, db_column='co_procedimento_compativel',
        related_name='procedimento_compativel',
        help_text='Código doprocedimento')
    co_registro_compativel = models.ForeignKey(
        Registro, on_delete=models.CASCADE, db_column='co_registro_compativel',
        related_name='registro_compativel',
        help_text='Registro Compatível')
    tp_compatibilidade = models.CharField(
        'Tipo Compatibilidade',
        max_length=1, help_text='Tipo de Compatibilidade')
    dt_competencia = models.CharField(
        'Competência', max_length=6,
        help_text='Data que informa a competência de validade deste registro')

    class Meta:
        db_table = 'rl_excecao_compatibilidade'
        ordering = ['co_procedimento_restricao']

    def __str__(self):
        return self.co_procedimento_restricao
