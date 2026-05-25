---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Therapeutic Healer"
level: "7"
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
    desc: "+14"
languages: "Common (two additional humanoid languages)"
skills:
  - name: Skills
    desc: "Diplomacy +17, Medicine +17, Occultism +16, Performance +15, Society +14"
abilityMods: ["+2", "+1", "+0", "+3", "+3", "+4"]
abilities_top:
  - name: "Doctor's Hand"
    desc: "When the therapeutic healer rolls a critical failure on a check to [[Treat Disease]], [[Treat Poison]], or [[Treat Wounds]], they get a failure instead."
  - name: "Emotionally Invested"
    desc: "When the therapeutic healer casts a spell with the healing trait on a creature other than themself, the healer regains HP equal to the spell's rank."
  - name: "Therapeutic Care"
    desc: "When [[Treating Wounds]], the therapeutic healer can treat up to four targets. If they succeed at a DC 20 check to Treat Wounds, they can also reduce the value of one [[Clumsy]], [[Enfeebled]], or [[Stupefied]] condition affecting a single patient by 1. They can reduce a [[Drained]] or [[Doomed]] condition instead if they succeed at a DC 30 check. This can't reduce permanent doomed conditions."
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +12, **Will** +18"
health:
  - name: HP
    desc: "110; **Resistances** mental 5"
abilities_mid:
  - name: "+2 to Sense Motive"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +13 (`pf2:1`) (two hand d8), **Damage** 1d8+6 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +13 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 25, attack +17<br>**3rd** (3 slots) [[Veil of Privacy]]<br>**2nd** (3 slots) [[Cleanse Affliction]], [[Clear Mind]], [[Clear Mind]], [[Status]], [[Translate]]<br>**1st** (3 slots) [[Guidance]], [[Message]], [[Prestidigitation]], [[Protection]], [[Sanctuary]], [[Shield]], [[Soothe]], [[Soothe]], [[Soothe]], [[Soothe]], [[Telekinetic Projectile]]"
  - name: "Bard Composition Spells"
    desc: "DC 25, attack +17<br>**1st** [[Hymn of Healing]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Some healers feel great empathy for their charges and take great pains to help shoulder their allies' burdens both in and out of combat.

The world is a dangerous place. Thankfully, there are those who devote their lives to easing the pain and suffering of others.

```statblock
creature: "Therapeutic Healer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
