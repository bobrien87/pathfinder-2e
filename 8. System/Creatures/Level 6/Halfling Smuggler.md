---
type: creature
group: ["Halfling", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Halfling Smuggler"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Halfling"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13"
languages: "Common, Halfling"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +11, Deception +14, Intimidation +14, Society +10, Stealth +15, Thievery +16, Underworld Lore +14"
abilityMods: ["+3", "+4", "+2", "+0", "+1", "+2"]
abilities_top:
  - name: "Grease Some Palms"
    desc: "A smuggler is adept at navigating official channels and makes network contacts in order to keep their goods moving. They gain a +2 circumstance bonus to [[Make an Impression]] and [[Request]] with members of the local bureaucracy."
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the [[Seek]] action to find [[Hidden]] or [[Undetected]] creatures within 30 feet of them. Whenever the halfling targets a creature that is [[Concealed]] or hidden from them, reduce the DC of the flat check to DC 3 flat check for a concealed target or DC 9 flat check for a hidden one."
  - name: "Sneak Attack"
    desc: "The smuggler deals an extra 2d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +16, **Will** +13"
health:
  - name: HP
    desc: "95"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Filcher's Fork +17 (`pf2:1`) (agile, backstabber, deadly d6, finesse, magical), **Damage** 1d4+9 piercing"
  - name: "Melee strike"
    desc: "Filcher's Fork +17 (`pf2:1`) (agile, backstabber, deadly d6, magical, thrown 20), **Damage** 1d4+9 piercing"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+9 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +16 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d4+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Distracting Escape"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** Smugglers succeed by making a move only after they've diverted others' attention. The smuggler Creates a Diversion. If the smuggler became [[Hidden]] to at least one creature, the smuggler can then [[Sneak]]."
  - name: "Hidden Pockets"
    desc: "`pf2:0` **Frequency** once per round <br>  <br> **Effect** The smuggler Interacts to draw an item of light Bulk concealed in one of their hidden pockets. The pockets can store up to four objects of light Bulk. For most smugglers, these items are [[Arsenic]], an [[Elixir of Life (Lesser)]], a [[Smoke Ball (Lesser)]], and a [[Thieves' Toolkit]]. The smuggler can refill the pockets over the course of 1 minute."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Halfling smugglers are sought out for their ability to deftly navigate the shadowy underworld to move illicit goods and information.

Halflings thrive on simple pleasures—having a pint at the pub or warming their feet by the hearth.

```statblock
creature: "Halfling Smuggler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
