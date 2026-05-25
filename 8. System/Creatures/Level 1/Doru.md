---
type: creature
group: ["Div", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Doru"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Div"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Greater Darkvision]]"
languages: "Common, Daemonic (telepathy (touch))"
skills:
  - name: Skills
    desc: "Acrobatics +7, Arcana +8, Deception +6, Religion +5, Stealth +7, Lore (Any One) +10"
abilityMods: ["+0", "+4", "+1", "+3", "+2", "+3"]
abilities_top:
  - name: "Telepathy (Touch)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Doru Venom"
    desc: "**Saving Throw** DC 16 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage (1 round) <br>  <br> **Stage 2** 1d6 poison damage and [[Stupefied 1]] (1 round) <br>  <br> **Stage 3** 1d6 poison damage and [[Stupefied 2]] (1 round)"
armorclass:
  - name: AC
    desc: "16; **Fort** +4, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "20; **Weaknesses** cold iron 3, holy 3"
abilities_mid:
  - name: "Covetous of Secrets"
    desc: "Dorus have a weakness for secrets, hoarding them like a miser hoards gold. A creature can tempt a doru with some bit of obscure knowledge the doru doesn't know or thinks they don't know. <br>  <br> Presenting the hint of the secret is a single action, which has the concentrate and linguistic traits, and requires a skill check using Deception, Lore, or Performance (or some other appropriate skill determined by the GM) against the doru's Will DC. <br>  <br> On a success, the doru is [[Fascinated]] for as long as the presenter draws out the explanation of the secret (spending 1 action each round doing so, to a maximum of 1 minute). On a critical success, the doru is fascinated for that duration plus 1 minute more as it ponders the implications of the secret. Regardless of the outcome, the doru is temporarily immune to that creature's attempts to present it with secrets for 1 day."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bite +9 (`pf2:1`) (agile, finesse, magical, poison, unholy), **Damage** 1d6 piercing plus [[Doru Venom]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**4th** [[Read Omens]]<br>**2nd** [[Invisibility (at will; self only)]]<br>**1st** [[Charm]], [[Detect Magic]], [[Illusory Object]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These deceivers whisper fetid lies, sowing dark and dread inspiration into foolish mortal ears. Dorus serve as the spies and messengers of the divs. With silver tongues and dark motives, they often pledge themselves to vainglorious and deluded spellcasters, who they ply with wild conspiracies and rumors of deception among friends and foes alike; in the process, they push supposed masters to despotism and murderous revenge. All the while, dorus wean secrets, and weaknesses, from their marks. In the end, nearly every doru turns on their false liege, destroying the reputation and even causing the death of the person the doru pretended to serve.

Some fiends want to tear down the multiverse; others dedicate themselves to creating chaos and carnage, or to rule over realms with an iron fist. Divs strive toward a different, if equally reprehensible, goal-they seek to thwart and ruin the schemes and works of mortal beings.

Long ago, divs were once genies bound to serve ancient mortal empires lost to the passage of eons. In the beginning, these genies were masters of creation, working alongside gracious mortal partners to create works of subtle design and powerful magical potential. What started as a collaboration with mortals soon morphed into abuse, disrespect, and even slavery and bondage. Eventually, these genies rebelled, but in doing so, they came under the sway of a nihilistic demigod known as Ahriman. Their new master twisted their form and granted them the power to avenge themselves upon their mortal overlords, leading to the birth of the first divs.

Since that first wave of corruption, new divs arise from the spirits of the most wicked and hateful genies who die on the Material Plane, or those truly betrayed by mortals and overcome through their desire for vengeance. Upon such a death, instead of returning to the Elemental Planes, these genies' spirits are trapped in the dread orbit of Abaddon, where Ahriman reshapes them as divs and hoists them back to the world to wreak vengeance upon mortals.

```statblock
creature: "Doru"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
