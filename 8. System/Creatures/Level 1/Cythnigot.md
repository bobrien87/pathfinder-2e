---
type: creature
group: ["Fiend", "Qlippoth"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cythnigot"
level: "1"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fiend"
trait_02: "Qlippoth"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Chthonian (Telepathy (Touch Only))"
skills:
  - name: Skills
    desc: "Acrobatics +6, Occultism +7, Stealth +6"
abilityMods: ["+1", "+3", "+4", "+2", "+2", "+1"]
abilities_top:
  - name: "Telepathy (Touch Only)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Tangle Spores"
    desc: "A creature bitten by a cythnigot becomes afflicted by fast-growing spores that swiftly grow into twitching spikes and hideous pallid growths of hairlike fibers. These growths erupt from the bite wound and writhe and wrap around the creature's limbs. Plant creatures take a –2 circumstance penalty to save against tangle spores <br>  <br> **Saving Throw** DC 17 [[Fortitude]] save; <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** [[Clumsy]] 1 (1 round) <br>  <br> **Stage 2** clumsy 1 and [[Off Guard]] (1 round) <br>  <br> **Stage 3** [[Clumsy]] 2, off-guard, and if you attempt a manipulate action, you must succeed at a DC 5 flat check or it's lost; roll the check after spending the action, but before any effects are applied (1 round)."
armorclass:
  - name: AC
    desc: "16; **Fort** +9, **Ref** +6, **Will** +5"
health:
  - name: HP
    desc: "14; **Immunities** controlled, fear effects; **Resistances** mental 3, physical 3 except cold iron"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bite +8 (`pf2:1`) (agile, finesse, magical, reach 0 ft., unholy), **Damage** 1d10+1 piercing plus [[Tangle Spores]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 17, attack +9<br>**4th** [[Read Omens]]<br>**2nd** [[Paranoia]]<br>**1st** [[Daze]], [[Detect Magic]], [[Phantom Pain]]"
abilities_bot:
  - name: "Sickening Display"
    desc: "`pf2:1` The cythnigot presents its awful appearance fully, and creatures in a @Template[emanation|distance:10] must attempt a DC 17 [[Will]] save. Once a creature attempts this save, it's temporarily immune to further Sickening Displays for 1 minute. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Off Guard]] until its next turn. <br> - **Failure** The creature is [[Sickened]] 1 and is off-guard for as long as it's sickened. <br> - **Critical Failure** As failure but [[Sickened]] 2."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The cythnigot is a foul fungal parasite that grows and thrives in the corpses of small creatures. It wears these bodies like a suit, but also adjusts and tailors the fleshy covering to fit its needs, and the body ends up looking as alien as anything else spawned from the Chthonian depths. The cythnigot's most identifying feature is the long stalk of fungal material that extends from creature's body, ending in a surprisingly strong set of fanged jaws.

Long before the creatures known as demons came to be the dominant force in the Outer Rifts, qlippoth ruled the innumerable cracks of the Outer Sphere. These inimical creatures are a form of primordial and alien evil that predates mortal life, and most immortal life as well. Since the rise of mortal sin and the associated expansion of demonic life through the Outer Rifts, qlippoth have been driven to their deepest reaches, and they seethe with rancor at the loss of their realms. Yet, rather than directly oppose demons, qlippoth instead turn to the source—mortal sin—and wage an endless war to eradicate all creatures capable of sinful acts so that the demonic tide might be turned back. To ensure they do not bolster their foe's ranks, they enact horrific transformations on their targets, converting their victims into beings incapable of discerning right from wrong; this renders them unable to be judged by Pharasma's courts and thus incapable of becoming fiends. Most mortals consider the ministrations of a qlippoth to be far worse than any fate awaiting them in the afterlife.

```statblock
creature: "Cythnigot"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
