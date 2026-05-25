---
type: creature
group: ["Amphibious", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sedacthy Speaker"
level: "6"
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
    desc: "+15; [[Darkvision]], [[Wavesense]] (imprecise) 30 feet"
languages: "Thalassic (Sea Speech)"
skills:
  - name: Skills
    desc: "Athletics +16, Crafting +14, Diplomacy +13, Intimidation +15, Nature +15"
abilityMods: ["+6", "+3", "+4", "+2", "+3", "+5"]
abilities_top:
  - name: "Sea Speech"
    desc: "A sedacthy speaking Thalassic can be understood by any animal that has a swim Speed or the amphibious or aquatic trait. By spending a week regularly interacting with such an animal, the sedacthy can make it permanently helpful."
  - name: "Exploit Weakness"
    desc: "The speaker's Strikes deal 1d6 additional damage to creatures that are [[Frightened]] or [[Sickened]]."
armorclass:
  - name: AC
    desc: "23; **Fort** +14, **Ref** +13, **Will** +15"
health:
  - name: HP
    desc: "95"
abilities_mid:
  - name: "Speaker's Privilege"
    desc: "`pf2:r` **Trigger** The sedacthy speaker takes damage <br>  <br> **Requirements** The sedacthy speaker has cover from an animal ally <br>  <br> **Effect** The animal takes the damage instead."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +16 (`pf2:1`) (agile, unarmed), **Damage** 1d6+8 slashing"
  - name: "Melee strike"
    desc: "Jaws +16 (`pf2:1`) (unarmed), **Damage** 1d4 bleed plus 1d6+8 piercing"
  - name: "Melee strike"
    desc: "Trident +17 (`pf2:1`) (magical), **Damage** 1d8+10 piercing"
  - name: "Melee strike"
    desc: "Trident +14 (`pf2:1`) (magical, thrown 20), **Damage** 1d8+8 piercing"
spellcasting: []
abilities_bot:
  - name: "Animal Shield"
    desc: "`pf2:1` **Requirements** The sedacthy speaker is adjacent to a Large or larger animal ally <br>  <br> **Effect** The speaker gains cover until the start of their next turn or when they're no longer adjacent to the animal, whichever comes first."
  - name: "Painful Cry"
    desc: "`pf2:2` The sedacthy shrieks across a range of painfully high tones, dealing @Damage[3d6[sonic],1d6[mental]|options:area-damage]{3d6 sonic damage and 1d6 mental damage} to all creatures in a @Template[cone|distance:30], with a DC 23 [[Fortitude]] save. A creature that fails its save is [[Sickened]] 1."
  - name: "Shared Feast"
    desc: "`pf2:2` The sedacthy makes a jaws Strike. If it hits, an ally of their choice can spend a reaction to make a jaws Strike against the same target. Allies with beaks or similar attacks can use those instead of jaws."
  - name: "Swim Together"
    desc: "`pf2:2` **Requirements** The speaker is adjacent to an animal ally <br>  <br> **Effect** The speaker and the animal both Swim, ending their movement adjacent to one another."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

High-ranking sedacthies are expected to both plan campaigns and wade into battle. These speakers achieve their rank by accumulating several large servants or a single massive creature like a megalodon.

Sedacthies are amphibious, fish-like humanoids who lurk in Golarion's oceans and are known for leading their animal servants ashore to devour air breathers. When an entire fishing village disappears overnight, sedacthies are the first suspects. Sedacthies pride themselves as natural leaders, with ambition limited only by their strict adherence to hierarchy. A sedacthy's station is determined by the strength of the animal servants they press into service, and the mettle they prove during hunts and in battles against outsiders.

```statblock
creature: "Sedacthy Speaker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
