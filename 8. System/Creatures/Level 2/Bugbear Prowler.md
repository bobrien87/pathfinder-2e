---
type: creature
group: ["Bugbear", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bugbear Prowler"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Bugbear"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +7, Intimidation +4, Stealth +6"
abilityMods: ["+4", "+2", "+3", "-1", "+1", "+0"]
abilities_top:
  - name: "Mauler"
    desc: "The bugbear prowler gains a +3 circumstance bonus to damage rolls against creatures they have [[Grabbed]]."
armorclass:
  - name: AC
    desc: "17; **Fort** +9, **Ref** +8, **Will** +5"
health:
  - name: HP
    desc: "34"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bastard Sword +10 (`pf2:1`) (two hand d12), **Damage** 1d8+4 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Javelin +8 (`pf2:1`) (thrown 30), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Bushwhack"
    desc: "`pf2:1` The bugbear prowler Strides up to 10 feet and attempts to [[Grapple]] a creature they're [[Undetected]] by. If they succeed, they also deal fist damage to that creature."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Bugbear prowlers specialize in the art of lurking in the shadows.

These stealthy and cruel goblinoid creatures delight in spreading fear and tormenting their victims. Bugbears are the monsters lurking in the closet and hiding under the bed. Preying on remote farmsteads, bugbears reveal their presence with thumps in the night or creaks of boards to build lurking dread and arouse suspicion and fear.

```statblock
creature: "Bugbear Prowler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
