# Poscomp Classification

Este projeto visa aplicar o processo de Knowledge Discovery in Databases (KDD) para a mineração de dados no conjunto de dados sobre a prova de POSCOMP.

O objetivo do projeto é fazer a classificação da linha de pesquisa de cada candidato de acordo com as informações da sua prova. 

Para fazer a classifação foi criado a feature “area” usando o atributo “especialidade” - campo em que o candidato preencheu na hora do cadastro da prova - em que as diversas opções de especialidade foram mapeadas para uma das quatro linhas de pesquisa do [PPGCOMP-UFPA](https://ppgcc.propesp.ufpa.br/index.php/br/programa/areas-de-concentracao-e-linhas-de-pesquisa). Aquelas especialidades que não se encaixaram nas quatro áreas do PPGCOMP-UFPA foram mapeadas para a linha de pesquisa denominada "Demais áreas".

O artigo de [Costa, Ferreira e Santos, 2024](https://www.tecsi.org/contecsi/index.php/contecsi/20CONTECSI/paper/view/7291) foi usado como a base para a realização desse projeto.

---

# Etapas do Projeto

O projeto se baseiou totalmente na metodologia KDD em que foi realizado as seguintes etapas:

- Seleção
- Pré-processamento
- Transformação
- Mineração de Dados
- Avaliação

---

# Tecnologias Usadas

- Python 
- Pandas
- Matplotlib e Seaborn
- Scikit-Learn
- Jupyter Notebook
