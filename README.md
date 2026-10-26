# EnergyInCloud

Assistente per chi ha un impianto solare con accumulo gestito da EnergyInCloud, e per chi lo
installa o lo distribuisce: risponde alle domande sugli impianti usando solo i dati del portale,
collegati tramite connettore. Tre skill, una per ruolo (cliente, installatore, distributore): si
attiva quella del tuo account.

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

- Dalla directory di Claude: installa il plugin e collega il connettore dalla sua scheda
  Connectors con il tuo account EnergyInCloud.
- Senza directory, in due passi:
  1. scarica la skill del tuo ruolo dal portale EnergyInCloud, dopo il login, all'indirizzo
     `/api/assistant/skill.zip`, e caricala in Customize → Skills;
  2. aggiungi il connettore personalizzato con
     [questo link](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=EnergyInCloud&connectorUrl=https%3A%2F%2Fmcp.cloud.energyincloud.com%2Fmcp)
     (nome `EnergyInCloud`, URL `https://mcp.cloud.energyincloud.com/mcp`) e accedi con il tuo
     account EnergyInCloud.

### ChatGPT

- Dalla directory dei plugin di ChatGPT.
- Su piani Business ed Enterprise puoi anche caricare la skill del tuo ruolo, scaricata dal
  portale come sopra.

### Mistral e altri assistenti

- Connettore: URL `https://mcp.cloud.energyincloud.com/mcp`, accesso con il tuo account.
- Skill: quella del tuo ruolo, scaricata dal portale come sopra.

### Microsoft 365 Copilot

- Dall'Agent Store di Microsoft 365 Copilot, quando sarà disponibile: aggiungi l'agente EnergyInCloud
  e accedi con il tuo account EnergyInCloud.

## Allarmi

L'elenco degli allarmi, con il dettaglio, è nel portale EnergyInCloud. L'assistente riporta solo
conteggi per gravità e tempo di blocco.

## Guida per i clienti

Documentazione per i clienti: <https://mycloud.energy/documentazione/> (testo sorgente in
`docs/onboarding.md`).

## Assistenza

Per contattare l'assistenza: <https://mycloud.energy/assistenza/>. Indica l'impianto e il periodo a cui ti riferisci.

## Contenuto del repository

- `.claude-plugin/plugin.json`: manifesto del plugin.
- `.mcp.json`: server MCP remoto (streamable HTTP, OAuth lato server).
- `skills/<ruolo>/`: le tre skill (`SKILL.md` e `references/`), `commands/`: le richieste
  pronte, e `copilot/appPackage/instruction.txt`: le istruzioni dell'agente per Microsoft 365
  Copilot (progetto Agents Toolkit in `copilot/`). Sono copie dell'albero generato in
  `triage-api/plugins/energyincloud/`: si modificano lì (`triage-api/src/app/assistant/`), mai qui.
- `tests/`: test di contratto delle skill e delle istruzioni Copilot, compresa l'identità con
  l'albero generato quando `triage-api` è accanto a questo repository (`uv run pytest`).

## Licenza

MIT, vedi [LICENSE](LICENSE).
