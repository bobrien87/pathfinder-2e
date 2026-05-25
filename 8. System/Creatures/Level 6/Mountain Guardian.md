---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mountain Guardian"
level: "6"
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
    desc: "+9; [[Tremorsense]] (imprecise) 10 feet"
languages: "Common, Petran"
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +15, Intimidation +13, Nature +11, Survival +9"
abilityMods: ["+4", "+1", "+4", "+0", "+1", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24; **Fort** +14, **Ref** +11, **Will** +11"
health:
  - name: HP
    desc: "100; **Resistances** earth 6, poison 6"
abilities_mid:
  - name: "+2 to Reflex vs. Damaging Effects"
    desc: ""
  - name: "Kinetic Aura"
    desc: "10 feet. Pieces of rock and earth float in the aura. The aura must be active for the guardian to use impulse actions, and deactivates if the guardian uses an overflow impulse, is knocked out, or Dismisses it. The guardian can Channel Elements to reactivate it."
  - name: "Weight of Stone"
    desc: "`pf2:3` The mountain guardian calls down boulders in a cylinder @Template[cylinder|distance:10]{20 feet in diameter} and 80 feet high within 120 feet. Each creature in the area takes @Damage[4d8[bludgeoning]|options:area-damage] damage with a DC 24 [[Reflex]] save. A creature that fails is also pushed downward 40 feet (80 feet on a critical failure) without taking falling damage and can't leave the ground for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Elemental Blast +16 (`pf2:1`) (concentrate, earth, impulse, primal, versatile p), **Damage** 2d8+4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Elemental Blast +16 (`pf2:1`) (concentrate, earth, impulse, primal, versatile p, range 30 ft.), **Damage** 2d8 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Base Kinesis"
    desc: "`pf2:2` The mountain guardian generates, moves, or suppresses up to 1 Bulk of naturally occurring earthen matter within 15 feet. Generating creates earthen matter, moving moves existing matter up to 20 feet into any direction, and suppressing destroys a piece of that element (which can't be a durable crafted good, only natural forms of the element)."
  - name: "Channel Elements"
    desc: "`pf2:1` The mountain guardian reactivates their kinetic aura and can make an elemental blast Strike."
  - name: "Empowered Blast"
    desc: "`pf2:2` The mountain guardian makes a melee or ranged elemental blast Strike with a +4 status bonus to damage."
  - name: "Tremor"
    desc: "`pf2:2` The mountain guardian stomps on natural earth or stone, causing a localized tremor. All creatures in a @Template[type:burst|distance:10] within 30 feet take @Damage[3d10[bludgeoning]|options:area-damage] damage with a DC 24 [[Fortitude]] save. A creature that critically fails is knocked [[Prone]]. Earth and stone in the area is difficult terrain until the start of the mountain guardian's next turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Those who have unlocked the secrets of opening a kinetic gate to an elemental plane within themselves wield immense power over that element. Practitioners who specialize in elemental earth are hardy and defense-minded. The mountain guardian is surrounded by heavy armor made of stone held together with elemental magic.

A primalist is a wielder of primal energies and magic, sometimes taught by forces of primal power, including powerful elementals or fey of the First World. Primalists protect the natural world, offering strong medicine to those in need while facing suspicion from those who don't understand their ways.

A great many primalists belong to druidic circles, and even those who aren't members tend to be familiar with the most prominent ones in their homeland.

```statblock
creature: "Mountain Guardian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
