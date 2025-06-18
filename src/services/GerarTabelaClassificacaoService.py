from ..repositories.campeonatoRepository import CampeonatoRepository
from ..models.tabelaTime                import TabelaTime

class GerarTabelaClassificacaoService:
    def __init__(self, session):
        self.repo = CampeonatoRepository(session)

    def GerarTabela(self, campeonato_id):
        campeonato = self.repo.buscar_por_id(campeonato_id)
        tabela = {}

        for partida in campeonato.partidas:
            if not partida.resultado:
                continue

            mandante = partida.mandante
            visitante = partida.visitante
            resultado = partida.resultado

            for time in [mandante, visitante]:
                if time.id not in tabela:
                    tabela[time.id] = TabelaTime(time)

            t_m = tabela[mandante.id]
            t_v = tabela[visitante.id]

            gols_m = resultado.num_gols_mandante
            gols_v = resultado.num_gols_visitante

            t_m.gols_pro += gols_m
            t_m.gols_contra += gols_v

            t_v.gols_pro += gols_v
            t_v.gols_contra += gols_m

            t_m.pontos += resultado.get_pontuacao_mandante()
            t_v.pontos += resultado.get_pontuacao_visitante()

            if resultado.jogo_saiu_empatado():
                t_m.empates += 1
                t_v.empates += 1
            elif gols_m > gols_v:
                t_m.vitorias += 1
                t_v.derrotas += 1
            else:
                t_v.vitorias += 1
                t_m.derrotas += 1

        return sorted(
            tabela.values(),
            key=lambda t: (t.pontos, t.vitorias, t.saldo_gols, t.gols_pro),
            reverse=True
        )