---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Crawling Hand"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Lifesense]] (precise) 30 feet, [[Tremorsense]] (imprecise) 30 feet"
languages: "Common ((can't speak any language))"
skills:
  - name: Skills
    desc: "Athletics +5, Stealth +6, Survival +2"
abilityMods: ["+1", "+3", "+0", "-4", "+0", "+0"]
abilities_top:
  - name: "Mark Quarry"
    desc: "A crawling hand can be assigned a quarry by anointing the hand with a drop of the intended quarry's blood. If the hand ever has no quarry, it automatically gains the next creature it damages as its quarry. The hand gains a +1 circumstance bonus to Perception checks when it [[Seeks]] its quarry, to Survival checks when it [[Tracks]] its quarry, and damage rolls when it Strikes its quarry."
armorclass:
  - name: AC
    desc: "12; **Fort** +2, **Ref** +5, **Will** +2"
health:
  - name: HP
    desc: "8; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, visual, bleed"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +7 (`pf2:1`) (agile, finesse, reach 0 ft., unarmed), **Damage** 1d4+1 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Throat Grab"
    desc: "`pf2:1` This ability functions as Grab, but the crawling hand grips the throat of a Medium or smaller creature. A creature [[Grabbed]] or [[Restrained]] this way has difficulty speaking and must spend an extra action to perform any action that requires speaking, including casting spells. <br>  <br> **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A crawling hand formed from the appendage of a Medium creature is quick and agile, skittering in the shadows until it can strike its prey.

Typically, crawling hands form when severed appendages are endowed with a crude sentience by necromantic energies that turn them into tireless killers. Yet, crawling hands can also arise spontaneously, usually when a creature loses an appendage in a place rife with necromantic energy or with a connection to the Void.

```statblock
creature: "Crawling Hand"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
