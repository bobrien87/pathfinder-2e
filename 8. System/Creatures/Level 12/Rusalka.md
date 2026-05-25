---
type: creature
group: ["Aquatic", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rusalka"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aquatic"
trait_02: "Fey"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Low-Light Vision]]"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +21, Athletics +24, Deception +25, Diplomacy +21, Nature +21, Performance +23, Stealth +25"
abilityMods: ["+4", "+5", "+3", "+1", "+3", "+7"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Entangling Tresses"
    desc: "A rusalka can have up to eight creatures grabbed within their tresses at a time."
armorclass:
  - name: AC
    desc: "33; **Fort** +21, **Ref** +25, **Will** +21"
health:
  - name: HP
    desc: "230; **Weaknesses** cold iron 15; **Resistances** fire 10"
abilities_mid:
  - name: "Blurred Form"
    desc: "A rusalka is [[Concealed]] while underwater."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tresses +24 (`pf2:1`) (agile, finesse, reach 15 ft.), **Damage** 3d8+10 bludgeoning plus [[Improved Grab]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 35, attack +27<br>**5th** [[Control Water]] (At Will)<br>**2nd** [[Invisibility]] (At Will), [[Mist]] (At Will), [[Water Walk]] (Constant)<br>**1st** [[Charm]] (At Will)"
abilities_bot:
  - name: "Beckoning Call"
    desc: "`pf2:1` The rusalka cries out a compelling invitation. Each non-fey creature within a @Template[type:emanation|distance:300] must attempt a DC 29 [[Will]] save. The effect lasts for 1 round, but if the rusalka uses Beckoning Call again on subsequent rounds, the duration extends by 1 round for all affected creatures. Once a creature succeeds at any save against Beckoning Call, that creature is temporarily immune for 24 hours. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature is [[Fascinated]] and must spend each of its actions to move closer to the rusalka, avoiding obvious dangers. If a beckoned creature is adjacent to the rusalka, it stays still and doesn't act. If attacked by the rusalka, the creature is freed from captivation at the end of the rusalka's turn. <br> - **Critical Failure** As failure, but if attacked by the rusalka, the creature can attempt a new save only at the start of its next turn, rather than being freed at the end of the rusalka's turn."
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d8+10)[bludgeoning]], DC 32 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Flowing Hair"
    desc: "`pf2:1` The rusalka attempts an [[Athletics]] check against the Fortitude DC of each creature they have [[Grabbed]] or [[Restrained]] by their tresses. The rusalka moves each creature they succeed against up to 10 feet and each creature they critically succeed against up to 20 feet. This movement must all be within reach of its tresses."
  - name: "Shameful Touch"
    desc: "`pf2:1` The rusalka touches a creature within 5 feet using their hand, stirring up memories of regret and shame. The target must attempt a DC 35 [[Will]] save. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target is [[Sickened]] 1. <br> - **Failure** The creature is sickened 1 and [[Stunned]] 1. <br> - **Critical Failure** The creature is sickened 1, stunned 1, and it must use its first action on its next turn to Strike itself, automatically hitting."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These androgynous, river-dwelling fey delight in manipulating the emotions of those unfortunate enough to fall into their grasp, using humiliation to break victims' wills. Rusalkas enjoy keeping their broken toys nearby, both for continuing entertainment and to aid in their defense, as their captives' misery often drives them to become obsessively loyal to these fey. If a person ever escapes a rusalka's clutches, the rusalka will likely seek them out and shame them for "abandoning" their home, all in the hopes their victim regresses into a distressed mental state and returns to captivity.

```statblock
creature: "Rusalka"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
