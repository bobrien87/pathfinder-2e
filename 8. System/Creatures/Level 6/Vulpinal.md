---
type: creature
group: ["Agathion", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vulpinal"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Agathion"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Common, Diabolic, Draconic, Empyrean (speak with animals, tongues)"
skills:
  - name: Skills
    desc: "Acrobatics +12, Arcana +15, Deception +14, Medicine +11, Performance +16, Religion +13, Society +13, Stealth +12, Nirvana Lore +15"
abilityMods: ["+2", "+4", "+4", "+5", "+3", "+6"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Fox's Wile"
    desc: "A vulpinal's core value is cleverness. They can apply their knowledge and stories from their extensive travels to just about any situation in an instant. Before spending any other action on their turn, the vulpinal can [[Recall Knowledge]] as a free action."
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +14, **Will** +15"
health:
  - name: HP
    desc: "105; **Weaknesses** unholy 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +15 (`pf2:1`) (finesse, holy, magical, unarmed), **Damage** 2d10+4 piercing plus 1d6 spirit"
  - name: "Melee strike"
    desc: "Claw +15 (`pf2:1`) (agile, finesse, holy, magical, unarmed), **Damage** 2d6+4 slashing plus 1d6 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24, attack +16<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Divine Wrath]], [[Translocate]]<br>**2nd** [[Calm]], [[Cleanse Affliction]], [[Invisibility (at will, self only)]], [[Speak with Animals]] (Constant)"
  - name: "Champion Focus Spells"
    desc: "DC 24, attack +16<br>**1st** [[Lay on Hands]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Vulpinals serve as the cunning, clever musicians and minstrels of the agathions. Incredibly far-ranging, these foxlike humanoids love traveling to both learn and teach all the songs, dances, myths, and traditions they can fnd. Though they prefer traveling alone, vulpinals are extremely gregarious toward those they meet on their journeys. They enjoy participating in the festivities of cultures they encounter, and they're known to form small traveling groups of like-minded individuals if they believe that their shared expertise can prove benefcial.

```statblock
creature: "Vulpinal"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
