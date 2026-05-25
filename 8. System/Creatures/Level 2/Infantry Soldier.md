---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Infantry Soldier"
level: "2"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +10, Intimidation +7, Warfare Lore +6"
abilityMods: ["+4", "+0", "+3", "+0", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18 (20 with shield raised); **Fort** +9, **Ref** +6, **Will** +6"
health:
  - name: HP
    desc: "28"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +10 (`pf2:1`) (agile, versatile s), **Damage** 1d6+6 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +6 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Guardian Shield"
    desc: "`pf2:1` The infantry soldier Raises their Shield, but grants the benefit to an adjacent ally and can Shield Block for that ally. Guardian Shield ends early if at any point the ally is no longer adjacent."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Though low on the military hierarchy, infantry are still highly disciplined warriors, challenging for any ordinary person to face in combat.

A military serves to defend and fight on behalf of nations and can be trained and deployed in various ways.

```statblock
creature: "Infantry Soldier"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
