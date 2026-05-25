---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Apprentice"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+2"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +3, Crafting +5, Geography Lore +5"
abilityMods: ["+1", "+2", "+1", "+3", "+0", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "14; **Fort** +5, **Ref** +6, **Will** +2"
health:
  - name: HP
    desc: "8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +4 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Dagger +4 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Fist +4 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Apprentice's Ambition"
    desc: "`pf2:0` **Frequency** once per day <br>  <br> **Requirements** A direct superior is supervising the apprentice <br>  <br> **Effect** The apprentice gains a +2 circumstance bonus to attack rolls, damage rolls, saving throws, and skill checks until the end of their next turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Ambitious apprentices can be found in all cities. These individuals are generally younger and seek the approval of their masters as they learn their craft. Many yearn to exemplify the artistry behind their craft, one day becoming masters themselves. Depicted below is an apprentice cartographer.

Expertise is forged through years of effort and often tedious work. Artisans are masters of their craft, able to create works both practical and beautiful.

```statblock
creature: "Apprentice"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
