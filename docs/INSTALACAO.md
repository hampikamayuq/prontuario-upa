# Instalação por plataforma

## ChatGPT

1. Baixe `dist/prontuario-upa-chatgpt.zip`.
2. Se sua conta/ambiente oferecer importação de plugins, importe o ZIP por esse recurso.
3. Ative o Prontuário UPA e solicite uma admissão ou evolução com dados fictícios para conferir o resultado.

A disponibilidade da importação depende do produto e da conta. Anexar o ZIP a uma conversa não instala automaticamente um plugin. Como alternativa manual, use o conteúdo de `gemini/instrucoes.txt` ou `gemini/instrucoes.md` nas instruções de um projeto ou assistente personalizado que aceite esse volume de texto, ou como arquivo de referência com uma instrução explícita para seguir o modelo. Isso não equivale à instalação nativa.

## Claude

1. Baixe `dist/prontuario-upa-claude.zip`.
2. Na área de Skills/Habilidades, escolha a opção de enviar uma Skill personalizada, quando disponível.
3. Envie o ZIP e ative a Skill.
4. Solicite: “Faça uma admissão no modelo Prontuário UPA com os dados que vou enviar”.

O ZIP contém `prontuario-upa/SKILL.md`. A disponibilidade de Skills depende do plano e das permissões da organização.

Referência oficial: https://support.claude.com/en/articles/12512180-use-skills-in-claude

## Gemini (aplicativo) — Habilidades

Fluxo conferido nas capturas do aplicativo fornecidas pelo mantenedor: a aba **Habilidades** mostra as habilidades instaladas e o botão **+** oferece **Criar com o Gemini** e **Criar manualmente**. Os campos do editor e o botão de conclusão não aparecem nas capturas.

### Criar com o Gemini e anexar o arquivo

1. Baixe [gemini/instrucoes.txt](../gemini/instrucoes.txt), que abre em leitores de texto comuns. Também está disponível a versão [Markdown](../gemini/instrucoes.md), com o mesmo conteúdo.
2. No aplicativo, abra **Habilidades → + → Criar com o Gemini**.
3. Anexe o arquivo `instrucoes.txt` (ou `instrucoes.md`) e envie:

   > Crie uma habilidade chamada prontuario-upa usando o arquivo anexado como fonte das instruções. Preserve integralmente as regras clínicas, a estrutura dos registros e as orientações de revisão médica. Não resuma nem omita regras.

4. Revise as instruções propostas pelo Gemini e conclua a criação pelo controle disponível no aplicativo.
5. Confira se `prontuario-upa` aparece em **Instaladas** e teste com um caso fictício.

A opção de anexar o arquivo nesse fluxo foi informada pelo mantenedor. Confira o texto gerado antes de salvar, pois o Gemini pode reformular as instruções.

### Criar manualmente

1. Abra a aba **Habilidades** no aplicativo Gemini.
2. Toque em **+** e selecione **Criar manualmente**.
3. Use `prontuario-upa` como nome, se o editor solicitar um nome.
4. Abra [gemini/instrucoes.txt](../gemini/instrucoes.txt) (ou a [versão Markdown](../gemini/instrucoes.md)) e copie todo o conteúdo para a área de instruções da habilidade.
5. Se houver um campo de descrição, use: “Organiza admissão, evolução e discussão clínica em português no modelo UPA quando o médico solicita esses registros”.
6. Conclua a criação pelo controle disponível no editor e confira se `prontuario-upa` aparece em **Instaladas**.
7. Em uma conversa, solicite: “Use a habilidade prontuario-upa para fazer uma admissão com os dados fictícios que vou enviar”. Confira se ela é aplicada ao resultado.

Se `prontuario-upa` já estiver instalada, abra as opções da habilidade pelo menu **…** e procure a opção de edição para atualizar as instruções. As opções desse menu ainda precisam ser conferidas no aplicativo.

Os arquivos `instrucoes.txt` e `instrucoes.md` têm conteúdo idêntico e contêm as instruções para anexar em **Criar com o Gemini** ou copiar e colar em **Criar manualmente**. As capturas não mostram importação de ZIP; o pacote `prontuario-upa-gemini.zip` abaixo é destinado ao Gemini CLI. A disponibilidade da tela Habilidades pode variar conforme a conta e a versão do aplicativo.

## Gemini CLI (opcional) — habilidade (Agent Skill)

Requer o Gemini CLI instalado, autenticado e com suporte a Agent Skills. A instalação descrita aqui é para o CLI; a interface web de Gems é um produto diferente.

1. Instale a habilidade a partir deste repositório:

   ```sh
   gemini skills install https://github.com/hampikamayuq/prontuario-upa.git --path gemini/prontuario-upa
   ```

2. No Gemini CLI, execute `/skills reload` e `/skills list` e confirme que `prontuario-upa` aparece na lista.
3. Solicite: “Use a habilidade prontuario-upa para fazer uma admissão com os dados fictícios que vou enviar”.
4. Quando o Gemini solicitar autorização para ativar a habilidade, confira os detalhes e confirme.

Para instalar a partir do download, baixe `dist/prontuario-upa-gemini.zip`, extraia-o e execute `gemini skills install ./prontuario-upa` no diretório onde extraiu o ZIP. A pasta contém `SKILL.md` e `LICENSE`.

Referência oficial: https://geminicli.com/docs/cli/skills/

## Verificação antes do uso

As adaptações preservam o conteúdo-base 0.1.4, mas ainda não foram testadas em sessões de Claude e Gemini. Confira o modelo com casos fictícios, inclusive pediatria, dados incompletos e exames alterados. Revise os campos de exame físico preenchidos automaticamente. Nenhuma instalação garante resultados idênticos entre modelos.

## Atualizar e gerar pacotes

Edite `skills/instructions/SKILL.md` como fonte principal e execute `python3 scripts/package.py`. Reimporte os pacotes de ChatGPT e Claude. No aplicativo Gemini, atualize o texto da habilidade com o conteúdo de `gemini/instrucoes.txt` ou `gemini/instrucoes.md`. No Gemini CLI, desinstale a versão anterior com `gemini skills uninstall prontuario-upa`, repita a instalação e execute `/skills reload`. Não publique dados reais de pacientes neste repositório.
