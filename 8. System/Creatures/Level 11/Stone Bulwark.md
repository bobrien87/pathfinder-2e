---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Stone Bulwark"
level: "11"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +26"
abilityMods: ["+7", "-1", "+4", "-5", "+0", "-5"]
abilities_top:
  - name: "Binding Stone"
    desc: "Any creature hit by the stone bulwark's fist or rock Strike is affected by a DC 30 [[Fortitude]] save [[Earthbind]] spell."
armorclass:
  - name: AC
    desc: "30; **Fort** +24, **Ref** +18, **Will** +19"
health:
  - name: HP
    desc: "175; **Resistances** physical 10 except adamantine, spells 10 except cold, earth, water"
abilities_mid:
  - name: "Statuary Aura"
    desc: "20 feet. <br>  <br> Rocks of marble magically arise from the ground in the aura. They protect the bulwark's allies, giving each of them standard  <br>  <br> > [!danger] Effect: Cover <br>  <br> . These stones can be used for Throw Rock. <br>  <br> This aura automatically activates at the start of the stone bulwark's first turn in combat and deactivates at the end of combat."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 2d10+13 bludgeoning plus [[Binding Stone]]"
  - name: "Ranged strike"
    desc: "Rock +22 (`pf2:1`) (brutal, magical, range 120 ft.), **Damage** 2d6+11 bludgeoning plus [[Binding Stone]]"
spellcasting: []
abilities_bot:
  - name: "Inexorable March"
    desc: "`pf2:1` The stone bulwark Strides up to its Speed, pushing back each creature whose space it moves into and damaging them if they try to stop its movement. A creature can attempt to bar the way by succeeding at a DC 34 [[Fortitude]] save. On a critical success, the resisting creature takes no damage; otherwise it is damaged as if hit by the construct's fist."
  - name: "Throw Rock"
    desc: "`pf2:1` The monster picks up a rock within reach or retrieves a stowed rock and throws it, making a ranged Strike."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Stone bulwarks are slow and steady constructs typically carved from marble or granite. They're often made to serve as works of art when at rest, so some magical crafters employ master sculptors to ensure their constructs make beautiful statues. Older stone bulwarks might be weathered, with scuffed or cracked surfaces or missing noses and digits, but this weathering is largely cosmetic and doesn't adversely impact the bulwark's functionality.

```statblock
creature: "Stone Bulwark"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
