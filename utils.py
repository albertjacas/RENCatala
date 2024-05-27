import re
from spacy.tokens import Span

# Una clase per definir temporalment entitats nomenades.
class EntitatNomenada:

    # Constructor de la classe.
    def __init__(self, etiqueta, inici, longitud, tokens):

        self.etiqueta = etiqueta
        self.inici = inici
        self.longitud = longitud
        self.fi = inici + longitud
        self.tokens = tokens

    # Exporta l'EntitatNomenada en el format de Spacy.
    def a_spacy(self, doc):

        return Span(doc, self.inici, self.fi, self.etiqueta)
    
    # Exporta l'EntitatNomenada com una tupla.
    def a_tupla(self):

        return (self.etiqueta, self.inici, self.longitud, tuple(self.tokens))
    
    # Imprimeix els valors per poder veure'ls fàcilment.
    def print(self):

        print("{} ({}-{}) =".format(self.etiqueta, self.inici, self.fi, self.tokens), self.tokens)

    # Verifica que aquesta entitat anomenada és correcta.
    def verificar(self, tokens_reals):

        tokens_extrets = tokens_reals[self.inici:self.fi]
        tokens_strip = [t.strip(',.') for t in tokens_extrets]
        assert(self.tokens == tokens_extrets or self.tokens == tokens_strip)


# Afegir una nova entitat nomenada al document d'Spacy.
def afegir_entitat_nomenada(doc, entitat_nomenada):

    # Obtenim la llista d'entitats com una llista de Python.
    llista_entitats = list(doc.ents)

    # Afegim la nostra en el format de spacy.
    llista_entitats.append(entitat_nomenada.a_spacy(doc))

    # Estamblim aquesta llista com a llista d'entitats al document.
    doc.set_ents(llista_entitats)
    
    return doc
    
# Troba tots els fragment del text que coincideixin amb l'expressió
# regular i els retorna com una llista.
def obtenir_totes_les_coincidencies(regex, text):

    return [match[0] for match in re.finditer(regex, text)]

# Converteix una serie de troballes en un text en referencies al text
# tokenitzat utilitzant els indexs dels tokens corresponents.
def convertir_fragments_a_referencies(tokens, fragments_tokenitzats, etiqueta):

    # Inicialitza la llista que retornarem.
    llista_referencies = []

    # Inicialitza un minim on cercar.
    # Això ens garanteix que el codi que apliquem es fa sobre la següent
    # coincidencia amb els tokens, i no sempre sobre la primera.
    index_min_cerca = 0

    # Per cada fragment trobat, itera.
    for fragment in fragments_tokenitzats:

        # Troba l'index on comença la subllista dins la llista de fragments.
        index_trobat = troba_llista_dins_de_llista(fragment, tokens, index_min_cerca)
        index_min_cerca = index_trobat + len(fragment)

        # Si no podem trobar el fragment en el conjunt de tokens, significa que és
        # un error i hem de descartar aquest fragment.
        if index_trobat < 0:
            print('DESCARTAT:', fragment)
            continue

        # Creem una nova entitat nomenada i l'incorporem a la llista.
        llista_referencies.append(EntitatNomenada(etiqueta, index_trobat, len(fragment), fragment))

    return llista_referencies

# Troba el primer index on apareix una llista donada dins d'una altra.
def troba_llista_dins_de_llista(subllista, llista, index_minim=0):

    # Com de llarga es la llista que busquem.
    longitut_cadena = len(subllista)

    # Iterem per les possibles subllistes d'aquesta durada.
    for index in range(index_minim, len(llista) - longitut_cadena + 1):

        subllista_actual = llista[index:index + longitut_cadena]

        # Probem també a fer un trimming del text per arreglar problemes
        # del tokenitzador.
        subllista_actual_trim = [t.strip(',.') for t in subllista_actual]

        # Si aquesta subllista es la mateixa que busquem, retorna
        # el seu index i deixem de buscar.
        if subllista_actual == subllista or subllista_actual_trim == subllista:
            return index

    return -1

# Retorna si dues entitats nomenades se solapen
def comprova_si_solapa(entitat_1, entitat_2):

    return (entitat_1.inici <= entitat_2.inici and entitat_1.fi - 1 >= entitat_2.inici) or \
        (entitat_1.inici <= entitat_2.fi - 1 and entitat_1.fi - 1 >= entitat_2.fi - 1)

# Verifica que les dues entitats nomenades són equivalents.
def entitats_nomenades_cmp(entitat_1, entitat_2):

    return entitat_1.etiqueta == entitat_2.etiqueta and \
        entitat_1.inici == entitat_2.inici and \
        entitat_1.longitud == entitat_2.longitud and \
        entitat_1.fi == entitat_2.fi and \
        entitat_1.tokens == entitat_2.tokens
