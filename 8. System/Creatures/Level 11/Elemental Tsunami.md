---
type: creature
group: ["Aquatic", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Elemental Tsunami"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: "Thalassic"
skills:
  - name: Skills
    desc: "Athletics +23, Stealth +23"
abilityMods: ["+6", "+6", "+6", "+0", "+3", "+0"]
abilities_top:
  - name: "Waterbound"
    desc: "When not touching water, the elemental tsunami is [[Slowed]] 1 and can't use reactions."
armorclass:
  - name: AC
    desc: "31; **Fort** +21, **Ref** +22, **Will** +19"
health:
  - name: HP
    desc: "195; **Immunities** bleed, paralyzed, poison, sleep; **Resistances** fire 10"
abilities_mid:
  - name: "Vortex"
    desc: "50 feet. <br>  <br> Water in the area that is in the same body of water as the elemental tsunami is difficult terrain for Swimming creatures that don't have the water trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Wave +24 (`pf2:1`) (reach 20 ft.), **Damage** 2d12+12 bludgeoning plus [[Push Or Pull 10 Feet]]"
spellcasting: []
abilities_bot:
  - name: "Drench"
    desc: "`pf2:1` The elemental puts out all fires in a @Template[emanation|distance:20]. <br>  <br> It extinguishes all non-magical fires automatically and attempts to counteract magical fires (+20 counteract modifier)."
  - name: "Surge"
    desc: "`pf2:2` The elemental tsunami momentarily expands to fill the area of its vortex. Creatures within the aura take @Damage[(5d12+6)[bludgeoning]|options:area-damage] damage with a DC 31 [[Fortitude]] save. A creature that fails this save is pushed 20 feet. <br>  <br> The elemental tsunami then shrinks to its normal space and can't Surge again for 1d4 rounds."
  - name: "Push or Pull 10 feet"
    desc: "`pf2:1` The elemental tsunami can choose whether to push or pull the creature on a successful hit. <br>  <br> **Push** `pf2:1` <br>  <br> **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance. <br>  <br> **Pull** `pf2:1` <br>  <br> **Requirements** The monster's last action was a success with a Strike that lists Pull in its damage entry <br>  <br> **Effect** The monster attempts to [[Reposition]] the creature, moving it closer to the monster. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Pull lists a distance, change the distance the creature is pulled on a success to that distance."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Elemental tsunamis are huge and destructive, having none of the caring or nurturing aspects of water.

Water elementals can be very destructive, but often not intentionally so; just as water can bring life to mortals in need, its waves can pound shores and rains can flood cities. Water elementals are similarly difficult to predict.

```statblock
creature: "Elemental Tsunami"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
