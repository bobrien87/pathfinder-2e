---
type: creature
group: ["Beast", "Incorporeal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cunning Fox"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Beast"
trait_02: "Incorporeal"
trait_03: "Spirit"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: "Common, Fey (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +6, Deception +6, Stealth +8, Survival +5"
abilityMods: ["+1", "+3", "+0", "+2", "+2", "+1"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +8, **Will** +7"
health:
  - name: HP
    desc: "15; **Immunities** bleed, disease, paralyzed, poison, precision; **Resistances** all damage 2 except force, ghost touch, spirit"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horn +6 (`pf2:1`) (finesse, magical), **Damage** 1d8+1 force"
  - name: "Melee strike"
    desc: "Jaws +6 (`pf2:1`) (agile, finesse, magical), **Damage** 1d4+1 force"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17, attack +9<br>**5th** [[Truespeech]] (Constant)<br>**3rd** [[Wanderer's Guide]]<br>**1st** [[Cleanse Cuisine]], [[Detect Poison]], [[Guidance]], [[Read Aura]], [[Stabilize]]"
abilities_bot:
  - name: "Bond with Mortal"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The spirit guide forms a bond with a mortal creature. While the bond exists, the spirit guide increases their current and maximum Hit Points by 10, gains a +2 status bonus to their attack and damage rolls, and can communicate telepathically with the bonded mortal as long as the two beings are on the same plane. <br>  <br> The spirit guide can only be bonded with one mortal at a time, and they can take this action again to end the bond or to form a new bond (which also ends the old bond). The bond also ends if the spirit guide or the mortal dies. <br>  <br> This bond strengthens the spirit guide's connection to the Universe. While bonded, the spirit guide loses the incorporeal and spirit traits, loses their immunities and resistances, and changes their Strikes to deal the appropriate physical damage (typically piercing or slashing) instead of force damage."
  - name: "Bonded Strike"
    desc: "`pf2:2` **Requirements** The spirit guide is currently Bonded with a Mortal <br>  <br> **Effect** The spirit guide makes a jaws Strike. If this attack hits, the bonded mortal can spend their reaction to Strike the same target."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Spirit guides of cunning are often seen as the weakest of the spirit guides, but they're also the most numerous and proactive, guiding families to safe paths or leaving food and water for warriors. Cunning guides often take the form of foxes.

Spirit guides are a distinctive form of spiritual entity with a tenuous attachment to the Universe. Some legends say the first spirit guides were the perfect conceptual forms of animals, and that from them, eagles, foxes, bears, and other mortal beasts were born. Each guide displayed an interest in mortal affairs, watching over communities and imparting their gifts. Fox shared his cunning with the mortals he befriended, while Bear taught them how to survive and endure.

Over countless mortal generations, new spirit guides were born, many of them possessing traits from two or more of the original guides. In the ancient human nation of Sarkoris, the people abandoned traditional gods in favor of venerating the spirit guides who watched over them. While some in neighboring nations saw this as heresy, to the old Sarkorians, such worship felt perfectly natural. After all, the same beings who'd taught their forebears to survive and thrive still walked among them.

Every so often, a spirit guide bonds with a mortal partner. While many spirit guides permanently bond with mortals, such as the spirit guides of Sarkoris and the spiritual leaders known as god callers, some instead form temporary bonds, either to test the prospective mortal before committing or because a permanent bond is undesirable. It's not uncommon for a single spirit guide to form bonds with multiple generations of the same family or community, protecting and guiding mortals they've grown fond of or who do them a great service.

```statblock
creature: "Cunning Fox"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
