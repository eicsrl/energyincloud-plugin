# EnergyInCloud

Assistente per chi ha un impianto solare con accumulo gestito da EnergyInCloud: risponde alle
domande sull'impianto usando solo i dati del portale, collegati tramite connettore.

## Cosa fa

- Risponde su produzione, consumo, autoconsumo, risparmio, batteria, connettività, qualità dei dati
  e report di periodo, e spiega cosa significa una cifra.
- Parte sempre dai risultati degli strumenti: se uno strumento non segnala un guasto, un degrado o
  una prestazione scarsa, l'assistente non lo dichiara.

## Cosa non fa

- Non configura l'impianto, non dà il dettaglio degli allarmi (lo mostra il portale) e non risponde
  su impianti che l'utente non possiede.
- Non assegna etichette proprie (sano, critico, urgente), non indica cause, manutenzione o
  previsioni, e non confronta l'impianto con altri impianti "tipici".

## Installazione

### Claude

- Quando sarà disponibile nella directory di Claude: installa il plugin e autorizza il
  connettore.
- Oggi, in due passi:
  1. comprimi in ZIP la cartella `skills/energyincloud` e caricala in Customize → Skills;
  2. aggiungi il connettore personalizzato con
     [questo link](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=EnergyInCloud&connectorUrl=https%3A%2F%2Fmcp.cloud.energyincloud.com%2Fmcp)
     (nome `EnergyInCloud`, URL `https://mcp.cloud.energyincloud.com/mcp`) e accedi con il tuo
     account EnergyInCloud.

### ChatGPT

- Dalla directory dei plugin di ChatGPT.
- Il caricamento manuale della skill è possibile solo su piani Business ed Enterprise.

## Allarmi

L'elenco degli allarmi, con il dettaglio, è nel portale EnergyInCloud. L'assistente riporta solo
conteggi per gravità e tempo di blocco.

## Contenuto del repository

- `.claude-plugin/plugin.json`: manifesto del plugin.
- `.mcp.json`: server MCP remoto (streamable HTTP, OAuth lato server).
- `skills/energyincloud/`: la skill (`SKILL.md` e `references/`).
- `tests/`: test di contratto della skill (`uv run pytest`).

## Licenza

TODO(Alberto): licenza da decidere, vedi `LICENSE`.
