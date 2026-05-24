---
statblock: true
layout: Basic Pathfinder 2e Layout
type: creature
group: ["Beast"]
name: "Owlbear"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: "Unaligned"
size: "Large"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; Low-Light Vision, Scent (imprecise) 30 feet"
languages: "None"
skills:
  - name: Skills
    desc: "Athletics +14, Intimidation +8"
abilityMods: ["+6", "+1", "+5", "-4", "+3", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +13, **Ref** +7, **Will** +11"
health:
  - name: HP
    desc: "70"
abilities_mid: []
speed: "25 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +14 (`pf2:1`), **Damage** 1d12+6 piercing"
  - name: "Melee strike"
    desc: "Talon +14 (`pf2:1`) (agile), **Damage** 1d10+6 slashing plus Grab"
  - name: "Screeching Growl"
    desc: "`pf2:1` (concentrate, emotion, fear, mental) The owlbear emits a terrifying screech. Each creature within 30 feet must succeed on a DC 20 Will save or become frightened 1 (frightened 2 on a critical failure)."
  - name: "Gnaw"
    desc: "`pf2:1` **Requirements** The owlbear has a creature grabbed in its talon Strike; **Effect** The owlbear makes a beak Strike against the grabbed creature. On a hit, the creature is also enfeebled 1 for 1 minute."
spellcasting: []
abilities_bot: []
sourcebook: "Bestiary"
source-type: "Remaster"
---
### `= this.file.name`

A aggressive beast combining the features of a bear and an owl.

```statblock
creature: "Owlbear"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
