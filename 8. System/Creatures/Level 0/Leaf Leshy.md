---
type: creature
group: ["Leshy", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Leaf Leshy"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Leshy"
trait_02: "Plant"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Low-Light Vision]]"
languages: "Common, Fey (Speak with Plants (Trees Only))"
skills:
  - name: Skills
    desc: "Acrobatics +4, Nature +4, Stealth +4"
abilityMods: ["-1", "+2", "+2", "-2", "+2", "+1"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Deafening Blow"
    desc: "When a leaf leshy hits with their seedpod Strike, the pod explodes loudly. The target must attempt a DC 16 [[Fortitude]] save. <br> - **Critical Success** The target is unaffected and temporarily immune for 24 hours. <br> - **Success** The target is unaffected. <br> - **Failure** The target is [[Deafened]] for 1 round. <br> - **Critical Failure** The target is deafened for 1 minute."
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +6, **Will** +4"
health:
  - name: HP
    desc: "15; **Weaknesses** fire 2"
abilities_mid:
  - name: "Verdant Burst"
    desc: "When a leaf leshy dies, a burst of primal energy explodes from their body, restoring 1d4 Hit Points to each plant creature in a @Template[emanation|distance:30]. This area is filled with tree saplings, becoming difficult terrain. <br>  <br> If the terrain is not a viable environment for these trees, they wither after 24 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longspear +3 (`pf2:1`) (reach 10 ft.), **Damage** 1d8-1 piercing"
  - name: "Ranged strike"
    desc: "Seedpod +6 (`pf2:1`) (range 30 ft.), **Damage** 1d6 bludgeoning plus [[Deafening Blow]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 14, attack +6<br>**3rd** [[Speak with Plants (Constant, Trees Only)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The leaf leshy transforms into a Small tree. This ability otherwise uses the effects of [[One with Plants]]. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Glide"
    desc: "`pf2:1` The leshy glides gently through the air, moving 5 feet toward the ground and up to 25 feet forward. As long as the leshy spends at least 1 action gliding each round, they remain in the air at the end of each turn. For the purpose of determining damage from falls, a leaf leshy always treats falls as if they were 20 feet shorter."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Leaf leshies are diminutive protectors of forests clad in armor and hats made of fruit, flowers, or leaves. They enjoy mock battles but act cautiously in real ones.

Leshies are intelligent plant creatures who guard areas of primeval wilderness or earthly power. Originally created by powerful fey, they manifest when a skilled practitioner of primal magic—typically a druid—combines a nature spirit with a body carefully grown and crafted from local vegetation. The rites and materials required to create a leshy vary depending on the type of leshy. They are typically given life in an area of great natural significance, such as an arboreal's grove, a druidic circle, a fairy ring, or a great natural wonder.

```statblock
creature: "Leaf Leshy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
