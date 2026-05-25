---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Granite Glyptodont"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]], [[Tremorsense]] (imprecise) 90 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +18"
abilityMods: ["+6", "+1", "+6", "+0", "+5", "+0"]
abilities_top:
  - name: "Calcification"
    desc: "A blow from a granite glyptodont's tail Strike hardens the flesh of the creature struck. The target must succeed at a DC 26 [[Fortitude]] save or become [[Slowed]] 1 ([[Slowed]] 2 on a critical failure). Further failed saves against calcification increase the value of the slowed condition. Once a creature's actions are reduced to 0 by calcification, that creature becomes [[Petrified]]. If the creature isn't petrified, the slowed conditions end once 1 minute passes without the creature failing a save against calcification. <br>  <br> Every 24 hours after it was petrified, the creature can attempt a DC 26 [[Fortitude]] save to recover. On a success, it becomes flesh again but is slowed 1 for the next 24 hours. On a critical success, the creature recovers and isn't slowed. On a failure, the creature remains petrified but can try again in 24 hours. On a critical failure, the petrification is permanent, and the creature can't attempt any more saves."
  - name: "Earth Glide"
    desc: "A granite glyptodont can [[Burrow]] through earthen matter, including rock. When it does so, it moves at its full burrow Speed, leaving no tunnels or signs of its passing."
armorclass:
  - name: AC
    desc: "27; **Fort** +18, **Ref** +13, **Will** +17"
health:
  - name: HP
    desc: "145; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tail +20 (`pf2:1`) (forceful, reach 10 ft., versatile p), **Damage** 2d12+9 bludgeoning plus [[Calcification]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

This squat and stony creature looks like an armadillo with a large raised back and a flail-like tail. The granite glyptodont has no true need to feed, as with all elementals, yet it does seem to linger after transforming the flesh of those it calcifies, as if the mere proximity of flesh fossilizing into stone pleases it somehow.

Certain earth elementals manifest as specific types of material, be they boulders, sand, or crystals.

```statblock
creature: "Granite Glyptodont"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
