---
type: creature
group: ["Gnome", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Umbral Gnome Rockwarden"
level: "5"
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
    desc: "+14; [[Darkvision]]"
languages: "Gnomish, Petran, Sakvroth"
skills:
  - name: Skills
    desc: "Crafting +9, Diplomacy +11, Nature +14, Stealth +9"
abilityMods: ["+1", "+2", "+3", "+0", "+5", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "22; **Fort** +12, **Ref** +9, **Will** +14"
health:
  - name: HP
    desc: "63"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pick +10 (`pf2:1`) (fatal d10), **Damage** 1d6 piercing"
  - name: "Ranged strike"
    desc: "Sling +11 (`pf2:1`) (propulsive, range 50 ft.), **Damage** 1d6 bludgeoning"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 24, attack +14<br>**3rd** (2 slots) [[Blindness]], [[One with Stone]]<br>**2nd** (3 slots) [[Acid Grip]], [[Deafness]], [[Gecko Grip]]<br>**1st** (3 slots) [[Ant Haul]], [[Thunderstrike]], [[Ventriloquism]]<br>**Cantrips** [[Caustic Blast]], [[Detect Magic]], [[Ignition]], [[Prestidigitation]], [[Read Aura]]"
  - name: "Primal Innate Spells"
    desc: "DC 21, attack +13<br>**1st** [[Illusory Disguise]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Umbral gnome rockwardens follow druidic teachings and commune with the natural elemental influences and denizens of the Darklands.

Gnomes are known for being creative and curious. They stand at around 3 feet tall, and their vivid personalities match their naturally vivid hair and eye color. Gnomes possess a natural connection to their ancestral home, the First World. They crave adventure and new experiences to fight off an ancestry-wide affliction known as the Bleaching. Gnomes who fail to dream and innovate begin to slowly lose their color and fall into a deep depression.

A notable subgroup of gnomes called umbral gnomes typically have gray or brown skin with a stony texture, and thin, pale hair or bald pates. Umbral gnomes are most numerous in the Darklands, where they go by the name drathnelar. Umbral gnomes often attribute these physical changes to the gnome deity regarded as the first of their kind, Nivi Rhombodazzle. Nivi was a surface gnome who traveled deep into the Darklands and was ultimately rewarded with demigodhood when she exchanged a particular gemstone with the dwarven deity, Torag. Nivi is immune to the Bleaching, and umbral gnomes are often immune or resistant to it as well.

```statblock
creature: "Umbral Gnome Rockwarden"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
