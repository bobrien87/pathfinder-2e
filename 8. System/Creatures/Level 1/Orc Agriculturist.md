---
type: creature
group: ["Humanoid", "Orc"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Orc Agriculturist"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Orc"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Common, Orcish"
skills:
  - name: Skills
    desc: "Athletics +5, Crafting +3, Nature +11, Survival +7, Farming Lore +13"
abilityMods: ["+2", "+1", "+2", "+0", "+4", "+0"]
abilities_top:
  - name: "Farming Specialist"
    desc: "For encounters involving farming, harvesting, or identifying plants, the agriculturalist is a 5th-level challenge."
armorclass:
  - name: AC
    desc: "14; **Fort** +9, **Ref** +6, **Will** +7"
health:
  - name: HP
    desc: "25"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pitchfork +7 (`pf2:1`) (reach), **Damage** 1d8+2 piercing"
  - name: "Melee strike"
    desc: "Sickle +7 (`pf2:1`) (agile, trip), **Damage** 1d4+2 slashing"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Blowgun +9 (`pf2:1`) (agile, nonlethal, reload 1, range 20 ft.), **Damage** 1 piercing"
spellcasting: []
abilities_bot:
  - name: "Herbal Poison"
    desc: "`pf2:1` The agriculturalist quickly turns some of their supplies of poisonous herbs into an herbal poison, then applies it to a melee weapon or piece of ammunition in their possession. The next successful attack with a weapon poisoned this way deals an additional 1d6 poison damage. The applied poison fades after its damage is applied to an attack or 1 minute passes, whichever happens first."
  - name: "Poison Detector"
    desc: "`pf2:2` The orc agriculturalist attempts a Farming lore check or [[Nature]] check to determine whether an object is poison or has been poisoned. The DC is the poison's DC (if any), or the standard DC of the poison's level. On a critical success, they also learn the number and types of poison involved."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

In the severe lands orcs occupy, there are no lush fields blooming with crops. An orc farmer must be tough and just as adept at foraging as planting and harvesting.

Orcs have a strict moral code encompassing valor and accomplishment, and they cast out those unwilling to follow it. For the last few generations, orcs have been trying to erase the narratives around their culture as being solely focused on war and violence. They invite other races and adventuring parties inside their holds so they may experience the truth of who the orcs are.

```statblock
creature: "Orc Agriculturist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
