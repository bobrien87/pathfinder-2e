---
type: creature
group: ["Gnome", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gnome Bard"
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
    desc: "+7; [[Low-Light Vision]]"
languages: "Common, Fey, Gnomish"
skills:
  - name: Skills
    desc: "Acrobatics +5, Deception +7, Diplomacy +5, Intimidation +7, Performance +7, Stealth +5"
abilityMods: ["+1", "+3", "+1", "+1", "+2", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +7, **Will** +9"
health:
  - name: HP
    desc: "16"
abilities_mid:
  - name: "Gnomish Shift"
    desc: "`pf2:r` **Trigger** The gnome bard would take damage <br>  <br> **Effect** The gnome bard gains resistance 2 to the triggering damage and teleports to an adjacent space."
speed: "0 feet"
attacks: []
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 19, attack +11<br>**1st** (2 slots) [[Charm]], [[Command]], [[Courageous Anthem]], [[Daze]], [[Figment]], [[Message]], [[Prestidigitation]], [[Summon Instrument]]"
abilities_bot:
  - name: "Do a Jig!"
    desc: "`pf2:1` The gnome bard plays a ditty that inspires dance. One creature within 30 feet must make a DC 19 [[Will]] save saving throw. <br> - **Success** The target is unaffected. <br> - **Failure** The target must waste 1 action on its next turn dancing. <br> - **Critical Failure** The target must waste 2 actions on its next turn dancing."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Being a bard allows a gnome a wonderful excuse to constantly travel and see new places while simultaneously creating wonderful things. Occasionally, these bards have a reputation for inappropriate or socially critical performances.

Gnomes are known for being creative and curious. They stand at around 3 feet tall, and their vivid personalities match their naturally vivid hair and eye color. Gnomes possess a natural connection to their ancestral home, the First World. They crave adventure and new experiences to fight off an ancestry-wide affliction known as the Bleaching. Gnomes who fail to dream and innovate begin to slowly lose their color and fall into a deep depression.

A notable subgroup of gnomes called umbral gnomes typically have gray or brown skin with a stony texture, and thin, pale hair or bald pates. Umbral gnomes are most numerous in the Darklands, where they go by the name drathnelar. Umbral gnomes often attribute these physical changes to the gnome deity regarded as the first of their kind, Nivi Rhombodazzle. Nivi was a surface gnome who traveled deep into the Darklands and was ultimately rewarded with demigodhood when she exchanged a particular gemstone with the dwarven deity, Torag. Nivi is immune to the Bleaching, and umbral gnomes are often immune or resistant to it as well.

```statblock
creature: "Gnome Bard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
