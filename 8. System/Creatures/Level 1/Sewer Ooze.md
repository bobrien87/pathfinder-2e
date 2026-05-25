---
type: creature
group: ["Mindless", "Ooze"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sewer Ooze"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Mindless"
trait_02: "Ooze"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3; [[Motion Sense]] (precise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Stealth +1"
abilityMods: ["+2", "-5", "+4", "-5", "+0", "-5"]
abilities_top:
  - name: "Motion Sense 60 feet"
    desc: "A sewer ooze can sense nearby motion through vibration and air movement."
armorclass:
  - name: AC
    desc: "8; **Fort** +9, **Ref** +1, **Will** +3"
health:
  - name: HP
    desc: "40; **Immunities** acid, critical hits, precision, unconscious, visual, bleed"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pseudopod +9 (`pf2:1`) (unarmed), **Damage** 1d6+1 bludgeoning plus 1d4 acid"
spellcasting: []
abilities_bot:
  - name: "Filth Wave"
    desc: "`pf2:1` **Frequency** once per minute <br>  <br> **Effect** The sewer ooze unleashes a wave of filth, covering all creatures in a @Template[emanation|distance:20]. Each creature in the area must succeed at a DC 17 [[Reflex]] save or take @Damage[1d4[acid]|options:area-damage] damage and take a –10-foot penalty to its Speeds for 1 minute (on a critical failure, the creature also falls [[Prone]]). <br>  <br> A creature can spend an Interact action to clean someone off, decreasing the Speed penalty by 5 feet with each action. <br>  <br> > [!danger] Effect: Filth Wave"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These amorphous masses of sewage and other detritus make their way through filthy culverts beneath cities large and small.

Slimes, molds, and other oozes can be found in dank dungeons and shadowed forests. While not necessarily evil, some grow to enormous sizes and have insatiable appetites.

```statblock
creature: "Sewer Ooze"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
