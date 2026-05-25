---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Mosquito"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +13, Stealth +13"
abilityMods: ["+4", "+5", "+2", "-5", "+2", "-5"]
abilities_top:
  - name: "Septic Malaria"
    desc: "The victim can't reduce its [[Sickened]] condition while it's affected by septic malaria <br>  <br> **Saving Throw** DC 24 [[Fortitude]] save <br>  <br> **Onset** 1 day <br>  <br> **Stage 1** [[Sickened]] 1 (1 day) <br>  <br> **Stage 2** [[Drained]] 1 and [[Sickened]] 1 (1 day) <br>  <br> **Stage 3** as stage 2 (1 day) <br>  <br> **Stage 4** [[Unconscious]] (1 day) <br>  <br> **Stage 5** dead"
armorclass:
  - name: AC
    desc: "24; **Fort** +14, **Ref** +17, **Will** +12"
health:
  - name: HP
    desc: "80"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Proboscis +17 (`pf2:1`) (finesse), **Damage** 2d10+7 piercing plus [[Grab]] plus [[Septic Malaria]]"
spellcasting: []
abilities_bot:
  - name: "Blood Drain"
    desc: "`pf2:1` **Requirements** The giant mosquito has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The giant mosquito uses its proboscis to drain blood from the grabbed or restrained creature. This deals 3d6 piercing damage (DC 24 [[Fortitude]] save), and the giant mosquito gains temporary Hit Points equal to the damage dealt that last 1 minute. A creature that takes any damage from having its blood drained by a giant mosquito is [[Drained]] 1 until it receives any kind or amount of healing."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These horrifically enlarged versions of the common mosquito often prey upon megafauna like dinosaurs and other large creatures, but they won't turn down a chance to drink the blood of a smaller target-such as a humanoid.

```statblock
creature: "Giant Mosquito"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
