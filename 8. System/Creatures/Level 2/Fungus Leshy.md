---
type: creature
group: ["Fungus", "Leshy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fungus Leshy"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Fungus"
trait_02: "Leshy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: "Common, Fey (Speak with Plants (Fungi Only))"
skills:
  - name: Skills
    desc: "Athletics +6, Nature +6, Stealth +8"
abilityMods: ["+2", "+4", "+2", "-1", "+2", "+0"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Spores"
    desc: "A creature that takes damage from a fungus leshy's spore pod Strike must attempt a saving throw with the same DC (DC 16 [[Fortitude]] save) and effect as its Spore Cloud ability"
armorclass:
  - name: AC
    desc: "19; **Fort** +8, **Ref** +10, **Will** +6"
health:
  - name: HP
    desc: "30"
abilities_mid:
  - name: "Verdant Burst"
    desc: "When a fungus leshy dies, a burst of primal energy explodes from its body, restoring 2d8 healing Hit Points to each fungi creature in a @Template[emanation|distance:30]. This area is filled with fungi, becoming difficult terrain. <br>  <br> If the terrain is not a viable environment for this fungi, they wither after 24 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d6+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Spore Pod +10 (`pf2:1`) (range 30 ft.), **Damage** 1d6+2 bludgeoning plus [[Spores]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16, attack +8<br>**3rd** [[Speak with Plants (Constant, Fungi Only)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The fungus leshy transforms into a giant mushroom or patch of fungi. This ability otherwise uses the effects of [[One with Plants]]. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Spore Cloud"
    desc: "`pf2:2` A fungus leshy can unleash a cloud of spores that irritates the eyes and throats of non-fungus creatures in a @Template[emanation|distance:15]. Each creature must succeed at a DC 16 [[Fortitude]] save or take @Damage[1[persistent,poison]|options:area-damage] damage. <br>  <br> A creature has its vision reduced as long as the persistent damage continues and can see only within 20 feet."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Fungus leshies guard caves, bogs, and damp, dark places. Their fungus gardens are bizarre by most standards, but fungus leshies are extremely proud of their works.

Leshies are intelligent plant creatures who guard areas of primeval wilderness or earthly power. Originally created by powerful fey, they manifest when a skilled practitioner of primal magic—typically a druid—combines a nature spirit with a body carefully grown and crafted from local vegetation. The rites and materials required to create a leshy vary depending on the type of leshy. They are typically given life in an area of great natural significance, such as an arboreal's grove, a druidic circle, a fairy ring, or a great natural wonder.

```statblock
creature: "Fungus Leshy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
