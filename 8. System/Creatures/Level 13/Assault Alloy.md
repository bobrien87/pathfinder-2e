---
type: creature
group: ["Elemental", "Metal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Assault Alloy"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Elemental"
trait_02: "Metal"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Darkvision]]"
languages: "Common, Talican"
skills:
  - name: Skills
    desc: "Arcana +27, Athletics +23, Crafting +23, Stealth +22, Thievery +24, Metal Lore +29, Plane of Metal Lore +29"
abilityMods: ["+4", "+7", "+5", "+8", "+6", "+4"]
abilities_top:
  - name: "Idle Transmutation"
    desc: "An assault alloy has full alchemical control over the properties of their metal. Each time they make a metal needle Strike or Cast a Spell with the metal trait, they choose whether the metal they use is adamantine, cold iron, dawnsilver, or any other solid precious metal."
armorclass:
  - name: AC
    desc: "31; **Fort** +20, **Ref** +26, **Will** +23"
health:
  - name: HP
    desc: "240; **Immunities** bleed, paralyzed, poison, sleep; **Resistances** electricity 10"
abilities_mid:
  - name: "Instinctive Alloy"
    desc: "`pf2:r` **Trigger** The assault alloy is hit by an attack with a metal weapon or metal spell or effect <br>  <br> **Effect** The physical damage from the triggering weapon, spell, or effect instead restores the assault alloy's Hit Points as they seamlessly incorporate some of the metal used into their body. If already at full Hit Points, the assault alloy gains temporary Hit Points that last for 1 round instead. If a metal weapon triggers this, the weapon's die size decreases by one step to a minimum die size of d4 for 1 minute, and that weapon can't trigger Instinctive Alloy again during this time."
  - name: "Metal Manipulation"
    desc: "30 feet. An assault alloy has control over all unattended metal within the emanation and can use any of this metal as the origin point for their metal needle ranged Strikes."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +27 (`pf2:1`) (agile, finesse), **Damage** 3d10+11 slashing"
  - name: "Ranged strike"
    desc: "Metal Needle +27 (`pf2:1`) (agile, arcane, magical, range 60 ft.), **Damage** 3d8+11 piercing plus [[Idle Transmutation]]"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 33, attack +25<br>**6th** [[Wall of Metal]]<br>**5th** [[Impaling Spike]]<br>**4th** [[Rust Cloud]]<br>**1st** [[Detect Metal]]"
abilities_bot:
  - name: "Metal Blink"
    desc: "`pf2:1` **Requirements** The assault alloy is adjacent to metal of at least 1 bulk <br>  <br> **Effect** An assault alloy can liquefy the metals of their body and travel up to their Speed through spaces with contiguous metal, even if it's not uniformly connected (as in a scrap heap or a pile of treasure). This movement doesn't trigger reactions."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`



```statblock
creature: "Assault Alloy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
