---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Crab"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +8, Stealth +7"
abilityMods: ["+4", "+3", "+1", "-4", "+2", "-3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +7, **Ref** +9, **Will** +8"
health:
  - name: HP
    desc: "25; **Resistances** physical 3 except bludgeoning"
abilities_mid:
  - name: "Scuttle"
    desc: "`pf2:r` **Trigger** A creature that the giant crab can see targets the crab with an attack <br>  <br> **Effect** The giant crab scuttles to the side and gains a +2 circumstance bonus to AC against the triggering attack. After the attack resolves, the crab can Stride up to its speed in a straight line as part of the reaction."
  - name: "Vulnerable to Prone"
    desc: "If a creature critically succeeds on a check to [[Trip]] the giant crab, the crab is flipped over onto its back in addition to the usual effects. A giant crab that is flipped onto its back has a particularly hard time defending itself; instead of taking the normal -2 circumstance penalty to AC for being [[Off Guard]], it takes a -4 circumstance penalty to AC."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +9 (`pf2:1`) (unarmed), **Damage** 1d10+4 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d6+3)[bludgeoning]] damage, DC 18 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Crabs are scavenging crustaceans known for their hard shells and iconic sideways gait. They use their claws to defend themselves, hunt, and fight other crabs for territory. When confronted with threats from outside their species, most crabs prefer to flee, but when retreat isn't possible, they clamp on to their foes as tightly as they can.

The statistics presented here represent giant crabs that live close to the water's surface. Crabs that live deeper underwater often exhibit more extreme adaptations to their environment. Crabs who live in the depths where little light reaches gain darkvision and cold resistance, and those adapted to the most hostile reaches of the deep sea can detect nearby creatures through subtle shifts in ocean currents.

These skittering creatures are prized for their delicious meat, but their size makes them dangerous targets for harvesting.

```statblock
creature: "Giant Crab"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
