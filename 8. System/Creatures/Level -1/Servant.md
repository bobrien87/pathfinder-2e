---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Servant"
level: "-1"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +5, Diplomacy +4, Society +2, Lore (any one subcategory related to their job, such as Alcohol Lore, Baking Lore, or Household Lore) +4"
abilityMods: ["+1", "+3", "+1", "+0", "+1", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "14 (15 with platter raised); **Fort** +5, **Ref** +7, **Will** +3"
health:
  - name: HP
    desc: "7"
abilities_mid:
  - name: "Protective Platter"
    desc: "The servant can raise their serving platter using the Raise a Shield action. The platter has the same statistics as a [[Buckler]] but requires a hand to hold. <br>  <br> [[Raise a Shield]]"
  - name: "Quick Catch"
    desc: "`pf2:r` **Trigger** An object the servant could hold in one hand is dropped within the servant's reach <br>  <br> **Requirements** The servant has at least one hand free <br>  <br> **Effect** The servant catches the dropped object before it hits the floor or leaves their reach."
  - name: "Raise a Shield"
    desc: "`pf2:1` **Requirements** You are wielding a shield. <br>  <br> You position your shield to protect yourself. When you have Raised a Shield, you gain its listed circumstance bonus to AC. Your shield remains raised until the start of your next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Cutlery +6 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Cutlery +6 (`pf2:1`) (agile, thrown 15, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A servant might be a maid or butler, keeping a home in working order, or a server in an establishment like an inn, taking orders and serving customers.

Society is built upon the backs of laborers.

```statblock
creature: "Servant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
