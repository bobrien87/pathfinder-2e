---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jabali"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: "Genie"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]], [[Tremorsense]] (imprecise) 60 feet"
languages: "Common, Petran (Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +19, Crafting +14, Deception +16, Nature +15, Society +14"
abilityMods: ["+6", "+1", "+4", "+3", "+2", "+3"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Earth Glide"
    desc: "The jabali can [[Burrow]] through dirt and stone at its full burrow Speed, leaving no tunnels or signs of its passing."
  - name: "Stone Clutch"
    desc: "When the jabali Pushes a creature into a stone barrier, the surface grips it with fingers of stone. The target must succeed at a DC 22 [[Reflex]] save or become [[Grabbed]] by the surface (`act escape dc=28`)."
armorclass:
  - name: AC
    desc: "25; **Fort** +18, **Ref** +12, **Will** +15"
health:
  - name: HP
    desc: "110"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Falchion +20 (`pf2:1`) (forceful, magical, reach 10 ft., sweep), **Damage** 1d10+12 slashing"
  - name: "Melee strike"
    desc: "Fist +19 (`pf2:1`) (agile, magical, nonlethal, reach 10 ft., unarmed), **Damage** 1d4+12 bludgeoning plus [[Push]] plus [[Shove Into Stone]]"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 24, attack +16<br>**7th** [[Interplanar Teleport (to Astral Plane, Elemental Planes, or the Universe only)]]<br>**5th** [[Truespeech]] (Constant), [[Wall of Stone]]<br>**4th** [[Shape Stone]] (At Will)<br>**1st** [[Detect Magic]]"
abilities_bot:
  - name: "Push 10 feet"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The proud and brazen jabalis of the Plane of Earth value physical skill and love bargaining, games of chance, and working with metal and stone.

Before mortal history, genies were some of the first creations of the cosmos to possess free will. Formed of elemental matter, they traversed the Universe and the six elemental planes of air, earth, fire, metal, water, and wood. The genies who remained on each elemental plane found their matter replaced with those elements. Genies of metal and wood appear in *Pathfinder Rage of Elements*.

Genie Shuyookhs
Older, wiser, and more powerful genies possess greater power and are revered with the title of shuyookh (typically adjusted to "sheikha" if the genie is female or "sheikh" for a male). Generally at least 5 levels higher than a typical example of their kind, a shuyookh gains additional spells. The basics of shuyookhs appear here in sidebars and are detailed further in *Rage of Elements*.

The most wondrous of their powers is their ability to grant wishes three times per year. This is not an innate ability but a ritual practice passed down over time in an attempt to replicate the wish-granting abilities of janns.

```statblock
creature: "Jabali"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
