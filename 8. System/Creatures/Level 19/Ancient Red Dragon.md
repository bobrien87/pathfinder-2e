---
type: creature
group: ["Dragon", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: Ancient Red Dragon
level: "19"
rare_01: Rare
rare_02: ""
rare_03: ""
rare_04: ""
alignment: Chaotic Evil
size: Gargantuan
trait_01: Dragon
trait_02: Fire
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: +35; Darkvision, Scent (imprecise) 60 feet
languages: Common, Draconic
skills:
  - name: Skills
    desc: Acrobatics +29, Athletics +38, Deception +34, Diplomacy +34, Intimidation +36, Religion +32, Society +32
abilityMods:
  - "+9"
  - "+5"
  - "+8"
  - "+5"
  - "+6"
  - "+7"
abilities_top:
  - name: Dragon Heat (Aura)
    desc: 10 feet, 4d6 fire damage (DC 39 basic Reflex save)
  - name: Frightful Presence (Aura)
    desc: 90 feet, DC 40
armorclass:
  - name: AC
    desc: 45 (+1 status vs. magic); **Fort** +35, **Ref** +32, **Will** +35
health:
  - name: HP
    desc: 425; **Immunities** fire; **Weaknesses** cold
abilities_mid:
  - name: Redirect Fire
    desc: "`pf2:r` **Trigger** A creature within 100 feet casts a fire spell or activates a fire item; **Effect** The dragon attempts to redirect the fire spell or effect. The dragon makes a counteract check (+33 counteract modifier). If successful, the dragon chooses the target or area of the spell/effect."
speed: 60 feet, fly 180 feet
attacks:
  - name: Melee strike
    desc: Bite +37 (`pf2:1`) (reach 20 ft.), **Damage** 4d10+17 piercing plus 3d6 fire
  - name: Melee strike
    desc: Claw +37 (`pf2:1`) (reach 15 ft., agile), **Damage** 4d8+17 slashing
  - name: Melee strike
    desc: Tail +35 (`pf2:1`) (reach 25 ft.), **Damage** 4d10+17 bludgeoning
  - name: Melee strike
    desc: Wing +35 (`pf2:1`) (reach 20 ft., agile), **Damage** 4d8+17 slashing
  - name: Draconic Frenzy
    desc: "`pf2:2` The dragon makes two claw Strikes and one wing Strike."
  - name: Breath Weapon
    desc: "`pf2:2` (fire) The dragon exhales fire in a 60-foot cone, dealing 20d6 fire damage (DC 42 basic Reflex save)."
  - name: Draconic Momentum
    desc: When the dragon scores a critical hit with a Strike, its Breath Weapon recharges.
spellcasting: []
abilities_bot: []
sourcebook: Bestiary
source-type: Legacy
---
### `= this.file.name`

A massive, prideful, and destructive ancient red dragon.

```statblock
creature: "Ancient Red Dragon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
