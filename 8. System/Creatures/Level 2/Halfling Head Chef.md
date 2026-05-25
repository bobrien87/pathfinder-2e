---
type: creature
group: ["Halfling", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Halfling Head Chef"
level: "2"
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
    desc: "+7; [[Scent]] (imprecise) 30 feet"
languages: "Common, Halfling"
skills:
  - name: Skills
    desc: "Acrobatics +7, Intimidation +7, Society +6, Baking Lore +15, Cooking Lore +17"
abilityMods: ["+1", "+3", "+2", "+2", "+1", "+1"]
abilities_top:
  - name: "+15 to Smell and Taste"
    desc: ""
  - name: "Culinary Specialist"
    desc: "For encounters involving cooking and taste, the head chef is a 7th-level challenge."
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the [[Seek]] action to find [[Hidden]] or [[Undetected]] creatures within 30 feet of them. Whenever the halfling targets a creature that is [[Concealed]] or hidden from them, reduce the DC of the flat check to DC 3 flat check for a concealed target or DC 9 flat check for a hidden one."
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +7, **Will** +7"
health:
  - name: HP
    desc: "36"
abilities_mid:
  - name: "Dash of Spice"
    desc: "`pf2:r` **Trigger** The head chef is targeted with a melee attack by an adjacent attacker they can see <br>  <br> **Effect** The head chef uses Spice Mix against the attacker."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Filcher's Fork +9 (`pf2:1`) (agile, backstabber, deadly d6), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Filcher's Fork +9 (`pf2:1`) (agile, backstabber, deadly d6, thrown 20), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Hot Frying Pan +9 (`pf2:1`) (fatal d8), **Damage** 1d4+3 bludgeoning plus 1d4 fire"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Angry Rant"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The chef shouts a flurry of insults and criticisms at either an ally or enemy within 30 feet with the following effects: <br>  <br> **Ally** The chef's assistant is shaken by the barrage of criticism but is determined to work faster and harder. The target becomes [[Quickened]] for 1 round but is also [[Frightened]] 1. They can use the extra action to Interact, Step, or Stride, or as part of an action or activity to prepare, cook, or serve food. <br>  <br> **Enemy** The target must succeed a DC 18 [[Will]] save or take 1d6 mental damage and become frightened 1 (or 2d6 mental damage and [[Frightened]] 2 on a critical failure)."
  - name: "Spice Mix"
    desc: "`pf2:1` The head chef throws a mixture of irritating spices into an adjacent creature's eyes, causing the creature to be [[Dazzled]] until it Interacts to clear its vision."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Renowned for their culinary expertise, halfling head chefs navigate the complex world of high cuisine with flavorful creations and fiery tempers.

Halflings thrive on simple pleasures—having a pint at the pub or warming their feet by the hearth.

```statblock
creature: "Halfling Head Chef"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
