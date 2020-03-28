siglas = {
    'UFLA': 'Universidade Federal de Lavras',
}


# GERADOR DA LISTA DE SIGLAS
if __name__ == '__main__':
    with open('listadesiglas.tex', 'w') as fp:
        fp.write('\\begin{center}\n  \\normalsize{\\textbf{LISTA DE SIGLAS}}\n\\end{center}\n')
        fp.write('\n\\vspace{1mm}\n')
        fp.write('\n\\begin{center}\n  \\begin{tabular}{ m{3cm} m{10cm} }\n')
        for i in sorted(siglas): fp.write(f'    {i} & {siglas[i]} \\\\ \n')
        fp.write('  \\end{tabular}\n\\end{center}\n')
