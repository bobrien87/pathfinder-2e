---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Crawling Hand"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Lifesense]] (precise) 30 feet, [[Tremorsense]] (imprecise) 30 feet"
languages: "Common ((can't speak any language))"
skills:
  - name: Skills
    desc: "Athletics +13, Stealth +11, Survival +12"
abilityMods: ["+4", "+2", "+4", "-4", "+3", "+0"]
abilities_top:
  - name: "Mark Quarry"
    desc: "A crawling hand can be assigned a quarry by anointing the hand with a drop of the intended quarry's blood. If the hand ever has no quarry, it automatically gains the next creature it damages as its quarry. The hand gains a +1 circumstance bonus to Perception checks when it [[Seeks]] its quarry, to Survival checks when it [[Tracks]] its quarry, and damage rolls when it Strikes its quarry."
armorclass:
  - name: AC
    desc: "22; **Fort** +13, **Ref** +11, **Will** +10"
health:
  - name: HP
    desc: "75; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, visual, bleed"
abilities_mid:
  - name: "Pus Burst"
    desc: "`pf2:r` **Trigger** The giant crawling hand takes piercing or slashing damage <br>  <br> **Effect** A random creature adjacent to the giant crawling hand is sprayed with vile pus that deals 4d6 void damage. The affected creature must attempt a DC 21 [[Reflex]] save. <br> - **Critical Success** The creature takes no damage. <br> - **Success** The creature takes half damage and becomes [[Sickened]] 1. <br> - **Failure** The creature takes full damage and becomes [[Sickened]] 2. <br> - **Critical Failure** The creature takes double damage and becomes [[Sickened]] 3."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +15 (`pf2:1`) (unarmed), **Damage** 2d6+7 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A giant crawling hand is the appendage of a very large creature, such as a giant.

Typically, crawling hands are formed when severed appendages are endowed with a crude sentience by evil necromantic energies that turn them into tireless killers. Yet crawling hands can also arise spontaneously, usually when a creature loses an appendage in a place rife with necromantic energy or with a connection to the Void.

```statblock
creature: "Giant Crawling Hand"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
