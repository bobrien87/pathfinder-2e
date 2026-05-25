---
type: creature
group: ["Gnome", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Umbral Gnome Scout"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Gnomish, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +7, Nature +5, Stealth +7, Survival +5"
abilityMods: ["+2", "+4", "+2", "+0", "+2", "-1"]
abilities_top:
  - name: "Hidden Movement"
    desc: "If the umbral gnome scout starts its turn [[Undetected]] or [[Hidden]] to a creature, that creature is [[Off Guard]] against the umbral gnome scout's attacks until the end of the turn."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +9, **Will** +5"
health:
  - name: HP
    desc: "18"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Light Pick +7 (`pf2:1`) (agile, fatal d8), **Damage** 1d4+2 piercing"
  - name: "Ranged strike"
    desc: "Sling +9 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+1 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 14, attack +6<br>**1st** [[Illusory Disguise]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Umbral gnome scouts patrol the tunnels that lead into their settlements.

Gnomes are known for being creative and curious. They stand at around 3 feet tall, and their vivid personalities match their naturally vivid hair and eye color. Gnomes possess a natural connection to their ancestral home, the First World. They crave adventure and new experiences to fight off an ancestry-wide affliction known as the Bleaching. Gnomes who fail to dream and innovate begin to slowly lose their color and fall into a deep depression.

A notable subgroup of gnomes called umbral gnomes typically have gray or brown skin with a stony texture, and thin, pale hair or bald pates. Umbral gnomes are most numerous in the Darklands, where they go by the name drathnelar. Umbral gnomes often attribute these physical changes to the gnome deity regarded as the first of their kind, Nivi Rhombodazzle. Nivi was a surface gnome who traveled deep into the Darklands and was ultimately rewarded with demigodhood when she exchanged a particular gemstone with the dwarven deity, Torag. Nivi is immune to the Bleaching, and umbral gnomes are often immune or resistant to it as well.

```statblock
creature: "Umbral Gnome Scout"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
