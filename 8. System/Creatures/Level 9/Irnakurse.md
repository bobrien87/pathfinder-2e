---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Irnakurse"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "Chthonian, Elven, Sakvroth ((Can't Speak Any Language))"
skills:
  - name: Skills
    desc: "Acrobatics +20, Athletics +20, Stealth +20"
abilityMods: ["+5", "+5", "+3", "-2", "+3", "+4"]
abilities_top:
  - name: "Mind Lash"
    desc: "A creature hit by an irnakurse's tentacle is overwhelmed with corrupted images of a ruined life and must succeed at a DC 28 [[Will]] save or be [[Stunned]] 2 (or [[Stunned]] 4 on a critical failure). After attempting this save, the creature is temporarily immune to mind lash for 24 hours."
armorclass:
  - name: AC
    desc: "28; **Fort** +20, **Ref** +18, **Will** +16"
health:
  - name: HP
    desc: "152"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d12+11 piercing"
  - name: "Melee strike"
    desc: "Tentacle +20 (`pf2:1`) (agile, reach 20 ft., unarmed), **Damage** 2d8+11 slashing plus [[Mind Lash]]"
spellcasting: []
abilities_bot:
  - name: "Soul Scream"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The irnakurse unleashes an alien shriek of nightmarish horror and pain. All non-aberration creatures within a @Template[emanation|distance:10] must attempt a DC 28 [[Will]] save. <br>  <br> The irnakurse can Sustain Soul Scream for up to 6 rounds; each time it does, it repeats the effect without a new save. <br> - **Critical Success** The creature is unaffected, and it's temporarily immune to Soul Scream for 24 hours. <br> - **Success** The creature is [[Stupefied 1]] for 1 round. <br> - **Failure** The creature is stupefied 1. Further failed saves against Soul Scream increase the stupefied value by 1, to a maximum of [[Stupefied 4]]. Each time the character gets a full night's rest, the stupefied condition gained from Soul Scream decreases by 1. <br> - **Critical Failure** As failure, except the stupefied value increases by 2 instead of by 1."
  - name: "Storm of Tentacles"
    desc: "`pf2:2` The irnakurse makes up to four tentacle Strikes, each against a different target. These attacks count toward the irnakurse's multiple attack penalty, but the multiple attack penalty doesn't increase until after it makes all of its attacks."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Irnakurse are believed to be elves who have been subjected to particularly cruel and humiliating fleshwarping practices, though they are so corrupted by their transformation it is nearly impossible to tell. The process of crafting an irnakurse twists the unfortunate elf into a mass of misplaced limbs, loose flesh, and bony protrusions—parts that should be internal are often left on full display to the world. These beings periodically crawl to the surface from the deepest reaches of the Darklands, leading some elven scholars to the gruesome suspicion that these are remnants of the elves who traveled underground in order to escape Earthfall.

Magical mishaps, divine curses, and untested technology are all capable of wreaking drastic transformations on the body, and are all rampant on the world of Golarion and beyond. Creatures that have undergone changes so drastic they no longer can be considered the same ancestry as they were before are known as fleshwarps. These beings are rare, and their unsettling appearance often provokes horrified responses from other people.

Some creatures revel in the total degradation of their defeated foes through fleshwarping. Though the technique was originally taught to mortals by the demon lord Haagenti, mortals have spent eons modifying and perfecting the method. Fleshcrafters torture their enemies in vats of churning magical reagents, reshaping their flesh and psyche alike into horrid and monstrous things.

```statblock
creature: "Irnakurse"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
