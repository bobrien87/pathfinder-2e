---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Beast Tamer"
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
    desc: "Athletics +8, Diplomacy +8, Intimidation +8, Nature +12, Performance +8, Survival +10, Circus Lore +6"
abilityMods: ["+2", "+1", "+2", "+0", "+4", "+2"]
abilities_top:
  - name: "Wild Empathy"
    desc: "The beast tamer can use Diplomacy to Requests of them."
  - name: "Animal Trick"
    desc: "The beast tamer gains the support benefit appropriate to its trained animal companion. Unlike for an animal companion, this doesn't require the animal to use any of its actions. The benefit for a [[Tiger]] is as follows: Until the start of the beast tamer's next turn, their Strikes that deal damage to a creature within the tiger's reach make the target [[Off Guard]] until the end of the beast tamer's next turn."
armorclass:
  - name: AC
    desc: "20; **Fort** +10, **Ref** +7, **Will** +12"
health:
  - name: HP
    desc: "55"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Whip +12 (`pf2:1`) (disarm, nonlethal, reach, trip), **Damage** 1d4+6 slashing"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 22, attack +13<br>**2nd** (3 slots) [[Animal Form]], [[Animal Messenger]], [[Speak with Animals]]<br>**1st** (3 slots) [[Grease]], [[Jump]], [[Runic Body]]<br>**Cantrips** [[Light]], [[Guidance]], [[Ignition]], [[Stabilize]], [[Tangle Vine]]"
  - name: "Druid Order Spells"
    desc: "DC 22, attack +13<br>**1st** [[Heal Animal]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Beast tamers bring the wild to civilization, rearing and training creatures to follow their commands and perform flashy tricks that entertain audiences. The beast tamer typically fights alongside a trained animal ally of its level or lower, most likely a tiger (Monster Core 51).

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Beast Tamer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
