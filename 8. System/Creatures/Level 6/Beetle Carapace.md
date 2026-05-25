---
type: creature
group: ["Mindless", "Skeleton"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Beetle Carapace"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +15"
abilityMods: ["+5", "+3", "+4", "-5", "+2", "-2"]
abilities_top:
  - name: "Abdomen Cache"
    desc: "The abdomen of a beetle carapace can be fitted with a simple hinge, allowing it to open and be used as storage. The abdomen can hold up to one Medium or smaller creature, a Large or smaller swarm, or a similar amount of cargo. The beetle or a creature stored in it can Interact to open the hatch. If the beetle carapace takes a critical hit by a bludgeoning weapon, roll a DC 10 flat check. If the check fails, the cache is breached, and its contents spill out of the beetle. The hatch can also be Forced Open (DC 22 [[Athletics]] check)."
armorclass:
  - name: AC
    desc: "24; **Fort** +16, **Ref** +13, **Will** +10"
health:
  - name: HP
    desc: "90; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** cold 5, electricity 5, fire 5, piercing 5, slashing 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandible +15 (`pf2:1`), **Damage** 2d8+7 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Foot +15 (`pf2:1`) (unarmed), **Damage** 2d6+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d8+2)[piercing]], DC 24 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Created from the exoskeleton of a giant stag beetle, this mindless husk can cut a foe in half using its powerful mandibles. The abdomen of this crawling undead is empty, and more than one necromancer has used this space to hide valuable cargo.

Among the ranks of the dead, none are so numerous, nor so varied, as the skeleton. While most are almost entirely made from bone, some maintain a few scraps of flesh to aid them in movement, such as wing membranes.

```statblock
creature: "Beetle Carapace"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
