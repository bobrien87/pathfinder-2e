---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Archer Sentry"
level: "2"
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
    desc: "+11"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +6, Intimidation +4, Legal Lore +4"
abilityMods: ["+2", "+4", "+1", "+0", "+3", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+4 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Longbow +10 (`pf2:1`) (deadly d10, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 1d8+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Sentry's Aim"
    desc: "`pf2:2` The archer sentry aims carefully and fires. They make a ranged weapon Strike with a +1 circumstance bonus. <br>  <br> The Strike ignores the [[Concealed]] condition, lesser  <br>  <br> > [!danger] Effect: Cover <br>  <br> , and standard cover, and reduces greater cover to standard cover."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Archer sentries slightly outrank rank-and-file guards, taking positions on walls, garrisons, and other important locations where they can stay out of the fray and pick off criminals or assailants.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Archer Sentry"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
