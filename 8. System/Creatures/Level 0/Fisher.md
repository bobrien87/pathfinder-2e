---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fisher"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +7, Nature +4, Survival +4, Fishing Lore +8, Sailing Lore +6"
abilityMods: ["+3", "+2", "+1", "+0", "+2", "+0"]
abilities_top:
  - name: "+2 Bonus on Perception to Spot Fish"
    desc: ""
  - name: "Fishhooked"
    desc: "While it has persistent bleed damage from the fisher's fishing line Strike, a creature has a fishhook embedded in it. The creature can't move farther away from the fisher (though it can move laterally). The fisher can reel the creature in as a single action with the attack and manipulate trait, attempting an [[Athletics]] check against the creature's Fortitude DC. On a success, the creature takes 2d4 slashing damage and is pulled 10 feet closer to the fisher (double the damage and distance on a critical success)."
armorclass:
  - name: AC
    desc: "14; **Fort** +7, **Ref** +6, **Will** +4"
health:
  - name: HP
    desc: "15"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spear +7 (`pf2:1`), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Spear +6 (`pf2:1`) (thrown 20), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Fishing Line +6 (`pf2:1`) (range 20 ft.), **Damage** 1 bleed plus 1 piercing plus [[Fishhooked]]"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

More than just hobbyists, fishers catch fish and other seafood with the intention of selling most of or all of their catch.

Society is built upon the backs of laborers.

```statblock
creature: "Fisher"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
