---
type: creature
group: ["Catfolk", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Catfolk Name Collector"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Catfolk"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Low-Light Vision]], [[Spiritsense]] (imprecise) 30 feet"
languages: "Amurrun, Common"
skills:
  - name: Skills
    desc: "Occultism +12, Performance +14, Society +12, Catfolk Lore +15"
abilityMods: ["+0", "+4", "+1", "+2", "+1", "+4"]
abilities_top:
  - name: "Spiritsense (Imprecise) 30 feet"
    desc: "The name collector senses spirits, embodied or not (including living creatures, most non-mindless undead, and haunts)."
armorclass:
  - name: AC
    desc: "24; **Fort** +11, **Ref** +14, **Will** +13"
health:
  - name: HP
    desc: "70"
abilities_mid:
  - name: "Name the Worthy"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** Another creature critically succeeds at a check <br>  <br> **Effect** The name collector honors the achievement with a new name. The creature gets a +1 status bonus on the same check until their next daily preparations. They become temporarily immune for 1 month."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sickle +15 (`pf2:1`) (agile, finesse, magical, trip), **Damage** 1d4+9 slashing"
  - name: "Melee strike"
    desc: "Claw +14 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4+9 slashing"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 24, attack +16<br>**3rd** (2 slots) [[Heroism]], [[Illusory Creature]]<br>**2nd** (3 slots) [[Laughing Fit]], [[See the Unseen]], [[Soothe]]<br>**1st** (3 slots) [[Bless]], [[Spirit Link]], [[Sure Strike]]<br>**Cantrips** [[Daze]], [[Detect Magic]], [[Read Aura]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Name collectors are esteemed touchstones of catfolk culture. They record the adventures of catfolk heroes, speak to spirits, and tell legends about strange and faraway places.

Catfolk can be found traveling almost anywhere, and they are quick to settle down for a chat when they encounter fellow travelers. Some trade stories, act as guides, or operate at the fringes of polite society.

```statblock
creature: "Catfolk Name Collector"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
