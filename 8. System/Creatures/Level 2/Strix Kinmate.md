---
type: creature
group: ["Humanoid", "Strix"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Strix Kinmate"
level: "2"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Strix"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Low-Light Vision]]"
languages: "Common, Strix"
skills:
  - name: Skills
    desc: "Acrobatics +8, Nature +7, Survival +9"
abilityMods: ["+8", "+4", "+0", "+0", "+3", "+0"]
abilities_top:
  - name: "Strix Camaraderie"
    desc: "Strix kinmates are tightly bonded to one another, adept at teamwork and supporting each other's attacks. If an enemy is within reach of both the kinmate and one other strix, that enemy is [[Off Guard]] to all strix."
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "25"
abilities_mid:
  - name: "Strix Vengeance"
    desc: "`pf2:0` **Frequency** once per 10 minutes <br>  <br> **Trigger** The kinmate or a strix ally they can see is damaged by an enemy's critical hit <br>  <br> **Effect** Until the end of their next turn, the kinmate gains a +`r {1d6}` status bonus to damage rolls on Strikes they make against the triggering enemy."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+4 piercing"
  - name: "Melee strike"
    desc: "Talon +10 (`pf2:1`) (agile, finesse), **Damage** 1d6+4 slashing"
  - name: "Ranged strike"
    desc: "Shortbow +10 (`pf2:1`) (deadly d10, range 60 ft.), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Kinmates carry a strong bond for one another and excel at teamwork.

Strix, called itarii in their own language, are avian humanoids with sprawling, dark-feathered wings and large talons. They possess angular features and piercing eyes that are fixed facing forward.

```statblock
creature: "Strix Kinmate"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
