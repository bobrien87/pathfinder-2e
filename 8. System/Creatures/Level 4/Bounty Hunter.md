---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bounty Hunter"
level: "4"
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
    desc: "+13"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +9, Deception +10, Diplomacy +8, Intimidation +8, Stealth +12, Survival +9"
abilityMods: ["+3", "+4", "+1", "+0", "+3", "+0"]
abilities_top:
  - name: "Posse's Edge"
    desc: "The bounty hunter and their allies gain a +1 circumstance bonus on initiative rolls if the opposing side includes their hunted prey. <br>  <br> > [!danger] Effect: Posse's Edge"
  - name: "Precision Edge"
    desc: "The first time the bounty hunter hits their hunted prey in a round, they deal an additional 1d8 precision damage."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +12, **Will** +11"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Falchion +13 (`pf2:1`) (forceful, sweep), **Damage** 1d10+6 slashing"
  - name: "Ranged strike"
    desc: "Crossbow +14 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Hunt Prey"
    desc: "`pf2:1` The bounty hunter designates a single creature they can see and hear, or one they're Tracking or Gathering Information about, as their prey. The bounty hunter gains a +2 circumstance bonus to Perception checks to [[Seek]] the prey, to Survival checks to [[Track]] the prey, and to Diplomacy checks to [[Gather Information]] about the prey. This effect lasts until they use Hunt Prey again."
  - name: "Running Reload"
    desc: "`pf2:1` The bounty hunter Strides, Steps, or Sneaks, and then Interacts to reload."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Bounty hunters are constantly on the move, whether within city walls or the wilderness, trailing their fugitive quarries for capture... or disposal. Often relying on stealth or deception as much as martial skill, bounty hunters employ a vast array of talents to accomplish their goals and collect the hefty payout.

Whether they're hired to wage war, protect a caravan, or infiltrate an impenetrable fortress, there's ample work for mercenaries all over Golarion.

```statblock
creature: "Bounty Hunter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
