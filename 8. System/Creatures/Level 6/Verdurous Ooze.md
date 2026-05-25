---
type: creature
group: ["Mindless", "Ooze"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Verdurous Ooze"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Mindless"
trait_02: "Ooze"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Motion Sense]] (precise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +15, Stealth +4"
abilityMods: ["+5", "-4", "+5", "-5", "+0", "-5"]
abilities_top:
  - name: "Motion Sense"
    desc: "A verdurous ooze can sense nearby creatures through vibration and air or water movement."
  - name: "Verdurous Ooze Acid"
    desc: "A verdurous ooze's acid damages only metal and flesh-not bone, stone, or other materials."
armorclass:
  - name: AC
    desc: "12; **Fort** +17, **Ref** +8, **Will** +10"
health:
  - name: HP
    desc: "157; **Immunities** acid, critical hits, piercing, precision, slashing, unconscious, visual"
abilities_mid:
  - name: "Corrosive Surface"
    desc: "A creature that hits a verdurous ooze with a metal weapon or unarmed attack must attempt a DC 21 [[Reflex]] save. On a failure, the weapon or creature takes 2d4 acid damage (after dealing damage to the ooze as normal). Thrown weapons take this damage automatically with no save."
  - name: "Enliven Foliage"
    desc: "20 feet. The verdurous ooze constantly emits supernatural vapors that cause nearby plants to grow rapidly and writhe and grasp at anything and everything within the emanation. This area becomes difficult terrain for non-verdurous ooze creatures. When a creature starts its turn in this aura, it must succeed at a DC 21 [[Reflex]] save or take a –10-foot circumstance penalty to its Speeds until it leaves the emanation. <br>  <br> > [!danger] Effect: Enliven Foliage"
  - name: "Split"
    desc: "When a verdurous ooze that has 10 or more HP is hit by an attack that would deal piercing or slashing damage, it splits into two identical oozes, each with half the original's HP. One ooze is in the same space as the original, and the other is in an adjacent, unoccupied space. If no adjacent space is unoccupied, it automatically pushes creatures and objects out of the way to fill a space (the GM decides if an object or creature is too big or heavy to push)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pseudopod +15 (`pf2:1`) (unarmed), **Damage** 2d6+7 bludgeoning plus 1d6 acid plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[2d6[bludgeoning],1d6[acid]]{2d6 bludgeoning plus 1d6 acid}, DC 24 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Sleep Gas"
    desc: "`pf2:2` The verdurous ooze adjusts its aura of supernatural vapors to affect living creatures within a @Template[emanation|distance:20], forcing them to attempt a DC 24 [[Will]] save. <br> - **Critical Success** The creature is unaffected and becomes temporarily immune to Sleep Gas for 24 hours. <br> - **Success** The creature is [[Stupefied 1]] for 1 round. <br> - **Failure** The creature falls [[Unconscious]]. If it's still unconscious after 1 minute, it wakes up automatically. <br> - **Critical Failure** The creature falls [[Unconscious]]. If it's still unconscious after 1 hour, it wakes up automatically."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Verdurous oozes are found in temperate forests, warm jungles, or other places where plant life grows in abundance. Unlike many types of oozes, verdurous oozes are not particularly good climbers and have been known to get trapped in natural or artificial chasms. Warlords and wizards sometimes make use of that fact and keep verdurous oozes as guardians in pits around the walls of their fortresses or towers.

```statblock
creature: "Verdurous Ooze"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
