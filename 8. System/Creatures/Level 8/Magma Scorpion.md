---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Magma Scorpion"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +16"
abilityMods: ["+6", "+3", "+5", "-4", "+4", "+0"]
abilities_top:
  - name: "Smoke Vision"
    desc: "The magma scorpion ignores the [[Concealed]] condition from smoke."
  - name: "Magma Scorpion Venom"
    desc: "**Saving Throw** DC 26 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 2d6 fire damage (1 round) and [[Enfeebled]] 1 <br>  <br> **Stage 2** 3d6 fire damage and [[Enfeebled]] 2 (1 round)"
armorclass:
  - name: AC
    desc: "27; **Fort** +19, **Ref** +14, **Will** +16"
health:
  - name: HP
    desc: "155; **Immunities** bleed, fire, paralyzed, poison, sleep; **Weaknesses** cold 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pincer +20 (`pf2:1`) (agile, reach 10 ft.), **Damage** 2d6+9 bludgeoning plus 1d6 fire plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tail Sting +20 (`pf2:1`) (reach 10 ft.), **Damage** 1d10+9 piercing plus 1d6 fire plus [[Magma Scorpion Venom]]"
  - name: "Ranged strike"
    desc: "Magma Spit +17 (`pf2:1`) (fire, range 40 ft.), **Damage** 1d6+9 fire plus 1d6 fire"
spellcasting: []
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Whether skittering through Chthonian wastelands or basking in the searing sand of the deepest deserts, magma scorpions have charred carapaces, constantly emitting vision-warping waves of heat.

Destructive manifestations of the Plane of Fire, fire elementals sometimes incorporate burning materials into their being or superheated matter, such as molten rock or searing smoke. In combat, they tend to be aggressive and somewhat reckless. Their attacks can sometimes cause major destruction to the surrounding environment, and many fire elementals seem to enjoy seeing their flames spread far and wide.

```statblock
creature: "Magma Scorpion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
