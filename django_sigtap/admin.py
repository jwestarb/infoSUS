from django.contrib import admin
from .models import Cid, ComponenteRede, Descricao, DescricaoDetalhe, Detalhe, \
    ExcecaoCompatibilidade, Financiamento, FormaOrganizacao, Grupo, \
    GrupoHabilitacao, Habilitacao, Modalidade, Ocupacao, Procedimento, \
    ProcedimentoCid, ProcedimentoCompativel, ProcedimentoComponenteRede, \
    ProcedimentoDetalhe, ProcedimentoHabilitacao, ProcedimentoIncremento, \
    ProcedimentoModalidade, ProcedimentoOcupacao, ProcedimentoOrigem, \
    ProcedimentoRegistro, ProcedimentoRegraCondicionada, ProcedimentoRenases, \
    ProcedimentoServico, ProcedimentoSiaSih, ProcedimentoTipoLeito, \
    ProcedimentoTuss, RedeAtencao, Registro, RegraCondicionada, Renases, \
    Rubrica, Servico, ServicoClassificacao, SiaSih, SubGrupo, TipoLeito, Tuss


@admin.register(Cid)
class CidAdmin(admin.ModelAdmin):
    list_display = ['co_cid', 'no_cid', 'tp_agravo',
                    'tp_sexo', 'tp_estadio', 'vl_campos_irradiados']


@admin.register(Descricao)
class DescricaoAdmin(admin.ModelAdmin):
    list_display = ['co_procedimento', 'dt_competencia']


@admin.register(DescricaoDetalhe)
class DescricaoDetalheAdmin(admin.ModelAdmin):
    list_display = ['co_detalhe', 'dt_competencia']


@admin.register(Detalhe)
class DetalheAdmin(admin.ModelAdmin):
    list_display = ['co_detalhe', 'no_detalhe', 'dt_competencia']


@admin.register(Financiamento)
class FinanciamentoAdmin(admin.ModelAdmin):
    list_display = ['co_financiamento', 'no_financiamento', 'dt_competencia']


@admin.register(FormaOrganizacao)
class FormaOrganizacaoAdmin(admin.ModelAdmin):
    list_display = ['co_grupo', 'co_sub_grupo',
                    'co_forma_organizacao', 'no_forma_organizacao', 'dt_competencia']


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ['co_grupo', 'no_grupo', 'dt_competencia']


@admin.register(GrupoHabilitacao)
class GrupoHabilitacaoAdmin(admin.ModelAdmin):
    list_display = ['nu_grupo_habilitacao',
                    'no_grupo_habilitacao', 'ds_grupo_habilitacao']


@admin.register(Habilitacao)
class HabilitacaoAdmin(admin.ModelAdmin):
    list_display = ['co_habilitacao', 'no_habilitacao', 'dt_competencia']


@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ['co_ocupacao', 'no_ocupacao']


@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ['co_procedimento', 'no_procedimento',
                    'tp_complexidade', 'tp_sexo', 'dt_competencia']


@admin.register(ProcedimentoOcupacao)
class ProcedimentoOcupacaoAdmin(admin.ModelAdmin):
    list_display = ['co_procedimento', 'co_ocupacao', 'dt_competencia']


@admin.register(ProcedimentoRegraCondicionada)
class ProcedimentoRegraCondicionadaAdmin(admin.ModelAdmin):
    list_display = ['co_regra_condicionada', 'co_procedimento']


@admin.register(ProcedimentoSiaSih)
class ProcedimentoSiaSihAdmin(admin.ModelAdmin):
    list_display = ['co_procedimento',
                    'co_procedimento_sia_sih', 'dt_competencia']


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ['co_registro', 'no_registro', 'dt_competencia']


@admin.register(RegraCondicionada)
class RegraCondicionadaAdmin(admin.ModelAdmin):
    list_display = ['co_regra_condicionada',
                    'no_regra_condicionada', 'ds_regra_condicionada']


@admin.register(Rubrica)
class RubricaAdmin(admin.ModelAdmin):
    list_display = ['co_rubrica', 'no_rubrica', 'dt_competencia']


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['co_servico', 'no_servico', 'dt_competencia']


@admin.register(ServicoClassificacao)
class ServicoClassificacaoAdmin(admin.ModelAdmin):
    list_display = ['co_classificacao', 'co_servico',
                    'no_classificacao', 'dt_competencia']


@admin.register(SiaSih)
class SiaSihAdmin(admin.ModelAdmin):
    list_display = ['co_procedimento_sia_sih',
                    'no_procedimento_sia_sih', 'tp_procedimento', 'dt_competencia']


@admin.register(SubGrupo)
class SubGrupoAdmin(admin.ModelAdmin):
    list_display = ['co_grupo', 'co_sub_grupo',
                    'no_sub_grupo', 'dt_competencia']


@admin.register(TipoLeito)
class TipoLeitAdmin(admin.ModelAdmin):
    list_display = ['co_tipo_leito', 'no_tipo_leito', 'dt_competencia']
