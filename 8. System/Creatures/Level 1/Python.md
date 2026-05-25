---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Python"
level: "1"
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
    desc: "+6; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +6, Stealth +6, Survival +4"
abilityMods: ["+3", "+3", "+3", "-4", "+1", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +8, **Ref** +10, **Will** +4"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Tighten Coils"
    desc: "`pf2:r` **Trigger** A creature [[Grabbed]] or [[Restrained]] by the python attempts to [[Escape]]. <br>  <br> **Effect** The DC of the Escape check is increased by 2."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +8 (`pf2:1`) (unarmed), **Damage** 1d8+3 piercing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d8)[bludgeoning]], DC 17 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Wrap in Coils"
    desc: "`pf2:1` **Requirements** A Medium or smaller creature is [[Grabbed]] or [[Restrained]] in the python's jaws. <br>  <br> **Effect** The python moves the creature into its coils, freeing its jaws to make attacks, then uses Constrict against the creature. The python's coils can hold one creature."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

This nonvenomous family of snakes is rarely a threat to anything but small mammals and birds, hunting by coiling around prey and crushing victims with their powerful muscles. Nonetheless, larger pythons can be dangerous due to their strength. Herpetologists sometimes keep pythons as pets.

Snakes come in an array of forms, from jungle-dwelling constrictors that wrap around their prey to venomous vipers with deadly bites. Regardless, all snakes consume their prey whole by unhinging their jaws and using powerful muscles to move the food down their throats and into their stomachs.

```statblock
creature: "Python"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
