---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Court Jester"
level: "10"
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
    desc: "+21"
languages: "Common (up to 4 others)"
skills:
  - name: Skills
    desc: "Acrobatics +22, Deception +19, Diplomacy +19, Performance +22, Society +19, Stealth +19"
abilityMods: ["+2", "+4", "+1", "+2", "+1", "+5"]
abilities_top:
  - name: "Poisoned Blade"
    desc: "The jester coats their dagger in poison. These daggers inflict an additional 4d4 persistent poison damage. The poison expires 1 hour after leaving the jester's possession."
armorclass:
  - name: AC
    desc: "29; **Fort** +16, **Ref** +19, **Will** +22"
health:
  - name: HP
    desc: "170; **Resistances** poison 10"
abilities_mid:
  - name: "Pointed Joke"
    desc: "The court jester can use Performance instead of Intimidation to `act demoralize statistic=performance`."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +22 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 2d4+8 piercing"
  - name: "Melee strike"
    desc: "Dagger +22 (`pf2:1`) (agile, magical, thrown 10, versatile s), **Damage** 2d4+8 piercing"
  - name: "Melee strike"
    desc: "Fist +21 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "No Peeking!"
    desc: "`pf2:1` The jester blows chalk or face powder in an adjacent enemy's face. The target must make a DC 29 [[Fortitude]] save saving throw. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target is [[Dazzled]] for 1 round. <br> - **Failure** target is dazzled and [[Off Guard]] for 1 round. <br> - **Critical Failure** The target is [[Blinded]] for 1 round."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Though court jesters are often put-upon as the targets of easy mockery and idle amusements, do not mistake their self-deprecation for weakness. Beneath, the jester hides malice, a sharp tongue, and even sharper knives. They can often be found entertaining the nobles of court or preparing their next japes. During the indiscreet hours of the night, they may be found in the company of servants and spymasters.

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Court Jester"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
