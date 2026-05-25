---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sand Sentry"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]], [[Tremorsense]] (imprecise) 60 feet"
languages: "Petran"
skills:
  - name: Skills
    desc: "Acrobatics +14, Stealth +14"
abilityMods: ["+5", "+2", "+4", "+0", "+2", "+1"]
abilities_top:
  - name: "Blinding Sand"
    desc: "When the sand sentry critically hits with a fist Strike, the target is [[Blinded]] for 1 round."
  - name: "Earth Glide"
    desc: "A sand sentry can [[Burrow]] through earthen matter, including rock. When it does so, it moves at its full burrow Speed, leaving no tunnels or signs of its passing."
armorclass:
  - name: AC
    desc: "24; **Fort** +16, **Ref** +12, **Will** +14"
health:
  - name: HP
    desc: "90; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Glass Armor"
    desc: "When the sand sentry takes electricity or fire damage, its outer layer of sand fuses into sheets of hardened glass for 1 minute. This increases the sand sentry's AC to 26 and grants it resistance 5 to acid, cold, electricity, fire, force, piercing, and slashing damage. A sand sentry can't use earth glide while glass armor is active."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +17 (`pf2:1`) (unarmed), **Damage** 2d8+8 bludgeoning plus [[Blinding Sand]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

This creature of pure sand moves with an eerie grace, shifting back and forth between a detailed likeness of a human and a muted and featureless bipedal form. The sand sentry is often called upon by spellcasters to stand guard over an area of great importance; these elementals are patient participants in such roles, making them well suited for long-term service.

Certain earth elementals manifest as specific types of material, be they boulders, sand, or crystals.

```statblock
creature: "Sand Sentry"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
