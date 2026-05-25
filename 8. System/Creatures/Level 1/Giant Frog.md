---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Frog"
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
    desc: "+7; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +6, Stealth +7"
abilityMods: ["+3", "+2", "+3", "-4", "+2", "-1"]
abilities_top:
  - name: "Sticky Feet"
    desc: "Giant frogs are not off-guard when [[Balancing]] on a narrow surface, and they gain a +4 circumstance bonus to Reflex saves to avoid falling."
  - name: "Tongue Grab"
    desc: "A creature hit by the giant frog's tongue becomes [[Grabbed]] by the giant frog. The creature isn't [[Immobilized]], but it can't move beyond the reach of the frog's tongue. A creature can sever the tongue with a Strike against AC 13 that deals at least 2 slashing damage. This deals no damage to the frog but prevents it from using its tongue Strike until it regrows its tongue, which takes a week."
armorclass:
  - name: AC
    desc: "15; **Fort** +8, **Ref** +7, **Will** +5"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +8 (`pf2:1`), **Damage** 1d6+3 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tongue +8 (`pf2:1`) (reach 15 ft.), **Damage**  plus [[Tongue Grab]]"
spellcasting: []
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Giant frogs can grow up to 6 feet long and weigh over 200 pounds, with rows of razor-sharp teeth lining their gaping mouths.

Frogs that are poisonous or grow to monstrous size can be a menace to adventurers.

```statblock
creature: "Giant Frog"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
