---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pack Leader"
level: "4"
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
    desc: "+12"
languages: "Common, Wildsong"
skills:
  - name: Skills
    desc: "Athletics +6, Diplomacy +9, Nature +12, Stealth +9, Survival +10"
abilityMods: ["+0", "+3", "+1", "+0", "+4", "+3"]
abilities_top:
  - name: "Animal Empathy"
    desc: "The pack leader can ask questions of, receive answers from, and use the Diplomacy skill with animals."
armorclass:
  - name: AC
    desc: "20; **Fort** +9, **Ref** +9, **Will** +12"
health:
  - name: HP
    desc: "55"
abilities_mid:
  - name: "Stay Strong!"
    desc: "`pf2:r` **Trigger** An allied animal within 30 feet attempts a saving throw <br>  <br> **Effect** The pack leader shouts a word of encouragement, granting the allied animal a +1 circumstance bonus to the save. <br>  <br> > [!danger] Effect: Stay Strong!"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sickle +11 (`pf2:1`) (agile, finesse, trip), **Damage** 1d4+4 slashing"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +11 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+4 bludgeoning"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 20, attack +12<br>**2nd** (3 slots) [[Animal Messenger]], [[Enlarge]], [[Summon Animal]]<br>**1st** (3 slots) [[Gentle Landing]], [[Heal]], [[Pet Cache]]<br>**Cantrips** [[Gouging Claw]], [[Guidance]], [[Ignition]], [[Stabilize]], [[Tangle Vine]]"
  - name: "Druid Order Spells"
    desc: "DC 20, attack +0<br>**1st** [[Heal Animal]]"
abilities_bot:
  - name: "Timely Trick"
    desc: "`pf2:1` The pack leader commands an animal ally within 30 feet to perform a specific action; the target can spend its reaction to immediately Step, Stride, or Strike."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Primal spellcasters with a particular affinity for animals often aid their community by training and healing their domesticated animals. Others focus their time on preserving endangered species and helping them propagate or adapt to a changing environment. The pack leader is most often paired with the [[Trained Bat]] companion.

A primalist is a wielder of primal energies and magic, sometimes taught by forces of primal power, including powerful elementals or fey of the First World. Primalists protect the natural world, offering strong medicine to those in need while facing suspicion from those who don't understand their ways.

A great many primalists belong to druidic circles, and even those who aren't members tend to be familiar with the most prominent ones in their homeland.

```statblock
creature: "Pack Leader"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
