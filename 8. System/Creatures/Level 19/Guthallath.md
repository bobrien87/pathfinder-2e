---
type: creature
group: ["Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Guthallath"
level: "19"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Construct"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +40"
abilityMods: ["+10", "+2", "+8", "-4", "+0", "-1"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Powerful Blows"
    desc: "If a guthallath hits with an attack and rolls a natural 19 on the d20 roll, the attack is a critical hit. This has no effect if the 19 would be a failure."
armorclass:
  - name: AC
    desc: "43; **Fort** +38, **Ref** +32, **Will** +30"
health:
  - name: HP
    desc: "325; **Resistances** physical 15 except adamantine, spells 15 except cold, earth, water"
abilities_mid:
  - name: "Erosion Aura"
    desc: "120 feet. <br>  <br> The guthallath erodes away the physical integrity of all around it. Creatures and objects in the emanation other than the guthallath have their Hardness and resistances reduced by 10. <br>  <br> At the start of their turn, a creature in the erosion aura's area takes 6d6 bludgeoning damage with a DC 39 [[Fortitude]] save."
  - name: "Immunity to Magic"
    desc: "The guthallath is immune to spells of 6th rank or lower and activations of magic items of 13th level or lower."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
  - name: "Improved Knockdown"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature as a free action. This attempt neither applies nor counts toward the monster's multiple attack penalty."
  - name: "Improved Push 20 feet"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Improved Push lists a distance, change the distance the creature is pushed on a success to that distance."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +38 (`pf2:1`) (deadly 3d12, magical, reach 20 ft., unarmed), **Damage** 4d12+18 bludgeoning plus [[Improved Grab]] plus [[Improved Push]]"
  - name: "Melee strike"
    desc: "Foot +38 (`pf2:1`) (deadly 3d12, magical, reach 20 ft., unarmed), **Damage** 4d8+18 bludgeoning plus [[Improved Knockdown]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 37, attack +29<br>**6th** [[Truesight]] (Constant)<br>**3rd** [[Haste]] (Constant)"
abilities_bot:
  - name: "Annihilation Beams"
    desc: "`pf2:2` A guthallath releases two beams of destruction from its eyes. Each beam is a @Template[line|distance:120]. Everything in either line takes @Damage[13d10[untyped]|options:area-damage] damage with a DC 41 [[Fortitude]] save. <br>  <br> A creature reduced to 0 HP is reduced to a fine powder as the [[Disintegrate]] spell. There is no additional effect on creatures in any area where the beams overlap. <br>  <br> The guthallath can't use this ability again for 1d4 rounds."
  - name: "Deadly Throw"
    desc: "`pf2:1` **Requirements** The guthallath has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The guthallath throws the creature into the air, 100 feet high and 50 feet away. If the flung creature lands on another creature, the creature it lands on takes the same amount of bludgeoning damage. <br>  <br> The creature being landed on can attempt a DC 41 [[Reflex]] save."
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, foot, DC 45 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A guthallath is an enormous construct created long ago, probably as a war machine, by a long-forgotten empire. Nearly 100 feet tall, this massive stone statue typically resembles a stalwart warrior wearing only a loincloth and skullcap. Few have seen the entire body of a guthallath, though; most of the time, the relic is buried up to its neck, covered in moss, and stranded in a forgotten place. Yet every so often, one of these harbingers of destruction reactivates in response to some unknown stimulus or rallying call, and when this happens, woe to any who stand in its way.

While a guthallath's ancient enemies are likely gone, it's still an engine of pure destruction, designed to rampage for weeks, even months. It's not intelligent enough to enjoy or regret its acts and cannot be reasoned with—it's also unaffected by most magic and unpredictable in how it selects its targets (and the creatures it spares).

```statblock
creature: "Guthallath"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
