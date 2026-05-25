---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zealot of Asmodeus"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Unholy"
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
    desc: "Athletics +9, Deception +10, Intimidation +10, Religion +12, Society +7"
abilityMods: ["+4", "+1", "+1", "+0", "+3", "+2"]
abilities_top:
  - name: "Deadly Simplicity"
    desc: "The zealot deals 1d8 damage with their mace instead of 1d6."
armorclass:
  - name: AC
    desc: "22 (24 with shield raised); **Fort** +9, **Ref** +7, **Will** +11"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
  - name: "Swear Vengeance"
    desc: "`pf2:r` **Trigger** A creature the zealot can see damages a follower of [[Asmodeus]] other than the zealot <br>  <br> **Effect** The zealot is affected by a [[Sure Strike]] spell. If the zealot makes an attack roll against anyone other than the triggering creature, the *sure strike* ends with no effect."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mace +12 (`pf2:1`) (shove), **Damage** 1d6+4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Shortbow +9 (`pf2:1`) (deadly d10, propulsive, reload 0, range 60 ft.), **Damage** 1d6+2 piercing"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 19, attack +11<br>**2nd** (7 slots) [[Cleanse Affliction]], [[Harm]], [[Harm]], [[Harm]], [[Harm]], [[See the Unseen]], [[Share Life]]<br>**1st** (3 slots) [[Command]], [[Runic Weapon]], [[Spirit Link]]<br>**Cantrips** [[Detect Magic]], [[Divine Lance]], [[Forbidding Ward]], [[Read Aura]], [[Sigil]]"
abilities_bot:
  - name: "Channel Smite"
    desc: "`pf2:2` **Cost** the zealot expends a [[Harm]] spell <br>  <br> **Effect** The zealot makes a melee Strike. If it hits, they damage the target with a 1-action *harm* spell. The target automatically gets a failure (or a critical failure if the Strike was a critical hit). The spell doesn't have the manipulate trait when cast this way."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Zealots ferret out plots against their religion and seek justice for their church's followers. This zealot serves Asmodeus, but others might serve Abadar, Calistria, Iomedae, Norgorber, Pharasma, Sarenrae, or Zon-Kuthon. They often ride a [[War Horse]] wearing light barding. To depict a zealot's mount, add this horse to the encounter as an additional monster with its own actions, adjusting the encounter's XP budget accordingly.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Zealot of Asmodeus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
