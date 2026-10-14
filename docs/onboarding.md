# Il tuo impianto, in una chat

L'assistente EnergyInCloud risponde alle tue domande sull'impianto solare e sull'accumulo:
produzione, consumo, autoconsumo, risparmio, batteria, collegamento e qualità dei dati, report del
periodo. Ti spiega anche cosa significa un dato o un termine, come autoconsumo, autosufficienza o stato di
salute della batteria.

Non configura l'impianto e non risponde su impianti che non sono tuoi. Non fa diagnosi, non indica
cause né consigli di manutenzione e non fa previsioni: ti mostra i dati e ciò che lo strumento dice
di essi.

## Installa su Claude

- Dalla directory di Claude: <https://claude.ai/directory/connectors/energyincloud>
- Oppure aggiungilo come connettore personalizzato con questo link, che compila già i campi:
  <https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=EnergyInCloud&connectorUrl=https%3A%2F%2Fmcp.cloud.energyincloud.com%2Fmcp>

## Altri assistenti

Se il tuo assistente non ha ancora EnergyInCloud nel proprio elenco, puoi collegarlo a mano. Ti servono
l'indirizzo del connettore, `https://mcp.cloud.energyincloud.com/mcp`, e il tuo account EnergyInCloud:
al primo collegamento ti viene chiesto di accedere. Le voci di menu possono cambiare con gli
aggiornamenti dell'assistente.

### ChatGPT

- Non è ancora disponibile nell'elenco di ChatGPT. Questa sezione sarà aggiornata con il link
  quando lo sarà.

### Mistral (Le Chat)

- Il connettore lo aggiunge l'amministratore dello spazio di lavoro; con un account personale sei tu
  l'amministratore.
- Vai in **Connectors** → **+ Add Connector** → **Custom MCP Connector**. Scrivi un nome senza spazi
  (per esempio `EnergyInCloud`), incolla l'indirizzo e premi **Connect**.
- Accedi con il tuo account EnergyInCloud quando richiesto. Gli altri membri dello spazio di lavoro
  si collegano ciascuno con il proprio account e vedono solo i propri impianti.
- Facoltativo: in **Context** → **Skills** → **New Skill** incolla il testo di
  [`skills/energyincloud/SKILL.md`](../skills/energyincloud/SKILL.md). Aiuta l'assistente a rispondere
  nel modo giusto.

### Microsoft Copilot Studio

- Serve un ambiente Copilot Studio; l'agente lo crea chi ha la licenza Copilot Studio. Chi lo usa
  poi non ha bisogno di licenze aggiuntive.
- Nell'agente apri **Tools** → **Add a tool** → **New tool** → **Model Context Protocol**.
  Inserisci nome, descrizione e indirizzo; come autenticazione scegli **OAuth 2.0** → **Manual**.
- Nei campi di **Manual** inserisci i dati del client che EnergyInCloud ti fornisce su richiesta
  all'assistenza: ID e segreto del client, indirizzi di autorizzazione e di token e scopes.
- Premi **Create**: il passaggio mostra un indirizzo di callback. Comunicalo all'assistenza, che lo
  abilita sul client; solo dopo, in **Create a new connection**, accedi con il tuo account
  EnergyInCloud e premi **Add to agent**.
- Per usarlo in Teams e Microsoft 365 Copilot pubblica l'agente (**Channels** → **Teams and Microsoft
  Copilot**). Per tutta l'organizzazione serve l'approvazione dell'amministratore Microsoft 365, e le
  politiche di protezione dei dati dell'organizzazione devono consentire il connettore.

### Perplexity

- In **Account settings** → **Connectors** scegli **+ Custom connector** → **Remote**.
- Inserisci il nome e l'indirizzo, come autenticazione **OAuth**, come trasporto **Streamable HTTP**.
  Conferma l'avviso e premi **Add**.
- Apri la scheda del connettore, accedi con il tuo account EnergyInCloud e attivalo.
- I connettori remoti possono essere riservati agli abbonamenti a pagamento; per l'organizzazione
  l'amministratore può condividerlo da **Enterprise settings** → **Permissions** → **Connectors permissions**.

### Grok

- Su grok.com apri **Connectors** → **New Connector** → **Custom**, inserisci l'indirizzo del
  connettore e completa l'accesso con il tuo account EnergyInCloud.
- Se la voce non compare, il tuo piano o il tuo spazio di lavoro non permette connettori personalizzati:
  in un account aziendale deve abilitarli l'amministratore.

## Tre domande da copiare

Incolla una di queste nella chat, senza altro:

1. `come va l'impianto oggi`
2. `quanto ho prodotto a settembre`
3. `quanto ho risparmiato`

## Allarmi

L'elenco degli allarmi e i loro dettagli sono nel portale. L'assistente ti dà solo il numero per
gravità e il tempo di blocco.

## Assistenza

Per contattare l'assistenza: <https://mycloud.energy/assistenza/>. Indica l'impianto e il periodo a cui ti riferisci.
