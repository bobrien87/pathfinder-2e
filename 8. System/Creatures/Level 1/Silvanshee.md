---
type: creature
group: ["Agathion", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Silvanshee"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Agathion"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Common, Diabolic, Draconic, Empyrean (speak with animals)"
skills:
  - name: Skills
    desc: "Acrobatics +7, Arcana +3, Medicine +6, Stealth +7, Nirvana Lore +3"
abilityMods: ["-2", "+4", "+2", "+0", "+3", "+2"]
abilities_top:
  - name: "Cat's Curiosity"
    desc: "A silvanshee's core value is curiosity. This enables them to seek out new experiences and information beyond their current understanding. A silvanshee can use trained skill actions for all skills, even if they're untrained."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Cat's Poise"
    desc: "When a silvanshee uses their [[Vapor Form]] spell, the mist form remains roughly the size and shape of a cat, and the silvanshee retains their fly speed in this form."
armorclass:
  - name: AC
    desc: "17; **Fort** +5, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "20; **Weaknesses** unholy 3"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (finesse, holy, magical, unarmed), **Damage** 1d6-2 piercing plus 1d4 spirit"
  - name: "Melee strike"
    desc: "Claw +9 (`pf2:1`) (agile, finesse, holy, magical, unarmed), **Damage** 1d4-2 slashing plus 1d4 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**4th** [[Read Omens]], [[Vapor Form]]<br>**2nd** [[Speak with Animals]] (Constant)<br>**1st** [[Know the Way]], [[Light]], [[Prestidigitation]], [[Stabilize]]"
  - name: "Champion Focus Spells"
    desc: "DC 17, attack +9<br>**1st** [[Lay on Hands]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Silvanshees are a stealthy and extremely inquisitive contingent of agathions who gather information about the mortal world for other agathions. While they love to explore the Universe and sate their curiosity, they're generally reclusive and skittish. These dual instincts war with each other whenever something exciting piques their interest. Because of their small size, they don't pose a combat threat to most creatures; instead, silvanshees act as Nirvana's eyes and ears in the mortal world, reporting back to superiors or calling for help should they run into danger.

Silvanshees appear indistinguishable from domestic felines, save for their violet eyes and the telltale blaze of differently colored fur on their chests. Of course, fying gives them away outright, so if at all possible, they only do so while in trusted company to avoid detection.

Their fur color runs the spectrum of normal feline colorations. They can also transform into mist when necessary to maintain discretion or make a hasty getaway.

```statblock
creature: "Silvanshee"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
