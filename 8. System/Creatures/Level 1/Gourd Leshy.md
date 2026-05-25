---
type: creature
group: ["Leshy", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gourd Leshy"
level: "1"
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
    desc: "+5; [[Low-Light Vision]]"
languages: "Common, Fey (Speak with Plants (Gourds Only))"
skills:
  - name: Skills
    desc: "Nature +5, Stealth +7"
abilityMods: ["+2", "+4", "+2", "-1", "+2", "+0"]
abilities_top:
  - name: "Keepsake"
    desc: "The leshy can store an item of light Bulk or less in their head, concealing it as [[Veil of Privacy]]. If stored for 24 hours, the item benefits from [[Mending]]."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Ensnare"
    desc: "When the gourd leshy damages a creature with a fist or seed Strike, vines lash out from the leshy (or seed) and wrap around the target's limbs. <br>  <br> The target must attempt a DC 17 [[Reflex]] save. On a failure, the target takes a –10-foot status penalty to its Speed for 1 round; on a critical failure, the target is [[Immobilized]] for 1 round and the penalty to Speed lasts for 1 minute. <br>  <br> > [!danger] Effect: Ensnare"
armorclass:
  - name: AC
    desc: "17; **Fort** +5, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Verdant Burst"
    desc: "When a gourd leshy dies, a burst of primal energy explodes from their body, restoring 1d8 Hit Points to each plant creature in a @Template[emanation|distance:30]. This area is filled with gourds, becoming difficult terrain. <br>  <br> If the terrain is not a viable environment for these gourds, they wither after 24 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4+2 bludgeoning plus [[Ensnare]]"
  - name: "Ranged strike"
    desc: "Seed +9 (`pf2:1`) (range 30 ft.), **Damage** 1d6+2 bludgeoning plus [[Ensnare]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 15, attack +7<br>**3rd** [[Speak with Plants (Constant, Gourds Only)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The gourd leshy transforms into a Small gourd-bearing plant. This ability otherwise uses the effects of [[One with Plants]]. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Gourd leshies are guardians of fields, gardens, and farms. Many villages benefit from the protection of a gourd leshy, even if they are unaware of it.

Leshies are intelligent plant creatures who guard areas of primeval wilderness or earthly power. Originally created by powerful fey, they manifest when a skilled practitioner of primal magic—typically a druid—combines a nature spirit with a body carefully grown and crafted from local vegetation. The rites and materials required to create a leshy vary depending on the type of leshy. They are typically given life in an area of great natural significance, such as an arboreal's grove, a druidic circle, a fairy ring, or a great natural wonder.

```statblock
creature: "Gourd Leshy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
