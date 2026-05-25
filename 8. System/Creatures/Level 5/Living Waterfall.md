---
type: creature
group: ["Aquatic", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Living Waterfall"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Thalassic"
skills:
  - name: Skills
    desc: "Athletics +13, Stealth +12"
abilityMods: ["+4", "+3", "+3", "-2", "+1", "+0"]
abilities_top:
  - name: "Waterbound"
    desc: "When not touching water, the living waterfall is [[Slowed]] 1 and can't use reactions."
armorclass:
  - name: AC
    desc: "20; **Fort** +14, **Ref** +12, **Will** +10"
health:
  - name: HP
    desc: "90; **Immunities** bleed, paralyzed, poison, sleep; **Resistances** fire 5"
abilities_mid:
  - name: "Vortex"
    desc: "30 feet. <br>  <br> Water in the area that is in the same body of water as the living waterfall is difficult terrain for Swimming creatures that don't have the water trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Wave +15 (`pf2:1`) (reach 10 ft.), **Damage** 2d8+7 bludgeoning plus [[Push Or Pull]]"
spellcasting: []
abilities_bot:
  - name: "Drench"
    desc: "`pf2:1` The elemental puts out all fires in a @Template[emanation|distance:5]. <br>  <br> It extinguishes all non-magical fires automatically and attempts to counteract magical fires (+14 counteract modifier)."
  - name: "Push or Pull 5 feet"
    desc: "`pf2:1` The living waterfall can choose whether to push or pull the creature on a successful hit. <br>  <br> **Push** `pf2:1` <br>  <br> **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance. <br>  <br> **Pull** `pf2:1` <br>  <br> **Requirements** The monster's last action was a success with a Strike that lists Pull in its damage entry <br>  <br> **Effect** The monster attempts to [[Reposition]] the creature, moving it closer to the monster. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Pull lists a distance, change the distance the creature is pulled on a success to that distance."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Living waterfalls are humanoid-shaped columns of churning water. They see the water as their natural domain and even aquatic animals as interlopers. When summoned, they are surly, but will grudgingly guard all forms of aquatic sites.

Water elementals can be very destructive, but often not intentionally so; just as water can bring life to mortals in need, its waves can pound shores and rains can flood cities. Water elementals are similarly difficult to predict.

```statblock
creature: "Living Waterfall"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
