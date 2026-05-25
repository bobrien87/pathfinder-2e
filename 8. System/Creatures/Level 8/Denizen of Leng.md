---
type: creature
group: ["Aberration", "Dream"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Denizen of Leng"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: "Dream"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: "Aklo (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +15, Deception +19, Occultism +18, Stealth +17, Thievery +17, Sailing Lore +20"
abilityMods: ["+3", "+3", "+4", "+6", "+3", "+5"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Debilitating Bite"
    desc: "A creature that takes damage from a denizen's bite must succeed at a DC 27 [[Fortitude]] save or become [[Clumsy]] 1. Each time a target fails an additional save against this ability, the condition value increases by 1 (to a maximum of Clumsy 4). This condition value decreases by 1 every 24 hours."
  - name: "Leng Ruby"
    desc: "Many denizens of Leng carry strange rubies mined from quarries in Leng. As long as a creature holds a Leng ruby that it willingly accepted as a gift or payment from a denizen of Leng, any denizen of Leng can target that creature with [[Mind Reading]], [[Outcast's Curse]], or [[Phantom Pain]] at a range of 1 mile, and the bearer uses an outcome one degree of success worse than the result of its saving throw against outcast's curse."
armorclass:
  - name: AC
    desc: "27; **Fort** +16, **Ref** +19, **Will** +17"
health:
  - name: HP
    desc: "100; planar fast healing 5; **Immunities** cold; **Resistances** critical hits 10, precision 10"
abilities_mid:
  - name: "Planar Fast Healing"
    desc: "A denizen of Leng maintains a connection to Leng at all times, and when away from Leng, they have fast healing 5. They lose this ability on Leng or in areas where planar connections do not function. If killed, their body dissolves into nothingness in 1d4 rounds, leaving behind their equipment. A slain denizen reforms in Leng; they can be permanently killed only when their planar fast healing doesn't function. <br>  <br> A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "No Breath"
    desc: "Denizens of Leng don't need to breathe."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Kukri +18 (`pf2:1`) (agile, finesse, magical, trip), **Damage** 2d6+6 slashing plus 1d6 bleed"
  - name: "Melee strike"
    desc: "Jaws +17 (`pf2:1`) (agile, finesse, unarmed), **Damage** 2d10+6 piercing plus [[Debilitating Bite]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 26, attack +18<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Outcast's Curse]], [[Suggestion]]<br>**3rd** [[Hypnotize]], [[Levitate]], [[Locate]], [[Mind Reading]]<br>**2nd** [[Blur]]<br>**1st** [[Detect Magic]], [[Message]], [[Phantom Pain]], [[Read Aura]], [[Telekinetic Hand]], [[Void Warp]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Travelers and raiders from the cold, windswept dimension of Leng, these malevolent human-shaped creatures range across reality in ominous black ships capable of sailing beyond the borders of dimensions and planes. Although most denizens of Leng seek conquest and riches, others operate as self-styled ambassadors and merchants, sowing discord with far-ranging plots. While the inscrutable denizens dress themselves in flowing robes, veils, and broad turbans to appear human, their aberrant physiology, when glimpsed, is evident from their crown of stubby horns and tentacled jaws to their furry, goat-like legs.

Denizens of Leng are often highly intelligent and can be found advising or nudging both the powerful and the meek alike. If there is any purpose to this beyond an individual Denizen of Leng's own interests, there has so far been no sign. Most appear to be perfectly genuine with their counsel, though generally lacking in anything resembling morality.

Above the fierce captains who command the infamous black ships is an even higher caste of denizens of Leng. These occultists and musicians serve as high priests, laboring to appease the frightening gods who look down upon the Nightmare Realm with cold malice.

```statblock
creature: "Denizen of Leng"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
