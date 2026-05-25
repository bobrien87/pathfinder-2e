---
type: creature
group: ["Incorporeal", "Shadow"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Betobeto-San"
level: "12"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Shadow"
trait_03: "Spirit"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Greater Darkvision]]"
languages: "Common, Shadowtongue"
skills:
  - name: Skills
    desc: "Deception +23, Intimidation +23, Stealth +27"
abilityMods: ["+4", "+7", "+5", "+4", "+4", "+5"]
abilities_top:
  - name: "Fearsense (Precise) 60 feet"
    desc: "The betobeto-san is aware of all [[Frightened]] creatures within the listed range."
armorclass:
  - name: AC
    desc: "33; **Fort** +19, **Ref** +25, **Will** +22"
health:
  - name: HP
    desc: "170; **Immunities** disease, paralyzed, poison, precision; **Resistances** all damage 10 except force, ghost touch, vitality"
abilities_mid:
  - name: "Ominous Footsteps"
    desc: "60 feet. The betobeto-san's footsteps seem to draw ever closer, yet the source remains difficult to pinpoint. Each creature that starts its turn within 60 feet of the betobeto-san must attempt a DC 29 [[Will]] save. <br> - **Critical Success** The creature is unaffected and is temporarily immune for 1 minute. <br> - **Success** The creature becomes [[Frightened]] 1. <br> - **Failure** The creature becomes [[Frightened]] 2. <br> - **Critical Failure** The creature becomes [[Frightened]] 4."
  - name: "Shadow Invisibility"
    desc: "The betobeto-san is [[Invisible]] unless within an area of bright light."
  - name: "Shadow Step"
    desc: "`pf2:r` **Trigger** A bright light source reveals the betobeto-san. <br>  <br> **Requirements** The betobeto-san isn't already within an area of bright light. <br>  <br> **Effect** The betobeto-san Steps briefly into the Shadow Plane and then back again, appearing up to 30 feet away from where they began."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +25 (`pf2:1`) (agile, finesse, magical, unarmed), **Damage** 3d12+10 void"
spellcasting: []
abilities_bot:
  - name: "Stepping Decoy"
    desc: "`pf2:1` The betobeto-san Steps. They then create two illusory decoys of sound within @Template[emanation|distance:15]{15 feet} of them that mimic the sounds of their ominous footsteps. <br>  <br> These decoys act independently on the betobeto-san's initiative with 2 actions apiece. They can only Sneak or Stride, and they have a Speed of 35 feet. Use the betobeto-san's Stealth DC (typically 37) against attempts to [[Seek]] or disbelieve a decoy. <br>  <br> Each decoy lasts for 1 minute. Any existing decoys vanish if the betobeto-san uses this ability again."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A betobeto-san wanders the highways and byways of the Material Plane, searching for unwilling traveling companions to sustain the spirit's appetite for fear. Though this shadow spirit is invisible in darkness or shade, in light they appear as a formless, shadowy mass with two sandaled feet. These sandals are made of wood or bone that cause the creature's footsteps to make the distinct "beto beto" sound from which they receive their name. A wide, toothy mouth smiles in the middle of their otherwise featureless mass, and they can manifest long, clawed limbs.

Betobeto-san trail behind nighttime travelers, compelled to follow until the creatures verbally offer to let the betobeto-san pass. This compulsion isn't usually malicious by nature and occurs more from a betobeto-san's misguided desire for company and courtesy; unfortunately, they lack of understanding how this behavior can frighten others. Betobeto-san don't attack those they follow, but they often end up in combat because their unwelcome behavior causes those they follow to attack first.

```statblock
creature: "Betobeto-San"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
