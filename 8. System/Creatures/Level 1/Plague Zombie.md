---
type: creature
group: ["Mindless", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Plague Zombie"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Zombie"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +9"
abilityMods: ["+4", "-2", "+3", "-5", "+0", "-2"]
abilities_top:
  - name: "Slow"
    desc: "A zombie is permanently [[Slowed]] 1 and can't use reactions."
  - name: "Zombie Rot"
    desc: "An infected creature can't heal damage it takes from zombie rot until it has been cured of the disease. <br>  <br> **Saving Throw** DC 18 [[Fortitude]] save <br>  <br> **Stage 1** carrier with no ill effect (1 day) <br>  <br> **Stage 2** 1d6 void damage (1 day) <br>  <br> **Stage 3** 1d6 void damage (1 day) <br>  <br> **Stage 4** 1d6 void damage (1 day) <br>  <br> **Stage 5** dead, rising as a plague zombie immediately"
armorclass:
  - name: AC
    desc: "13; **Fort** +6, **Ref** +3, **Will** +4"
health:
  - name: HP
    desc: "50; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Weaknesses** vitality 10, slashing 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (unarmed), **Damage** 1d8+4 bludgeoning plus [[Grab]] plus [[Zombie Rot]]"
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (unarmed), **Damage** 1d12+4 piercing plus [[Zombie Rot]]"
spellcasting: []
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Plague zombies are infested with horrible contagions.

A zombie's only desire is to consume the living. Unthinking and ever-shambling harbingers of death, zombies stop only when they're destroyed.

```statblock
creature: "Plague Zombie"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
