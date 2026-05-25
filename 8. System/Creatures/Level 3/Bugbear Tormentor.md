---
type: creature
group: ["Bugbear", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bugbear Tormentor"
level: "3"
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
    desc: "+8; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +9, Intimidation +7, Stealth +8, Thievery +8"
abilityMods: ["+4", "+3", "+2", "-1", "+1", "+0"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The bugbear tormentor deals 1d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "20; **Fort** +9, **Ref** +10, **Will** +6"
health:
  - name: HP
    desc: "44"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +11 (`pf2:1`) (agile, versatile s), **Damage** 1d4+6 piercing"
  - name: "Melee strike"
    desc: "Sickle +11 (`pf2:1`) (agile, trip), **Damage** 1d4+6 slashing"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Twin Feint"
    desc: "`pf2:2` The bugbear tormentor makes a dazzling series of attacks with two weapons, using the first attack to throw their foe off-guard against a second attack at a different angle. They make one Strike with each of their two melee weapons, both against the same target. The target is automatically [[Off Guard]] against the second attack. The bugbear tormentor applies their multiple attack penalty to these Strikes normally."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The bugbear tormentor seeks to torture their prey as much through psychological intimidation as through physical harm. The longer a bugbear tormentor can keep their victim alive and terrified, the better they feel.

These stealthy and cruel goblinoid creatures delight in spreading fear and tormenting their victims. Bugbears are the monsters lurking in the closet and hiding under the bed. Preying on remote farmsteads, bugbears reveal their presence with thumps in the night or creaks of boards to build lurking dread and arouse suspicion and fear.

```statblock
creature: "Bugbear Tormentor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
