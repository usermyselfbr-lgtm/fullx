# 09 · /white-label: acesso antecipado ao white label

- **Rota:** `/white-label/`. **Fonte:** `paginas/p09_software_whitelabel.py`. **Funil do formulário:** `software-whitelabel` (3 passos, `fid=form`, evento `Lead`).
- **Mercado:** agências de marketing e consultorias no Brasil que vendem serviço recorrente.
- **ICP:** dono de agência ou consultoria com carteira de clientes que quer oferecer software com a própria marca. Já conhece o produto e decide a compra (B2B).
- **Objetivo:** pedir demonstração e entrar na lista de acesso antecipado ao white label do CRM e da cobrança.

## Fase 1: diagnóstico (dist + baseline `screens/baseline/white-label-*.png`)
- **Copy:** o H1 "Seu próprio software de CRM, cobrança e IA. Com a sua marca." vende como pronto algo que não existe (FONTE 3b: white label "só plano/oferta", sem cliente; IA comercial inexistente). Os 4 módulos vêm do bento compartilhado, com "Gateway de pagamento" (proibido: é Asaas por baixo), "Painel de inadimplência" e "IA comercial". Os passos prometem domínio próprio, e-mails com seu nome, suporte de nível 2 (sem fonte). A seção de planos tem `[R$X]`, `[10]`, `[50]`, `[Sob consulta]`. A FAQ tem `[PRAZO]` e `[DESCREVA HOSPEDAGEM, BACKUP E LGPD]`. "Demonstração de 30 minutos" e "prévia com o seu logo" não têm fonte.
- **Conversão:** o CTA "Agendar demonstração" leva ao formulário, e a conclusão abre o Calendly, que não existe (`CALENDLY_URL` vazio). No ar o visitante veria "Configure CALENDLY_URL no topo do arquivo". O passo 2 diz "Define o plano ideal" e não há plano. O rodapé completo lista "Gateway de pagamento" e "IA comercial" e mostra `[RAZÃO SOCIAL · CNPJ]`.
- **Técnica (baseline):** `todo:8`, placeholders `[R$X] [10] [50] [Sob consulta] [RAZÃO SOCIAL · CNPJ]`, overflow 0, console 0, LCP 272 ms.

## Fase 2: research
**FATOS (pode usar)**
- CRM próprio em produção: pipeline/kanban, formulário multi-etapa que pontua o lead (filtro MQL/SQL), WhatsApp dentro do CRM (inbox, resposta com texto/foto/áudio, cadência), cargos SDR/Closer/Gestor (FONTE 3b).
- Isolamento multi-tenant testado no código ("teste de orgId", CI) com 1 org em produção (FONTE 3b, linha White label).
- Sistema de cobrança próprio: régua de cobrança com disparos por WhatsApp, dívida D+30, integrado ao Asaas (FONTE 3b). A régua está pronta e desligada por decisão do financeiro: por isso não pode virar "em uso" nem "painel de inadimplência".
- IA operacional: protótipo (base de processos que responde o time), sem registro de uso pelo time (FONTE 3b).
- Frases publicadas: "Você vê a tela, não a teoria." / "Eu mostro o que roda, não o que li." / "O CRM, o formulário que pontua o lead e o sistema de cobrança… foram construídos para a minha operação." (FONTE 1 e 7).
- Números liberados: "+R$10 milhões em tráfego gerenciado", "+2.300 clientes de serviço gerados" (linha `PROOF` do `_comum.py`).
- Resposta em "até 24 horas úteis" quando não há agenda (decisão do orquestrador).

**HIPÓTESES (não afirmar)**
- Licença white label a R$197–497/mês (RMBC, hipótese 4). O white label deve ser vendido como lista ou demonstração (hipótese 4).
- Que o software com a marca da agência ajuda a reter o cliente: vale como argumento lógico, nunca como dado.

**AUSENTES**
- Preço, planos, limite de clientes, prazo de implantação, texto de LGPD, política de backup, domínio próprio, e-mail com a marca, nível de suporte, data de abertura do white label, duração da demonstração, Calendly.

## Fase 3: brief RMBC
- **Avatar:** dono de agência ou consultoria com clientes recorrentes que já pensou em vender software com o próprio nome e desconfia de white label genérico.
- **Nível de consciência:** consciente do produto (já sabe o que é white label e compara fornecedores).
- **Dor central:** "Cliente cancela em 3 meses." O serviço dele é trocável e falta uma recorrência que prenda o cliente. Por isso pensa em software, mas não quer revender uma tela que nunca vendeu nada.
- **Inimigo:** o white label de apresentação: painel bonito, sem operação real por trás, que a agência revende e depois tem de explicar.
- **Mecanismo do problema:** o fornecedor nunca usou o sistema para vender e cobrar. Quem descobre as falhas é o seu cliente, com a sua marca na tela.
- **Mecanismo da solução:** primeiro roda na nossa agência, depois ganha a sua marca. O CRM e a cobrança são usados na operação da Full10X antes de virar licença.
- **Big idea:** "Primeiro roda na nossa agência. Depois leva a sua marca."
- **Promessa defensável:** ver hoje, na tela, o CRM e a cobrança que rodam na nossa agência, e estar entre os primeiros a revendê-los com a sua marca quando o white label abrir.
- **3 provas:** (1) CRM em produção com pipeline, formulário que pontua, tarefas do SDR e WhatsApp dentro; (2) sistema de cobrança próprio com régua por WhatsApp sobre o Asaas; (3) separação de dados por agência já testada no código. Mais a linha PROOF (+R$10 milhões em tráfego, +2.300 clientes de serviço).
- **Objeções:** "Já posso contratar?" → ainda não; a lista é para a primeira leva. "Quanto custa?" → preço não definido; entrar na lista não custa nada. "Preciso programar?" → não, a Full10X configura. "Posso cobrar o que quiser?" → o preço ao seu cliente é seu. "Meus dados ficam seguros?" → nuvem e separação por agência testada; termos de LGPD e backup por escrito antes de qualquer contrato. "Tem IA que vende sozinha?" → não existe; não vendemos o que não roda.
- **Oferta:** demonstração do CRM e da cobrança rodando + lugar na lista de acesso antecipado. Sem preço, sem prazo, sem garantia.
- **CTA:** "Pedir demonstração" (conclusão: "Vamos montar sua demonstração. O time fala com você em até 24 horas úteis.").
- **Arquitetura:** (1) Hero: o que é, para quem, estado real (acesso antecipado), CTA, PROOF, interface com "Sua Agência". (2) Problema/tese: por que white label de apresentação queima a sua marca e por que o nosso roda primeiro aqui. (3) `#modulos`: o que já roda (CRM, cobrança) e o que está em construção (IA operacional). (4) Como funciona o acesso antecipado em 3 passos. (5) Para quem é / não é: filtra quem precisa de sistema pronto este mês ou de IA que vende. (6) Formulário + FAQ verdadeira.

## Fase 4: 15 headlines
1. Revenda o CRM que roda na nossa agência. Com a sua marca. *(promessa)*
2. Primeiro roda na nossa agência. Depois leva a sua marca. *(mecanismo)*
3. Não revenda tela de apresentação. Revenda o sistema que vende e cobra aqui dentro. *(contrarian; usa a estrutura "não X, Y")*
4. Seu cliente cancela no 3º mês. Um CRM com o seu nome dá a ele mais um motivo para ficar. *(problema-solução)*
5. O CRM e a régua de cobrança da Full10X, com o seu logo, para os seus clientes. *(especificidade)*
6. Construímos o CRM para a nossa agência. Agora estamos abrindo para a sua marca. *(história)*
7. White label só depois de rodar aqui: entre na lista da primeira leva. *(mecanismo + lista)*
8. Pipeline, formulário que pontua, WhatsApp e cobrança. Com o seu nome na tela. *(especificidade)*
9. Software com a sua marca, testado primeiro na nossa operação. *(mecanismo)*
10. Venda software junto com o serviço, sem escrever uma linha de código. *(promessa)*
11. A ferramenta que o seu cliente usa todo dia pode ter o seu nome. *(desejo)*
12. Antes de levar a sua marca, o sistema passa pela nossa agência. *(mecanismo)*
13. Quem revende software que nunca usou descobre os defeitos pelo cliente. *(problema)*
14. Veja o CRM rodando hoje. Revenda com a sua marca quando abrir. *(promessa honesta + estado)*
15. O sistema que fecha e cobra na nossa agência, pronto para levar o nome da sua. *(especificidade; "pronto" é falso hoje)*

**Escolhida:** H1 = nº 1 "Revenda o CRM que roda na nossa agência. Com a sua marca.", com a eyebrow "Acesso antecipado ao white label" e um lead que explica o estado real. Justificativa: diz o produto, a prova (roda aqui) e o benefício em 11 palavras para um leitor que já sabe o que é white label. A nº 2 vira o H2 da tese.

## Fase 5: copy completa
Implementada como está no `.py` (fonte única do texto). Peças-chave:
- **Eyebrow:** Acesso antecipado ao white label
- **H1:** Revenda o CRM que roda na nossa agência. Com a sua marca.
- **Lead:** O CRM e o sistema de cobrança que usamos para vender e cobrar na Full10X vão ganhar versão com o seu logo e as suas cores, para você oferecer aos seus clientes. O white label ainda não está à venda. Peça a demonstração e entre na lista da primeira leva.
- **CTAs:** "Pedir demonstração" (hero, topo, barra do celular) · "Ver o que já roda" (âncora `#modulos`).
- **Tese (H2):** Primeiro roda na nossa agência. Depois leva a sua marca. Três cartões: o problema do white label de apresentação, o que já roda aqui, por que lista em vez de venda.
- **Módulos (H2):** O que já roda e o que ainda estamos construindo. CRM (em uso na nossa operação), Sistema de cobrança (régua pronta, roda sobre o Asaas), IA operacional (em construção, protótipo). A IA comercial não aparece.
- **Passos (H2):** Como funciona o acesso antecipado. 1. Você responde 3 perguntas. 2. O time mostra o CRM e a cobrança rodando. 3. Quando abrir, a lista é chamada primeiro e a Full10X configura com a sua marca.
- **Para quem:** é para você se tem clientes pagando todo mês, quer vender software junto do serviço e prefere esperar a versão pronta. Não é para você se precisa do sistema com a sua marca este mês, se procura IA que vende sozinha ou se ainda não tem clientes.
- **Formulário:** título "Peça sua demonstração"; passo 2 com o hint "Ajuda a mostrar o sistema no volume da sua carteira."; módulos honestos ("Sistema de cobrança (régua por WhatsApp)", "IA operacional (em construção)", "IA comercial (ainda não existe)"); botão final "Pedir demonstração"; conclusão "Vamos montar sua demonstração. O time fala com você em até 24 horas úteis."
- **FAQ local `FAQ_09`:** Já posso contratar? · Quanto vai custar? · Preciso saber programar? · Posso cobrar o que eu quiser do meu cliente? · Meus dados e os dos meus clientes ficam seguros? · E a IA que atende no WhatsApp?

## Fase 6: implementação
- A página foi reescrita no `.py`. Saem a seção `#planos` (inteira, sem `data-draft`, para não deixar `.todo` no DOM) e o `soft_cards.replace(...)`.
- Entram a lista local `SOFT_09` (CRM, Sistema de cobrança, IA operacional marcada "em construção", sem IA comercial), a tese em `grid g3` + `card` e o bloco "Para quem é" com `compare`. A FAQ local `FAQ_09` não tem `[PRAZO]` nem `[LGPD]`.
- **Desvio da instrução `bento(SOFT_09, …)`:** `bento()` no `_sistema.py` percorre a ordem fixa `crm, pay, chat, ops` e daria `KeyError` sem o módulo `chat` (IA comercial). Por isso criei a função local `bento09()` com a mesma marcação (`tile spot`, `ART[...]`, chips, link `#form`). A IA operacional ocupa a linha inteira (`style="grid-column:1/-1"`).
- **Formulário:** `name=`, `value=`, `data-s`, `data-funil`, `data-evento` e `fid` estão intactos. Mudaram só legendas, hints, labels, o título do card e o botão final ("Pedir demonstração"). A opção `ia-com` continua no formulário com o label "IA comercial (ainda não existe)", para não quebrar o contrato.
- **`done9`:** a confirmação agora é "Vamos montar sua demonstração. O time fala com você em até 24 horas úteis.", sem `data-calendly` (com `CALENDLY_URL` vazio, o sistema exibiria "Configure CALENDLY_URL"). O comentário no `.py` diz como religar a agenda.
- **Mantidos:** `app_mock('wl', white_label=True)` e `strip()`. O rodapé passou para `footer('f10', full=False)`, porque o rodapé completo lista "Gateway de pagamento" e "IA comercial" e mostra `[RAZÃO SOCIAL · CNPJ]`.
- Meta title e description reescritos sem gateway nem IA.

## Fase 7: ajuste visual
- `node qa/screens.mjs 09-v1 white-label` → `white-label  overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:273ms`. Conferi os PNGs de 1440 e 390: o hero tem H1 de 5 linhas no desktop e CTA e PROOF visíveis, os cards da tese têm alturas iguais e os tiles quebram sem cortar texto no 390. Não precisei de correção visual.
- `node qa/screens.mjs 09-v2 white-label` (depois da revisão editorial) → `white-label  overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:233ms`.

## Fase 8: engenharia
- O `grep` no `dist/white-label/index.html` deu: `h1= 1 h2= 5`; `id="form"` 1, `id="modulos"` 1; `<img>` sem `alt`: 0 (a página não tem `<img>`, a interface é HTML com `aria-hidden`).
- Todos os CTAs (topo, hero, links dos tiles, barra do celular) levam a `#form`. "Ver o que já roda" leva a `#modulos`. O relatório não acusa links quebrados nem erros de console.
- Termos que restam no HTML: "IA comercial" aparece 2× (item de menu do `app_mock` compartilhado e a opção do formulário marcada "ainda não existe"). "Calendly" aparece no JS compartilhado e no chip do `strip()`. Não há `gateway`, `[R$`, `PRAZO` nem "30 minutos".

## Fase 9: revisão editorial
- Li a página na ordem do visitante. Troquei a resposta sobre IA no WhatsApp: a frase do Julio em 1ª pessoa ("Eu mostro o que roda…") destoava do "nós" da página e virou "Aqui só entra o que já roda."
- Checklist do Georgi: a primeira frase se sustenta sozinha. Toda afirmação sobre o produto tem fonte na FONTE 3b. Nada de preço, prazo, garantia ou escassez numérica. Os números são só os da linha PROOF. Nenhum clichê da lista proibida, e cada CTA diz o que acontece.

## Fase 10: documentação
- **Estratégia aplicada:** de "SaaS pronto com planos" para "acesso antecipado + demonstração do que já roda". A honestidade virou o argumento: "Primeiro roda na nossa agência. Depois leva a sua marca."
- **Principais mudanças (antes → depois):**
  - H1: "Seu próprio software de CRM, cobrança e IA. Com a sua marca." → "Revenda o CRM que roda na nossa agência. Com a sua marca."
  - CTA: "Agendar demonstração" → "Pedir demonstração"
  - Módulos: 4 (com gateway e IA comercial) → 3 (CRM e cobrança em uso, IA operacional em construção)
  - Planos com `[R$X]` → seção removida
  - FAQ com `[PRAZO]`/`[LGPD]` → 6 respostas verdadeiras
  - Conclusão: Calendly → confirmação em até 24 horas úteis
- **Testes executados (saída real):** `python3 _gerar.py` → `12 páginas em /Users/juliomyself/projetos/fullx-funis/dist` (rc 0); `grep -c 'class="todo"' dist/white-label/index.html` → `0`; QA v2 → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:233ms`.
- **Bloqueios:** nenhum.
- **Pendências para o Julio:**
  1. Decidir se e quando o white label abre, com preço, limite de clientes e prazo de implantação. Sem isso a página fica como lista de espera.
  2. Escrever a política de LGPD e a de backup do CRM e da cobrança. A FAQ promete esse texto "por escrito antes de qualquer contrato".
  3. Gravar o vídeo ou print real do CRM para trocar o `app_mock` (os KPIs são ilustrativos e o menu mostra "IA comercial").
  4. Confirmar as integrações do `strip()` (Calendly, Make) ou trocar os itens.
  5. Definir quem atende os pedidos de demonstração em até 24 horas úteis.
- **Sugestões para arquivos compartilhados:**
  - `bento()` deveria aceitar um subconjunto de módulos (hoje dá `KeyError` sem `chat`).
  - `app_mock()` deveria receber um parâmetro para esconder o item "IA comercial" do menu.
  - `strip()` deveria receber a lista de integrações.
  - O rodapé completo deveria tirar "Gateway de pagamento" e "IA comercial" e resolver `[RAZÃO SOCIAL · CNPJ]`.
- **Checklist (marcado só o verificado):**
  - COPY:
    - [x] promessa defensável
    - [x] mecanismo nomeado
    - [x] provas só da FONTE
    - [x] objeções reais na FAQ
    - [x] CTA com verbo e consequência
    - [x] sem clichê
    - [x] sem preço, prazo ou garantia inventados
    - [x] nenhum produto inexistente vendido como disponível
  - ENGENHARIA:
    - [x] 1 h1
    - [x] âncoras `#form` e `#modulos` existem
    - [x] contrato do formulário intacto
    - [x] `todo:0 placeholders:0 overflow:0 console:0`
    - [x] sem links quebrados
    - [ ] envio real do formulário não testado (`WEBHOOK_URL` vazio, modo demonstração)
  - O documento com a "seção 19" citada no brief não foi encontrado em `docs/landing-audit/`. O checklist acima segue as fases do brief.
- **Status final:** CONCLUÍDA.
