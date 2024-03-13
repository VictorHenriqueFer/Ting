def exists_word(escrita, momento):
    """Aqui irá sua implementação"""
    fial = list()
    for rastrio in range(len(momento)):
        xx = []
        for rastraioDois, pi in enumerate(
            momento.search(rastrio)["linhas_do_arquivo"]
        ):
            if escrita in pi.lower():
                xx.append({"linha": rastraioDois + 1})
        if xx:
            fial.append(
                {
                    "palavra": escrita,
                    "arquivo": momento.search(rastrio)["nome_do_arquivo"],
                    "ocorrencias": xx,
                }
            )
    return fial


def search_by_word(escrita, momento):
    """Aqui irá sua implementação"""
    final = []
    escrita = escrita.lower()
    for dd in momento._files:
        xpw = []
        for rastreio, pi in enumerate(dd["linhas_do_arquivo"], start=1):
            if escrita in pi.lower():
                xpw.append({"linha": rastreio, "conteudo": pi})
        if xpw:
            final.append(
                {
                    "palavra": escrita,
                    "arquivo": dd["nome_do_arquivo"],
                    "ocorrencias": xpw,
                }
            )
    return final
