import re
import random



class MadLib(object):
    pattern = re.compile(r"(?<=\{).*?(?=\})")

    def __init__(self, text):
        self.args = self.pattern.findall(text)
        self.text = self.pattern.sub("", text)


mad_libs = {
    'Dinosaurs': MadLib("""
            Today we are going to study the lifestyle of the huge and {adjective}
            animals.  The word 'dinosaur' comes from the Greek word deinos
            meaning {noun} and 'saurus' meaning {noun}. No one has even seen a {adjective}
            dinosaur.  We know about them because {plural noun} called palentolgist found
            their {plural noun} preserved in rocks.  Dinosaurs were almost evenly divided
            between carnivores who ate {plural noun} and herbivores who only ate
            {plural noun}. At one time, there were over {number} different types of
            these {adjective} beasts roaming the face of the {noun}. They range in size
            from those as large as a {noun} to those as small as a {noun}.  Today a
            dinosaur would be as impossible to find as a {noun} in a haystack.
    """),
    'Talk Like A Pirate': MadLib("""
        Ye can always pretend to be a bloodthirsty {noun}, threatening everyone
        by waving yer {adjective} sword in the air but until ye learn to {verb}
        like a pirate, ye'll never be {adverb} accepted as an authentic {noun}.
        So here's what ye do: Cleverly work into yer daily conversations {adjective}
        pirate phrases such as "Ahoy there, {plural noun},"Avast, ye {plural noun},"
        and "Shiver me {plural noun}." Remember to drop all yer gs when ye say
        such words as sailin', spittin', and fightin'.  This will give ye a
        {part of the body} start to being recognized as a swashbucklin' {noun}.
        Once ye have the lingo down pat, it helps to wear a three-cornered {noun}
        on yer head, stash a {noun} in yer pants, and keep a {noun} perched atop
        yer {part of the body}.  Aye, now ye be a real pirate.
    """),
    'Jolly Roger': MadLib("""
        The black-and-white {noun} that waved in the breeze
        atop a pirate ship was called a Jolly Roger.  There are many theories
        as to how the Jolly {noun} got its {adjective}
        name, but most {plural noun} agree that the {adjective}
        flag was designed to scare the living {plural noun} out of
        captains and crews on merchant {plural noun}. And indeed, it
        did.  When a lookout shouted, "{noun} ahoy!" and the
        captain sighted the dreaded skull and cross-{plural noun}
        through his or her spy-{noun}, not only did it strike terror
        in his or her {part of the body}, but it sent chills up and down the
        {part of the body} of every member on the {noun}.
        However, nothing generated as much {adjective}
        fear on merchant {plural noun} as the hoisting of a
        {adjective} red flag on a pirate {noun}. The
        red flag signaled that mercy would neither be asked for nor given -
        no {plural noun} would be spared.
    """)
}


# Now you have to figure out how to actually run the mad lib!
