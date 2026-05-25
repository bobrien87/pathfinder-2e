---
type: creature
group: ["Amphibious", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sedacthy Scout"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Humanoid"
trait_03: "Sedacthy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]], [[Wavesense]] (imprecise) 30 feet"
languages: "Thalassic (Sea Speech)"
skills:
  - name: Skills
    desc: "Athletics +8, Intimidation +9, Stealth +8, Survival +7"
abilityMods: ["+4", "+4", "+1", "+0", "+1", "+3"]
abilities_top:
  - name: "Sea Speech"
    desc: "A sedacthy speaking Thalassic can be understood by any animal that has a swim Speed or the amphibious or aquatic trait. By spending a week regularly interacting with such an animal, the sedacthy can make it permanently helpful."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (unarmed), **Damage** 1d4 bleed plus 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Claw +10 (`pf2:1`) (agile, unarmed), **Damage** 1d6+4 slashing"
  - name: "Melee strike"
    desc: "Spear +10 (`pf2:1`), **Damage** 1d6+6 piercing"
  - name: "Melee strike"
    desc: "Spear +10 (`pf2:1`) (thrown 20), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Shared Feast"
    desc: "`pf2:2` The sedacthy makes a jaws Strike. If it hits, an ally of their choice can spend a reaction to make a jaws Strike against the same target. Allies with beaks or similar attacks can use those instead of jaws."
  - name: "Wriggling Rush"
    desc: "`pf2:1` **Frequency** once per round; <br>  <br> **Effect** The scout takes a Stride action and a Swim action, in either order. They ignore difficult terrain from mud, quicksand, and similar terrain during this movement."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Scouts, usually young sedacthies, ply the ocean in search of animal servants or tread ashore to hunt. Scouts hunting on the surface press crocodiles and snakes into service, while those underwater prefer electric eels and hippocampi.

Sedacthies are amphibious, fish-like humanoids who lurk in Golarion's oceans and are known for leading their animal servants ashore to devour air breathers. When an entire fishing village disappears overnight, sedacthies are the first suspects. Sedacthies pride themselves as natural leaders, with ambition limited only by their strict adherence to hierarchy. A sedacthy's station is determined by the strength of the animal servants they press into service, and the mettle they prove during hunts and in battles against outsiders.

```statblock
creature: "Sedacthy Scout"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
