---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Standard Bearer"
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
languages: "Common"
skills:
  - name: Skills
    desc: "Diplomacy +11, Medicine +10, Society +8, Warfare Lore +10"
abilityMods: ["+2", "+2", "+2", "+0", "+2", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +10, **Ref** +8, **Will** +14"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Inspiring Aura"
    desc: "60 feet. The standard bearer and each ally in the aura who can see their battle standard gains a +1 status bonus to initiative rolls and saves against fear effects. Each time an affected creature gains the [[Frightened]] condition, reduce the frightened value by 1."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ranseur +12 (`pf2:1`) (disarm, reach 10 ft.), **Damage** 1d10+8 piercing"
  - name: "Melee strike"
    desc: "Shortsword +12 (`pf2:1`) (agile, versatile s), **Damage** 1d6+8 piercing"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Signal the Advance!"
    desc: "`pf2:2` The standard bearer raises their flag to the sky, signaling their allies to charge. Each ally affected by inspiring aura can use a reaction to Stand, Step, or Stride."
  - name: "Stay in the Fight!"
    desc: "`pf2:2` The standard bearer shouts an inspiring cry. Each ally affected by inspiring aura gains 10 temporary Hit Points that last for 1 minute. <br>  <br> > [!danger] Effect: Stay in the Fight!"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Within a troop, the standard bearer is a beacon of morale, cohesion, and camaraderie. They proudly wave the flag of the entity they fight for. Whether they lead the spearhead or provide support from the back lines, their presence alone is usually enough to rally the soldiers around them to continue fighting.

A military serves to defend and fight on behalf of nations and can be trained and deployed in various ways.

```statblock
creature: "Standard Bearer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
