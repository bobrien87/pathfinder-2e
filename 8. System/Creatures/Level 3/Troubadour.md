---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Troubadour"
level: "3"
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
    desc: "+9"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +8, Deception +9, Diplomacy +9, Occultism +7, Performance +13, Society +7, Stealth +8, Bardic Lore +7, Storytelling Lore +9"
abilityMods: ["+0", "+3", "+0", "+2", "+1", "+4"]
abilities_top:
  - name: "Bardic Lore"
    desc: "The troubadour can [[Recall Knowledge]] on any subject with a +7 modifier."
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +11, **Will** +9"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +11 (`pf2:1`) (deadly d8, disarm, finesse), **Damage** 1d6+4 piercing"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 20, attack +12<br>**2nd** (2 slots) [[Calm]], [[Embed Message]]<br>**1st** (3 slots) [[Charm]], [[Daze]], [[Figment]], [[Illusory Disguise]], [[Message]], [[Prestidigitation]], [[Read Aura]], [[Soothe]], [[Ventriloquism]]"
  - name: "Bard Composition Spells"
    desc: "DC 20, attack +12<br>**1st** [[Counter Performance]], [[Courageous Anthem]], [[Lingering Composition]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Troubadours keep alive the traditional songs of their culture and write original works to commemorate major events.

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Troubadour"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
