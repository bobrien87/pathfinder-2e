---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Plague Doctor"
level: "5"
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
    desc: "Intimidation +9, Medicine +13, Religion +13, Plague Lore +13"
abilityMods: ["+0", "+1", "+4", "+2", "+4", "+2"]
abilities_top:
  - name: "Healing Hands"
    desc: "When the plague doctor casts [[Heal]], they roll d10s instead of d8s."
  - name: "Improved Communal Healing"
    desc: "When the plague doctor casts [[Heal]] targeting a single creature, the plague doctor also restores Hit Points equal to the spell's rank to themself or any other creature within range of the spell."
armorclass:
  - name: AC
    desc: "20; **Fort** +13, **Ref** +8, **Will** +13"
health:
  - name: HP
    desc: "70"
abilities_mid:
  - name: "+2 Circumstance Bonus on Saves vs. Disease"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +9 (`pf2:1`) (two hand d8), **Damage** 1d4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +10 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8 piercing"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 23, attack +15<br>**3rd** (5 slots) [[Heal]], [[Heal]], [[Heal]], [[Cleanse Affliction]], [[Cleanse Affliction]]<br>**2nd** (3 slots) [[Clear Mind]], [[Clear Mind]], [[Peaceful Rest]]<br>**1st** (3 slots) [[Detect Poison]], [[Cleanse Cuisine]], [[Cleanse Cuisine]]<br>**Cantrips** [[Guidance]], [[Light]], [[Message]], [[Sigil]], [[Stabilize]]"
  - name: "Cleric Domain Spells"
    desc: "DC 23, attack +15<br>**1st** [[Healer's Blessing]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

These healers, often seen wearing distinctive masks and burning powders to defend against airborne plagues, are as much feared as they are respected. To see a plague doctor signals that disease has infested the land—and that it might have already taken hold.

The world is a dangerous place. Thankfully, there are those who devote their lives to easing the pain and suffering of others.

```statblock
creature: "Plague Doctor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
