---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mukradi"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+24; [[Darkvision]], [[Tremorsense]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +32"
abilityMods: ["+9", "+0", "+7", "-3", "+3", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "37 all-around vision; **Fort** +32, **Ref** +23, **Will** +26"
health:
  - name: HP
    desc: "300; **Resistances** acid 20, electricity 20, fire 20"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Partitioned Anatomy"
    desc: "`pf2:0` **Trigger** The mukradi would be [[Confused]], [[Paralyzed]], [[Slowed]], or [[Stunned]] <br>  <br> **Effect** The mukradi confines the debilitating effect to a certain portion of its nervous system, ignoring the effect but causing a maw of its choice to go dormant for the effect's duration. That maw can't be used for a Strike or to Breathe Energy during that time. This ability can't be used if all the mukradi's heads are dormant."
  - name: "Spitting Rage"
    desc: "`pf2:r` **Trigger** A creature scores a critical hit on the mukradi <br>  <br> **Effect** The mukradi's Breathe Energy recharges. It can use Breathe Energy immediately as part of this reaction. It can't use this reaction again until it recharges Breathe Energy naturally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Acid Maw +32 (`pf2:1`) (magical, reach 20 ft.), **Damage** 2d12+17 piercing plus 3d6 acid"
  - name: "Melee strike"
    desc: "Flame Maw +32 (`pf2:1`) (magical, reach 20 ft.), **Damage** 2d12+17 piercing plus 3d6 fire"
  - name: "Melee strike"
    desc: "Shock Maw +32 (`pf2:1`) (magical, reach 20 ft.), **Damage** 2d12+17 piercing plus 3d6 electricity"
  - name: "Melee strike"
    desc: "Leg +32 (`pf2:1`) (agile, magical, reach 15 ft.), **Damage** 2d10+17 piercing"
  - name: "Melee strike"
    desc: "Tail Lash +32 (`pf2:1`) (magical, reach 30 ft.), **Damage** 3d10+17 slashing plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Breathe Energy"
    desc: "`pf2:2` The mukradi breathes a blast of energy from one of its three heads; each creature in the area must attempt a DC 36 [[Reflex]] save. <br>  <br> The mukradi can't Breathe Energy again for 1d4 rounds. <br>  <br> - **Acid Maw** (acid) 10-foot-wide, @Template[line|distance:60|width:10] of acid dealing @Damage[16d6[acid]|options:area-damage] damage. <br> - **Flame Maw** (fire) @Template[cone|distance:60] of fire dealing @Damage[16d6[fire]|options:area-damage] damage. <br> - **Shock Maw** (electricity) @Template[line|distance:120] of electricity dealing @Damage[16d6[electricity]|options:area-damage] damage."
  - name: "Pull Apart"
    desc: "`pf2:2` The mukradi makes two Strikes with different maws against the same target. If both hit, the target takes an extra @Damage[(2d12+13)[slashing]] damage, with a DC 36 [[Fortitude]] save. On a critical failure, the creature is torn to pieces and dies. <br>  <br> The mukradi's multiple attack penalty increases only after all the attacks are made."
  - name: "Thrash"
    desc: "`pf2:2` The mukradi Strikes once against each creature in its reach. It can make one of these Strikes with each of its maws, one with its tail lash, and the rest with its legs. Each attack takes a –2 circumstance penalty and counts toward the mukradi's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks are made."
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, leg, DC 36 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Fearsome centipede-like creatures, mukradis are three-headed predators with a devastating array of ways to kill, burn, and dismember. A version of the mukradi that dwells in the Darklands is rumored to exist. It's said these variant mukradis have black scales, and all of their heads spew a black, acidic goo that animates before being reabsorbed by the mukradis.

```statblock
creature: "Mukradi"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
