---
type: creature
group: ["Catfolk", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lucky Courser"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Catfolk"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: "Amurrun, Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +16, Athletics +14, Deception +14, Nature +16, Stealth +18, Survival +16, Lore about a magical creature type +16"
abilityMods: ["+2", "+4", "+3", "+1", "+2", "+2"]
abilities_top:
  - name: "Elusive Hunter"
    desc: "The lucky courser can `act hide` and `act sneak` in any natural terrain and in lesser cover from allies."
armorclass:
  - name: AC
    desc: "27; **Fort** +17, **Ref** +18, **Will** +14"
health:
  - name: HP
    desc: "140"
abilities_mid:
  - name: "Warning Ears"
    desc: "`pf2:0` **Trigger** The lucky courser rolls initiative using Perception or Survival <br>  <br> **Effect** Their expressive ears twitch in alarm, granting allies within 10 feet a +2 circumstance bonus to initiative rolls."
  - name: "Guide to Fortune"
    desc: "`pf2:r` **Frequency** once per hour <br>  <br> **Trigger** The lucky courser or an ally within 10 feet fails a Reflex save, Acrobatics check, or Athletics check <br>  <br> **Effect** The triggering creature rerolls the save or check and uses the better result."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Whip +20 (`pf2:1`) (disarm, finesse, nonlethal, reach, trip), **Damage** 1d4+12 slashing"
  - name: "Melee strike"
    desc: "Claw +19 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4+12 slashing"
  - name: "Ranged strike"
    desc: "Arbalest +20 (`pf2:1`) (backstabber, magical, reload 1, range 110 ft.), **Damage** 2d10+6 piercing plus [[Cold Iron Bolts]] plus [[Dawnsilver Bolts]]"
spellcasting: []
abilities_bot:
  - name: "Feline Skirmish"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The lucky courser can Interact to reload their arbalest, Step, and Strike, taking the actions in any order. The Step ignores difficult terrain."
  - name: "Head Shot"
    desc: "`pf2:2` The lucky courser Creates a Diversion and then Strikes. The target is [[Dazzled]] until the end of the lucky courser's next turn on a successful Strike (or [[Blinded]] on a critical hit)."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Masterful catfolk hunters travel the far corners of the world, stalking terrible the monsters who dwell there in hopes of someday putting an end to their predations. They eagerly cooperate with other adventurers to defeat demons, aberrations, and malevolent beasts and fey.

Catfolk can be found traveling almost anywhere, and they are quick to settle down for a chat when they encounter fellow travelers. Some trade stories, act as guides, or operate at the fringes of polite society.

```statblock
creature: "Lucky Courser"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
