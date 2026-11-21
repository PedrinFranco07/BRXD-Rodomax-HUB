// ========================================
// DADOS DEMONSTRATIVOS
// ========================================

const demandas = [

    {
        cliente: "TransParaná Logística",
        email: "contato@transparana.com",
        origem: "Cascavel",
        destino: "Curitiba",
        valor: 1500.00,
        fonte: "CSV"
    },

    {
        cliente: "SulCargo Transportes",
        email: "contato@sulcargo.com",
        origem: "Toledo",
        destino: "Curitiba",
        valor: 2000.50,
        fonte: "CSV"
    },

    {
        cliente: "Expresso Oeste Cargas",
        email: "fretes@expressooeste.com",
        origem: "Foz do Iguaçu",
        destino: "Maringá",
        valor: 1850.00,
        fonte: "CSV"
    },

    {
        cliente: "NorteSul Distribuição",
        email: "comercial@nortesul.com",
        origem: "Cascavel",
        destino: "São Paulo",
        valor: 2500.00,
        fonte: "CSV"
    },

    {
        cliente: "Oeste Brasil Transportes",
        email: "contato@oestebrasil.com",
        origem: "Toledo",
        destino: "Londrina",
        valor: 1200.00,
        fonte: "CSV"
    },

    {
        cliente: "Grupo ViaCerta",
        email: "fretes@viacerta.com",
        origem: "Curitiba",
        destino: "São Paulo",
        valor: 3000.00,
        fonte: "CSV"
    },

    {
        cliente: "Paraná Cargo Express",
        email: "contato@paranacargo.com",
        origem: "Maringá",
        destino: "Cascavel",
        valor: 1750.00,
        fonte: "CSV"
    },

    {
        cliente: "FastRoute Logística",
        email: "json@fastroute.com",
        origem: "Cascavel",
        destino: "Curitiba",
        valor: 1800.00,
        fonte: "JSON"
    },

    {
        cliente: "Mercado Central Distribuição",
        email: "fretes@mercadocentral.com",
        origem: "Toledo",
        destino: "Maringá",
        valor: 1600.00,
        fonte: "JSON"
    },

    {
        cliente: "Cargas União",
        email: "contato@cargasuniao.com",
        origem: "Curitiba",
        destino: "Londrina",
        valor: 900.00,
        fonte: "XLSX"
    },

    {
        cliente: "TransParaná Logística",
        email: "contato@transparana.com",
        origem: "Cascavel",
        destino: "Curitiba",
        valor: 1500.00,
        fonte: "XLSX"
    },

    {
        cliente: "SulCargo Transportes",
        email: "contato@sulcargo.com",
        origem: "Toledo",
        destino: "Curitiba",
        valor: 2000.50,
        fonte: "XLSX"
    },

    {
        cliente: "Expresso Oeste Cargas",
        email: "fretes@expressooeste.com",
        origem: "Foz do Iguaçu",
        destino: "Maringá",
        valor: 1850.00,
        fonte: "XLSX"
    },

    {
        cliente: "NorteSul Distribuição",
        email: "comercial@nortesul.com",
        origem: "Cascavel",
        destino: "São Paulo",
        valor: 2500.00,
        fonte: "XLSX"
    },

    {
        cliente: "Oeste Brasil Transportes",
        email: "contato@oestebrasil.com",
        origem: "Toledo",
        destino: "Londrina",
        valor: 1200.00,
        fonte: "XLSX"
    },

    {
        cliente: "Grupo ViaCerta",
        email: "fretes@viacerta.com",
        origem: "Curitiba",
        destino: "São Paulo",
        valor: 3000.00,
        fonte: "XLSX"
    },

    {
        cliente: "Paraná Cargo Express",
        email: "contato@paranacargo.com",
        origem: "Maringá",
        destino: "Cascavel",
        valor: 1750.00,
        fonte: "XLSX"
    }

];



// ========================================
// VARIÁVEIS
// ========================================

let mostrarTodas = false;



// ========================================
// ELEMENTOS
// ========================================

const tabelaDemandas =
    document.getElementById("tabelaDemandas");

const tabelaTodasDemandas =
    document.getElementById("tabelaTodasDemandas");

const contadorDemandas =
    document.getElementById("contadorDemandas");

const btnVerTodas =
    document.getElementById("btnVerTodas");

const modal =
    document.getElementById("modalNovaDemanda");

const formDemanda =
    document.getElementById("formDemanda");



// ========================================
// FORMATAR MOEDA
// ========================================

function formatarMoeda(valor) {

    return valor.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
    });

}



// ========================================
// PEGAR INICIAIS
// ========================================

function pegarIniciais(nome) {

    const palavras =
        nome.trim().split(" ");

    if (palavras.length >= 2) {

        return (
            palavras[0][0] +
            palavras[1][0]
        ).toUpperCase();

    }

    return nome
        .substring(0, 2)
        .toUpperCase();

}



// ========================================
// CRIAR LINHA
// ========================================

function criarLinha(demanda) {

    const linha =
        document.createElement("tr");


    linha.innerHTML = `

        <td>

            <div class="cliente-info">

                <div class="cliente-avatar">
                    ${pegarIniciais(demanda.cliente)}
                </div>

                <div>

                    <strong>
                        ${demanda.cliente}
                    </strong>

                    <span>
                        ${demanda.email}
                    </span>

                </div>

            </div>

        </td>


        <td>
            ${demanda.origem}
        </td>


        <td>
            ${demanda.destino}
        </td>


        <td>

            <strong>
                ${formatarMoeda(demanda.valor)}
            </strong>

        </td>


        <td>

            <span class="badge-fonte">
                ${demanda.fonte}
            </span>

        </td>


        <td>

            <span class="badge-status">
                Integrado
            </span>

        </td>

    `;


    return linha;

}



// ========================================
// RENDERIZAR TABELA PRINCIPAL
// ========================================

function renderizarDemandas() {

    if (!tabelaDemandas) {
        return;
    }


    tabelaDemandas.innerHTML = "";


    const quantidade =
        mostrarTodas
            ? demandas.length
            : Math.min(5, demandas.length);


    const lista =
        demandas.slice(0, quantidade);


    lista.forEach(demanda => {

        tabelaDemandas.appendChild(
            criarLinha(demanda)
        );

    });


    if (contadorDemandas) {

        contadorDemandas.textContent =
            `Exibindo ${quantidade} de ${demandas.length} demandas`;

    }


    if (btnVerTodas) {

        if (mostrarTodas) {

            btnVerTodas.textContent =
                "Mostrar menos ↑";

        } else {

            btnVerTodas.textContent =
                "Ver todas as demandas →";

        }

    }

}



// ========================================
// RENDERIZAR TODAS AS DEMANDAS
// ========================================

function renderizarTodasDemandas() {

    if (!tabelaTodasDemandas) {
        return;
    }


    tabelaTodasDemandas.innerHTML = "";


    demandas.forEach(demanda => {

        tabelaTodasDemandas.appendChild(
            criarLinha(demanda)
        );

    });

}



// ========================================
// ATUALIZAR DASHBOARD
// ========================================

function atualizarDashboard() {

    // TOTAL

    const total =
        document.getElementById("totalDemandas");

    if (total) {

        total.textContent =
            demandas.length;

    }



    // INTEGRADAS

    const integradas =
        document.getElementById("demandasIntegradas");

    if (integradas) {

        integradas.textContent =
            demandas.length;

    }



    // VALOR TOTAL

    const valorTotal =
        document.getElementById("valorTotal");

    if (valorTotal) {

        const soma =
            demandas.reduce(
                (total, demanda) =>
                    total + demanda.valor,
                0
            );

        valorTotal.textContent =
            formatarMoeda(soma);

    }



    // CSV

    const contadorCSV =
        document.getElementById("contadorCSV");

    if (contadorCSV) {

        const quantidadeCSV =
            demandas.filter(
                demanda => demanda.fonte === "CSV"
            ).length;

        contadorCSV.textContent =
            `${quantidadeCSV} registros`;

    }



    // JSON

    const contadorJSON =
        document.getElementById("contadorJSON");

    if (contadorJSON) {

        const quantidadeJSON =
            demandas.filter(
                demanda => demanda.fonte === "JSON"
            ).length;

        contadorJSON.textContent =
            `${quantidadeJSON} registros`;

    }



    // XLSX

    const contadorXLSX =
        document.getElementById("contadorXLSX");

    if (contadorXLSX) {

        const quantidadeXLSX =
            demandas.filter(
                demanda => demanda.fonte === "XLSX"
            ).length;

        contadorXLSX.textContent =
            `${quantidadeXLSX} registros`;

    }

}



// ========================================
// BOTÃO VER TODAS
// ========================================

if (btnVerTodas) {

    btnVerTodas.addEventListener(
        "click",
        function () {

            mostrarTodas =
                !mostrarTodas;

            renderizarDemandas();

        }
    );

}



// ========================================
// MENU LATERAL
// ========================================

const menuItems =
    document.querySelectorAll(".menu-item");

const sections =
    document.querySelectorAll(".section");

const tituloPagina =
    document.getElementById("tituloPagina");


menuItems.forEach(item => {

    item.addEventListener(
        "click",
        function () {

            const sectionId =
                this.dataset.section;


            // Remove ativo

            menuItems.forEach(menu => {

                menu.classList.remove("active");

            });


            // Ativa botão

            this.classList.add("active");


            // Esconde seções

            sections.forEach(section => {

                section.classList.remove("active");

            });


            // Mostra seção escolhida

            const section =
                document.getElementById(sectionId);


            if (section) {

                section.classList.add("active");

            }


            // Atualiza título

            const nomes = {

                dashboard: "Dashboard",
                demandas: "Demandas",
                fontes: "Fontes de dados",
                historico: "Histórico"

            };


            if (tituloPagina) {

                tituloPagina.textContent =
                    nomes[sectionId];

            }


            // Se abriu demandas,
            // mostra todas

            if (sectionId === "demandas") {

                renderizarTodasDemandas();

            }

        }
    );

});



// ========================================
// MODAL
// ========================================

function abrirModal() {

    if (modal) {

        modal.classList.add("show");

    }

}



function fecharModal() {

    if (modal) {

        modal.classList.remove("show");

    }

}



// ========================================
// BOTÃO NOVA DEMANDA
// ========================================

const btnNovaDemanda3 =
    document.getElementById("btnNovaDemanda3");


if (btnNovaDemanda3) {

    btnNovaDemanda3.addEventListener(
        "click",
        abrirModal
    );

}



// ========================================
// FECHAR MODAL
// ========================================

const btnFecharModal =
    document.getElementById("btnFecharModal");

const btnCancelar =
    document.getElementById("btnCancelar");


if (btnFecharModal) {

    btnFecharModal.addEventListener(
        "click",
        fecharModal
    );

}


if (btnCancelar) {

    btnCancelar.addEventListener(
        "click",
        fecharModal
    );

}



// ========================================
// CLICAR FORA DO MODAL
// ========================================

if (modal) {

    modal.addEventListener(
        "click",
        function (event) {

            if (event.target === modal) {

                fecharModal();

            }

        }
    );

}



// ========================================
// NOVA DEMANDA
// ========================================

if (formDemanda) {

    formDemanda.addEventListener(
        "submit",
        function (event) {

            event.preventDefault();


            // PEGAR DADOS

            const cliente =
                document.getElementById("cliente").value.trim();


            const origem =
                document.getElementById("origem").value.trim();


            const destino =
                document.getElementById("destino").value.trim();


            const valor =
                Number(
                    document.getElementById("valor").value
                );


            const fonte =
                document.getElementById("fonte").value;



            // VALIDAR FONTE

            if (!fonte) {

                alert(
                    "Selecione a fonte da demanda."
                );

                return;

            }



            // ADICIONAR NOVA DEMANDA

            demandas.unshift({

                cliente: cliente,

                email: "não informado",

                origem: origem,

                destino: destino,

                valor: valor,

                fonte: fonte

            });



            // ATUALIZAR TABELAS

            renderizarDemandas();

            renderizarTodasDemandas();



            // ATUALIZAR DASHBOARD

            atualizarDashboard();



            // FECHAR MODAL

            fecharModal();



            // LIMPAR FORMULÁRIO

            formDemanda.reset();



            // AVISO

            alert(
                "Demanda adicionada com sucesso!"
            );

        }
    );

}



// ========================================
// INICIALIZAÇÃO
// ========================================

renderizarDemandas();

renderizarTodasDemandas();

atualizarDashboard();