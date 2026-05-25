---
type: creature
group: ["Dwarf", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dwarf Smith"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Dwarf"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Common, Dwarven"
skills:
  - name: Skills
    desc: "Athletics +6, Crafting +12, Society +6"
abilityMods: ["+2", "+1", "+2", "+3", "+1", "-1"]
abilities_top:
  - name: "Blacksmithing Specialist"
    desc: "For encounters involving blacksmithing, the dwarf smith is a 5th-level challenge."
  - name: "Temper Armament"
    desc: "The smith spends 1 day tempering a single suit of metallic armor, metallic shield, or metallic weapon. Tempering armor or a shield increases its Hardness by 1. Tempering a weapon grants the weapon a +1 circumstance bonus to damage rolls. Regardless of the item, the tempering remains for 3 days, after which item is temporarily immune to further tempering for 1 week as the technique would otherwise damage it. <br>  <br> > [!danger] Effect: Temper Armament"
armorclass:
  - name: AC
    desc: "14; **Fort** +6, **Ref** +3, **Will** +5"
health:
  - name: HP
    desc: "12; **Resistances** fire 1"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Clan Dagger +6 (`pf2:1`) (agile, parry, versatile b), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Light Hammer +6 (`pf2:1`) (agile), **Damage** 1d6+2 bludgeoning"
  - name: "Melee strike"
    desc: "Light Hammer +4 (`pf2:1`) (agile, thrown 20), **Damage** 1d6+2 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Crack the Shell"
    desc: "`pf2:2` The dwarf smith makes a Strike to break a creature's defenses. If the Strike hits and the creature is wearing armor with Hardness 9 or lower, the armor is [[Broken]]. This Strike doesn't further damage armor that's already broken."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Many dwarves become smiths as their attention to detail, lifestyles that keep them close to useful materials such as iron, and a pride in their work all come together to become a brilliant skill set for working with armaments. Though dwarves are capable of smithing most any kind of item, most focus on armaments as a way of creating objects to defend their fellow dwarves.

From the dwarven perspective, most things in life are best done correctly, and that means taking one's time. Dwarves are a focused and intentional people, taking years or even decades to ply their trades, doing their best to make every detail perfect. The patience and dedication required for such tasks pays off, and many dwarves become experts in their respective field, trade, or area of focus. Many dwarves uphold traditions, and since dwarven origins trace back to underground life, many still hone skills focused on life underground.

```statblock
creature: "Dwarf Smith"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
